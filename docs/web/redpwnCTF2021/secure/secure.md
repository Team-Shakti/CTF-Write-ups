# secure

## Description
Any input you give on this page is converted to Base64 before passing. From the source we can see that username `admin` is encoded using btoa() before inserting.

```javascript
db.exec(`INSERT INTO users (username, password) VALUES (
    '${btoa('admin')}',
    '${btoa(crypto.randomUUID)}'
)`);
```
Neither username nor password field can be empty. We will get the flag if the query returns any results.

```javascript
app.post('/login', (req, res) => {
  if (!req.body.username || !req.body.password)
    return res.redirect('/?message=Username and password required!');

  const query = `SELECT id FROM users WHERE
          username = '${req.body.username}' AND
          password = '${req.body.password}';`;
  try {
    const id = db.prepare(query).get()?.id;

    if (id) return res.redirect(`/?message=${process.env.FLAG}`);
    else throw new Error('Incorrect login');
  } catch {
    return res.redirect(
      `/?message=Incorrect username or password. Query: ${query}`
    );
  }
});
```

## Solution
The encoding is done on client-side using JavaScript. Any security mechanisms implemented on client-side is no security at all as it can easily be modified. Send a request with random values.

![index](../../images/6.png)

Capture request using Burp. SQLi using password parameter. 

![index](../../images/7.png)

All ids will be returned and we will get the flag.

![index](../../images/8.png)