# orm-bad

## Description
Looking at the source we can see that username needs to be `admin` to get the flag.

```javascript
app.post('/flag', (req, res) => {
    db.all("SELECT * FROM users WHERE username='" + req.body.username + "' AND password='" + req.body.password + "'", (err, rows) => {
        try {
            if (rows.length == 0) {
                res.redirect("/?alert=" + encodeURIComponent("you are not admin :("));
            } else if(rows[0].username === "admin") {
                res.redirect("/?alert=" + encodeURIComponent(flag));
            } else {
                res.redirect("/?alert=" + encodeURIComponent("you are not admin :("));
            }
        } catch (e) {
            res.status(500).end();
        }
    })
})
```
  
## Solution
The query is vulnerable to SQLi. Use `-- ` after `admin` to comment out the rest of the query.

![index](../../images/1.png)

This essentially removes the password check.

```SELECT * FROM users WHERE username=admin```

![index](../../images/2.png)