import os
from flask import Flask, render_template, url_for, request, session, redirect
from flask.ext.pymongo import PyMongo
import bcrypt


app = Flask(__name__)


app.config["MONGO_DBNAME"] = 'paw_purfect_planner'
app.config['MONGO_URI'] = os.environ['MONGO_URI']
app.secret_key = os.getenv("SECRET")


mongo = PyMongo(app)


@app.route('/')
def hello():
    return 'Hello World ...again'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)