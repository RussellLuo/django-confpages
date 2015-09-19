# Form Page

An example showing how to create configurable pages containing form submissions, which are handled by the backend API.


## Usage

### 1. Start the MongoDB server

```
$ mongod
```

### 2. Prepare some data

```
$ mongo
> use test
> content = '<form action="." method="POST">{% one_time_token %}<input type="hidden" name="_method" value="PUT" /><input type="text" name="data" value="" /><input type="submit" /></form>'
> api_url = 'http://127.0.0.1:5000/index'
> db.page.insert({name: 'index', title: 'Form submissions', content: content, api_url: api_url})
```

### 3. Install additional dependencies

Install `pymongo` to make it possible for `Django-ConfPages` to communicate with MongoDB:

```
$ pip install pymongo
```

Install `RESTArt` for building the backend API:

```
$ pip install Python-RESTArt
```

### 4. Run the API

```
$ cd examples/formpage/api
$ restart api:api
 * Running on http://127.0.0.1:5000/
```

### 5. Run the Django project

```
$ cd examples/formpage
$ python manage.py runserver
...
Starting development server at http://127.0.0.1:8000/
...
```

Now access `http://127.0.0.1:8000/` in your browser, and submit the form.
