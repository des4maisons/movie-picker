movie-picker
============

An app that stores movie titles and retrieves random ones.
So that hacklab doesn't have such a hard time choosing movies.

Install
-------

```bash
cd <this-repo>
virtualenv env
. env/bin/activate
pip install -r requirements.txt
```

Run
---

```bash
cd site
python serve.py
```

Use
---

```bash
curl -X GET 127.0.0.1:5000/  # gives help
curl -X POST 127.0.0.1:5000/movies -d 'title=foo'  # adds movie 'foo' to database
curl -X GET 127.0.0.1:5000/movies/random  # returns the name of a random movie
```
