import os
from flask import Flask, render_template, redirect, request, url_for, request, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt
from os import path
if path.exists("env.py"): 
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'paw_purfect_planner'
app.config['MONGO_URI'] = os.environ['MONGO_URI']
app.secret_key = 'somesecretkey'

mongo = PyMongo(app)

@app.route('/', methods=["GET", "POST"])
def index():
    if 'username' in session:
        return render_template("userprofile.html")
    
    return render_template("index.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'name' : request.form['username']})

        if login_user:
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                session['username'] = request.form['username']
                return render_template("userprofile.html")
            flash('Invalid username/password combination')
    return render_template('index.html', page_title="Please Login")

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template("register.html")


@app.route('/endsession')
def endsession():
    """End session."""
    session.clear()
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)