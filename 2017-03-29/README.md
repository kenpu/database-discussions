# Building a web application that uses a database

## Requirements:

- Python
- Flask
- SQLite3 (python driver and command-line)

See `http://flask.pocoo.org/`

## Setup

```
pip install flask
```

## Hello world

A simple web application that says "Hello".

Note:

Python has a decorator syntax.  If `f` is a function, then

```
@g
f
``` 
is equivalent to `g(f)`.  So `@` applies a function that takes a function
as an input to some function.

Therefore,

```
@app.route("/")
def Hello():
    ...
```

Is equivalent to:

```
def Hello():
    ...

app.route("/")(Hello)
```

