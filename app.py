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
    user = mongo.db.users.find_one({'_id': ObjectId(session['username_id'])})
    events = mongo.db.events.find({'owner': user['username']})
    return render_template("events.html", events=events)

@app.route('/add_event', methods=['POST', 'GET'])
def add_event():
    """*user = mongo.db.users.find_one({'_id': ObjectId(session['username_id'])})"""
    if 'username' in session:
        return render_template('addevent.html', 
                                categories=mongo.db.categories.find(), user=session['username'])
    return render_template('index.html')

@app.route('/insert_event', methods=['POST'])
def insert_event():
    events =  mongo.db.events
    event_data = request.form.to_dict()
    event_data['username'] = session['username']
    events.insert_one(event_data)
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

@app.route('/get_pets')
def get_pets():
    user = mongo.db.users.find_one({'_id': ObjectId(session['username_id'])})
    pets = mongo.db.pet_profile.find({'owner': user['username']})
    return render_template("pets.html", 
                           pets=pets)

@app.route('/add_pet', methods=['POST', 'GET'])
def add_pet():
    if 'username' in session:
        return render_template('addpet.html',
                            users=mongo.db.users.find())
    return render_template('index.html')

@app.route('/insert_pet', methods=['POST'])
def insert_pet():
    pets =  mongo.db.pets
    pets.insert_one(request.form.to_dict())
    return redirect(url_for('get_pets'))

@app.route('/edit_pet/<pet_id>')
def edit_pet(pet_id):
    the_pet =  mongo.db.pet_profile.find_one({"_id": ObjectId(pet_id)})
    all_types =  mongo.db.type.find()
    all_genders = mongo.db.gender.find()
    return render_template('editpet.html', pet=the_pet,
                           types=all_types, gender=all_genders)

@app.route('/update_pet/<pet_id>', methods=["POST"])
def update_pet(pet_id):
    pets = mongo.db.pets
    pets.update( {'_id': ObjectId(pet_id)},
    {
        'pet_name':request.form.get('pet_name'),
        'pet_type':request.form.get('pet_type'),
        'gender': request.form.get('gender'),
        'pet_breed': request.form.get('pet_breed'),
        'birth_date':request.form.get('birth_date')
    })
    return redirect(url_for('get_pets'))

@app.route('/delete_pet/<pet_id>')
def delete_pet(pet_id):
    mongo.db.pets.remove({'_id': ObjectId(pet_id)})
    return redirect(url_for('get_pets'))

@app.route('/userprofile')
def userprofile():
    user = mongo.db.users.find_one({'_id': ObjectId(session['username_id'])})
    pets = mongo.db.pet_profile.find({'owner': user['username']})
    user = mongo.db.users.find_one({'_id': ObjectId(session['username_id'])})
    events = mongo.db.events.find({'owner': user['username']})
    return render_template("userprofile.html", pets=pets, events=events)

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
                session['username_id'] = str(login_user['_id'])
                return redirect(url_for('userprofile'))
            
        return redirect(url_for('invaliduser'))

@app.route('/register', methods=['POST', 'GET'])
def register():
    """ If username already exists renders login.html,
    if does not exist, renders register.html """
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            inserted_user = users.insert_one({'username' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            session['username_id'] = str(inserted_user.inserted_id)
            print (session['username_id'])
            return render_template('userprofile.html')
        
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