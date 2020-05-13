![Paw Purfect Site Header Image](https://github.com/TiffanyDonner/paw-purfect-planner/blob/master/static/readme/header-readme.PNG)
# 🐾Paw Purfect Planner
What did the Vet say the last time we were there? When was the last time Rocco had his shots? This is something we often say as pet owners. Paw Purfect Planner is a simple web application that gives you everything you need to maintain your pet records and events.

## Table of Contents

1. [Demo](#Demo)
2. [Project Purpose](#Project-purpose)
3. [UX](#ux)
    - [User Stories](#User-stories)
4. [Features](#Features)    
5. [Technology Used](#Technology-Used)
6. [Testing](#Testing)
7. [Deployment](#Deployment)
8. [Credits](#Credits)

## Demo
A live demo of the website can be found [here](https://paw-purfect-planner.herokuapp.com/).

## Project Purpose
To build a CRUD (Create, Read, Update, Delete) application using HTML, CSS, JavaScript, Python+Flask, and MongoDB.

## UX
#### The ideal Paw Purfect User is:
- Reading and Speaking English
- A pet owner or a pet sitter
- Busy, so keeping all their pet information in one place and easy to access is important.

#### Strategy
The strategy of the design was to give the user a clean and easy way to access all their pets information all from one user profile.

#### Scope
The visitors of this site will get quick access to an overview of there pet's important information. They will be able to schedule important upcoming appointments. Also giving them a view into their pet's history.

#### Structure
Most pet record sites leave the pet owner bogged down with features that are hard to find. I am starting the build on the site to be simple with nested functions that are intuitively placed. The future builds will be based on this original design.

#### Skeleton
Wireframes presentation designed in Adobe XD. Click the green text/button or next to view pages. [XD Share Link](https://xd.adobe.com/view/d3d4d633-9037-43ba-7e94-c97a5ff472d3-a5e5/)

#### Surface
Natural earth tones that reflex earth and sky.

### User Stories
#### SOFIA AND BELLA
Sofia wants to keep track of important information about her Ragdoll cat Bella. She wants to be able to access the information quickly and easily. She wants to receive 2 reminders when she needs to go to the veterinarian next and when to apply Bellas Flea and Tick Medication.
- Features she needs:
    - A place to track Bella’s weight.
    - Event schedule of what she has already had and when she needs to visit a veterinarian next.
    - A place to keep emergency vet appointment notes.
    - Reminders on when to next apply Bella’s flea and Tick medication.

#### RANDY AND ROSCOE
Randy has a very active American Stafford Terrier, Roscoe, that is accident prone. Randy would like a place that he can store important information that can be accessed easily in case of an emergency.
- Features he needs:
    - A list of past and upcoming visits to the vet.
    - Roscoe's proof of vaccination and schedule

## Features
### Paw Purfect Planner (BETA)
The site uses Materialize to enhance the site by providing a responsive design, clean scrolling and nifty form features.
#### Header Logo
Resides at the top of every page in the navigation bar. The logo is linked to the home page for users not logged in and the user profile for logged in users as expected.
#### Navigation Bar
Exists on every page to easily navigate through the website's core features.
#### Create
Each user can create a user account, create a pet profile, and add events through forms.
#### Read
Each registered user can read their data through their User Profile page. The data view also includes a Materialize collapsable heading where they can view additional information.
#### Update
From the Profile page, the user can edit their pet or event, and navigate to a form to update the database with their new information. 
#### Delete
If the user feels they no longer need a record they have entered, they have the option to delete it.
#### Footer
Resides at the bottom of each page to establish closure and to protect the business copyright.

### Features Left To Implement
This is an ongoing project and will go fully live later in 2020. 
#### Next Release 1.5:
- Create a forgot password link for the user.
- Log the user out automatically after a time period.
- About and Contact Page
- Add a search feature to events with the most recent event first in the list.
- Mark an event as done and create a history page that is will be added to.
- Add the ability to add contacts.
- Add an email to the registration form.
- Create a user profile where the user can update account information such as email and change password.
- Ability to upload documents into an event.
- The current setup allows anyone to edit pets/events that do not belong to them. Need to check whether the event or pet belongs to session['username'] first before updating. If not, redirect them to their User Profile.

#### Future Updates
- Add the ability to add a pet photo to the profile page.
- Create a button to add Logo, with hyperlink to website, to users' home screen.
- Add the ability to connect an event to a pet.
- Connect contacts' address to google maps.
- Connect the contact's phone number to a dialer.

## Technology Used
| Languages | Libraries | Tools | Hosting |
|----------------------------------|----------------------------------|----------------------------------|----------------------------------|
| [HTML](https://www.w3.org/html/) | [Materialize](https://materializecss.com/) | MongoDB | Github
|    - To provide the structure of the webiste. | [Google Fonts](https://fonts.google.com/) |  | Heroku
| [CSS](https://www.w3.org/Style/CSS/Overview.en.html) | [jQuery] 3.4.1 | 
|    - To make the website look better visually. | Flask | 
| [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) | Flask-PyMongo | 
|    - Materialize functionality. | Dnspython | 
| [Python](https://www.python.org/) | py-bcrypt | 

## Testing
- [Manual Testing (PDF)](https://github.com/TiffanyDonner/paw-purfect-planner/blob/master/static/readme/manual-testing.pdf)
- [Validation Testing (PDF)](https://github.com/TiffanyDonner/paw-purfect-planner/blob/master/static/readme/testing-validators.pdf)
- [Database Testing (PDF)](https://github.com/TiffanyDonner/paw-purfect-planner/blob/master/static/readme/database-testing.pdf)

## User Testing
### Questions and Answers
(Each Tester was asked to send a screenshot of the home page and the user profile page.)

#### When you clicked on the [link provided](http://paw-purfect-planner.herokuapp.com/), was the website purpose clear?
- User A, "Yes, it was clear. I was able to find the registration page and register for an account."
- User B, "I am not really sure what the site does... I can tell it's about pets?"
    - Update: I added additional text to the greeting to make the purpose of the website more clear.

#### After you filled in the registration form, were you able to intuitively know what your next step was?
- User A, "No. I can't find where to add my pet's information."
    - Update: I added an add pet button below pet information.
- User B, "Yes, I used the navigation menu to add a pet to my profile page.

#### When you add an event, is it clear where to find and edit the information for that event?
- User A, "Yes. No problem."
- User B, "Yes, but the dates are out of order and nothing happens on the user profile page when I mark it urgent.
    - Update: These features will be added in the next update.

#### Would you use the website to keep track of your important pet information?
- User A, "I think I would like more features if I was going to use this exclusively for my pets. Rather than just using my google calendar..."
- User B, "Sure, seems like a good idea. I am looking forward to seeing what gets added in the future."

Any suggestions given by users have been added above in [Features Left To Implement](#Features-Left-To-Implement)

### Devices Tested
✓ The site is accessible to everyone on all devices.<br/>
✓ Both Windows and Apple computers in:<br/>
    - Chrome<br/>
    - Firefox<br/>
    - Microsoft Edge<br/>
✓ Samsung:<br/>
    - Galaxy S9<br/>
    - Galaxy S9 Plus<br/>
    - Galaxy S5 Note<br/>
✓ Caterpillar Android Device<br/>
✓ Apple:<br/>
    -iPhone 11<br/>
    -iPhone 10<br/>

## Deployment
#### 1. MongoDB Database Set-up
1. Sign in to your [MongoDB Account](https://www.mongodb.com/) account.
2. Navigate to or create a project.
3. [Create a Database](https://github.com/TiffanyDonner/paw-purfect-planner/blob/master/static/readme/database-testing.pdf)
4. Add a collection to your database.
5. Add a Document to your collection.

#### 2. Create a new [repository](https://github.com/TiffanyDonner/paw-purfect-planner) in GitHub
1. In the upper right corner use the + to bring down the menu. And select Repository.
2. Select your account from the owner dropdown menu.
3. Give your repository a name and optional description.
4. Choose the repository's visibility and initialize this repository with a README.
5. Click Create Repository

#### 3. Create Your Website
1. In GitHub navigate to your repository.
2. Click on the green Gitpod button to open your development environment.
3. Create a [template folder](https://github.com/TiffanyDonner/paw-purfect-planner/tree/master/templates) and add an index.html with what you want to be displayed on the main page of your site.
4. Push your files and folders while updating git by adding files with commit messages to keep you organized through development.

#### 4. Create an App in Heroku
1. Sign in to your [Heroku Account](https://heroku.com/) and create a unique app.
2. Navigate to Deploy and choose GitHub as your deployment method.
3. Navigate to App connected to GitHub and connect your GitHub Repository.
4. Then Enable Automatic Deploys.
5. Now your Heroku app will update every time you push GitHub (git add ., git commit -m "", git push)

#### 5. Create a Flask Application
1. In the terminal install flask *pip3 install flask*
2. Create an app.py file in the root directory.
3. Create an instance of Flask in the app.py file *app = Flask(__name__)*
4. Then do a test. You can find a sample on how to set-up a test app.py file [here](https://github.com/Code-Institute-Solutions/TaskManager/blob/master/01-PuttingTheBasicsInPlace/02-create_the_flask_application/app.py)
5. Create a requirements file *pip3 freeze --local > requirements.txt*
6. Create procfile using *echo web: python app.py > Procfile*
7. Add, commit and push your changes to GitHub from you terminal and now when you view your app on Heroku you should be ab
8. In Heroku navigate to Settings, Config Vars. Set your IP and PORT.
9. Now when you Open App from Heroku you should see your test page.

#### 6. Connect Flask To MongoDB Atlas
1. Install library in the terminal *pip3 install flask pymongo*
2. Install new connection string in the terminal *pip3 install dnspython*
3. Add additional imports to app.py
4. To set up your MongoDB connection during testing use these [instructions](https://github.com/TiffanyDonner/paw-purfect-planner/blob/master/static/readme/environment-variables-gitpod.pdf) to keep your database environment variables secret.
4. Create Templates folder and initial html file, events.html, and start building your website.

#### 7. Last... Remember to add your MongoDB environment variables to Heroku to complete the deployment.
1. In Heroku navigate to Settings, Config Vars.
2. Set your MONGO_URI and environment variables.

## Credits
- Code Institue, [TaskManager Lesson](https://github.com/Code-Institute-Solutions/TaskManager): For basic event Function
- My mentor Brian Macharia, Code Institute Tutors, and Slack Group!
- Creating a User Login System Using Python, Flask and MongoDB [Pretty Printed](https://www.youtube.com/watch?v=vVx1737auSE)
- Ewan Lockwood, [The Book Stop](https://github.com/ewanlockwood/the-book-stop): For structure on how to implement a login system.
- Px Here, [Banner Image](https://pxhere.com/en/photo/1597775)
