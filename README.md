![Paw Purfect Site Header Image](https://github.com/TiffanyDonner/paw-purfect-planner/blob/master/static/images/readme/header-readme.PNG)
# 🐾Paw Purfect Planner
What did the Vet say the last time we were there? This is something we often say as pet owners. Paw Purfect Planner is a simple web application that gives you everything you need to maintain your pet records and events.
## Table of Contents

1. [Demo](#Demo)
2. [Project purpose](#Project-purpose)
3. [UX](#ux)
    - [User stories](#User-stories)
4. [Features](#Features)    
5. [Technology Used](#Technology-Used)
6. [Testing](#Testing)
7. [Credits](#Credits)
8. [DEPLOYMENT](#DEPLOYMENT)

## Demo
A live demo of the website can be found [here](https://paw-purfect-planner.herokuapp.com/).

## Project-purpose
To build a CRUD (Create, Read, Update, Delete) application using HTML, CSS, JavaScript, Python+Flask, and MongoDB.

## UX
#### The ideal Paw Purfect User is:
- Reading and Speaking English
- A pet owner or a pet sitter
- Busy, so keeping all their pet information in one place and easy to access is important.

#### Stradegy
The stradegy of the design was to give the user a clean and easy way to access their pets information all from one user profile.

#### Scope
The vistors of this site will get quick acces to an overview of there pets important information. They will be able to schedule important upcoming appointments. Also giving them a view into their pets history.

#### Structure
Most pet record sites leave the pet owner bogged down with features that are hard to find. I am starting the build on the site to be simple with nested functions that are intuativly placed. The future builds will be based on this original design.

#### Skeleton
- Wireframes [XD Share Link](https://xd.adobe.com/view/202021a4-b5e4-4aa5-77a7-936194d5fdf4-5611/?fullscreen&hints=off)
- Database design [XD Share Link](https://xd.adobe.com/view/202021a4-b5e4-4aa5-77a7-936194d5fdf4-5611/?fullscreen&hints=off)

#### Surface
Natural earth tones that reflex earth and sky.

### User-stories
#### SOFIA AND BELLA
Sofia wants to keep track of important information about her Ragdoll cat Bella. She wants to be able to access the information quickly and easily. She wants to receive 2 reminders when she needs to go to the veterinarian next and when to apply Bellas Flea and Tick Medication .
Features she needs.
- A place to track Bella’s weight.
- Event schedule of what she has already had and when she needs to visit a veterinarian next.
- A place to keep emergency vet appointment notes.
- Reminders on when to next apply Bella’s flea and Tick medication.

#### RANDY AND ROSCOE
Randy has a very active American Stafford Terrier, Roscoe, that is accident. Randy would like a place that he can store important information that can be accessed easily in case of an emergency.
- A list of last and upcoming visits to the vet.
- Roscoe's proof of vaccination and schedule

## Features
The site uses Materialize to enhance the site design by providing a responsive design, clean scrolling and nifty form features.

### Features left to impliment
This is an ongoing project and will go fully live later in 2020. 
#### Next Release 1.5:
- About and Contact Page
- Add the appbility to add a pet photo.
- Add a search feature to events with most recent event first in list.
- Mark an event as done and add it to a history page.
- Create popup to add webpage to home screen.
- Add the ability to add contacts.
- Add email to the register form.
- Ability to uplaod documents into an event.

#### Future of 🐾Paw Purfect Planner
Demonstration of what Paw Putfect Planner will look like in the future [XD Share Link](https://xd.adobe.com/view/202021a4-b5e4-4aa5-77a7-936194d5fdf4-5611/?fullscreen&hints=off)

## Technology-Used
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

Tested CSS in w3 (2) errors found and corrected:
1. Bad value: 
    - Corrected by 
2. Error
    - Corrected by 

W3C CSS Validator results: 

W3 Link Validator results: 

W3C Internationalization Checker
1. (5) "<b>" tags without class
    - Added the HTML class of totals. Since they related to the totals on the final tab.

## User Testing
### Devices Tested
✓ The site is accessible to everyone on all devices.
✓ Both Windows and Apple computers in:
    - Chrome
    - Firefox
    - Microsoft Edge
✓ Samsung:
    - Galaxy S9
    - Galaxy S9 Plus
    - Galaxy S5 Note
✓ Caterpillar Android Device
✓ Apple:
    -iPhone 11
    -iPhone 10

## Credits
- Code Institue, [TaskManager Lesson](https://github.com/Code-Institute-Solutions/TaskManager): For basic event Function
- Ewan Lockwood, [The Book Stop](https://github.com/ewanlockwood/the-book-stop): For structure on how to impliment a login system.
- Px Here, [Banner Image](https://pxhere.com/en/photo/1597775)

## DEPLOYMENT
### GitHub Deployment with GitHub Pages

#### Create a new [repository](https://github.com/TiffanyDonner/paw-purfect-planner). 
1. In the upper right corner use the + to bring down the menu. And select Repository.
2. Select your account from the owner dropdown menu.
3. Give your repository a name and optional description.
4. Choose the repository's visibility and initialize this repository with a README.
5. Click Create Repository

#### Create Your Website
1. In GitHub navigate to your repository.
2. Click on the green Gitpod button to open your development environment.
3. Create an index.html in the root with what you want to be displayed on the main page of your site.
4. Push your files and folders while updating git by adding files with commit messages to keep you organized through development.

#### Deployment to GitHub Pages
1. In GitHub, navigate to Settings. Within Settings, navigate to the Source section under Github Pages. 
2. From the dropdown menu, selected master branch and selection will save automatically. 
3. Git hub creates a [link](https://tiffanydonner.github.io/paw-purfect-planner/) to where the site is hosted/published.

#### Updating
1. Any updates that are committed and push to GitHub will be updated to GitHub Pages.

### Heroku Deployment with GitHub Pages