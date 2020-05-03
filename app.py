import os
from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import bcrypt
from os import path
if path.exists("env.py"): 
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'paw_purfect_planner'
app.config['MONGO_URI'] = os.environ['MONGO_URI']
app.secret_key = 'somesecretkey'

mongo = PyMongo(app)

@app.route('/')
def home():
    if 'username' in session:
        return render_template('user_profile.html')

    return render_template('home.html')

@app.route('/login')
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('home'))
    
    return 'Invalid username/password combination'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('home'))
        
        return 'That username already exists!'

    return render_template('register.html')


@app.route('/end_session')
def end_session():
    """End session."""
    
    session.clear()
    return render_template("home.html")


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)