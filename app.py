import os
from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import bcrypt
from bson.objectid import ObjectId

""" Congfiguration of env.py file with MongoDB login """
from os import path
if path.exists("env.py"):
    import env

""" Congfiguration of MongoDB with PyMongo """
app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'paw_purfect_planner'
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = 'somesecretkey'

mongo = PyMongo(app)


@app.route('/')
def index():
    """ Landing page with login / index.html """
    if 'username' in session:
        return redirect(url_for('userprofile'))

    return render_template('index.html')

@app.route('/get_events')
def get_events():
    return render_template("events.html", 
                           events=mongo.db.events.find())

@app.route('/add_event')
def add_event():
    return render_template('addevent.html',
                           categories=mongo.db.categories.find())

@app.route('/insert_event', methods=['POST'])
def insert_event():
    events =  mongo.db.events
    events.insert_one(request.form.to_dict())
    return redirect(url_for('get_events'))

@app.route('/edit_event/<event_id>')
def edit_event(event_id):
    the_event =  mongo.db.events.find_one({"_id": ObjectId(event_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editevent.html', event=the_event,
                           categories=all_categories)

@app.route('/update_event/<event_id>', methods=["POST"])
def update_event(event_id):
    events = mongo.db.events
    events.update( {'_id': ObjectId(event_id)},
    {
        'event_name':request.form.get('event_name'),
        'category_name':request.form.get('category_name'),
        'event_description': request.form.get('event_description'),
        'due_date': request.form.get('due_date'),
        'is_urgent':request.form.get('is_urgent')
    })
    return redirect(url_for('get_events'))

@app.route('/delete_event/<event_id>')
def delete_event(event_id):
    mongo.db.events.remove({'_id': ObjectId(event_id)})
    return redirect(url_for('get_events'))

@app.route('/userprofile')
def userprofile():
    
    return render_template("userprofile.html")

@app.route('/invaliduser')
def invaliduser():
    
    return render_template("invalid.html")

@app.route('/existinguser')
def existinguser():
    
    return render_template("existinguser.html")

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        login_user = mongo.db.users.find_one({'username': username})
        
        if login_user:
            if bcrypt.hashpw(
                    request.form['pass'].encode('utf-8'),
                    login_user['password']):
                session['username'] = request.form.to_dict()['username']
                return redirect(url_for('userprofile'))
            
        return redirect(url_for('invaliduser'))

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'username' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('userprofile'))
        
        return render_template('existinguser.html')

    return render_template('register.html')

@app.route('/end_session')
def end_session():
    """End session."""
    
    session.clear()
    return render_template("index.html")


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)