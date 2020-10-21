# REST_API_Workshop

Setup server reload in development
```sh
export FLASK_APP=main.py
export FLASK_ENV=development
flask run --port <port-number>
```

Mock Up Data:

Open the `db_populate.py` file on the main directory. Change the database connection string to the location of your mongodb. run `python db_populate.py`.


Database engine **pymongo**

Another test for webhooks 1