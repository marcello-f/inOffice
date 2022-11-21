# inOffice
### Video Demo:  https://youtu.be/uYGHjPHyYRk
### Description:

##### Introduction:
In this new era of hyrbid/remote working, it can be difficult to arrange time in the office together. I built this project to enable users to easily keep track of when all their colleagues, and themselves, are going to be in the office.

In this document I will explain what each file in this project accomplishes. 

##### main.py:
This file simply imports the project from the package and runs it.

##### __init__.py:
This file marks the folder as a Python package directory. Having a package is beneficial as it allows us to split the project into multiple files and folders, which helps with organisation. Within this file we also initialise a whole host of features including; the database which stores our data, the login manager which manages user sessions and the scheduler which allows us to run a job which moves data within the database. We also create the application itself in this file.

##### auth.py:
This file contains the routes for the signup, login and logout features. Signup checks for a set of requirements before adding the new users data to the database tables. The users password is hashed for security. Login finds the users details in the databse and ensures they match with those the user inputed before logging them in. Logout simply ends the users session, logging them out. I chose to have a separate file for these routes as they are all focused on authorisation and authentication so it made sense to group them together for better organisation.

##### models.py:
This file contains the models which are used to build the tables in the database. We have two tables, user and tracker. The user table stores all the user details such as email, password and names when a user registers. The tracker table stores data for which days of the week the user will be in the office. The primary key for the database is the user id and the two tables are related to each other through this.

##### tasks.py:
This file contains a single task for the scheduler to run. This task is set to run every Monday at 00:00 hours. What it does is transfer all the 'next week' data to 'this week' and sets all the next weeks data to none so users do not have to automatically reset the days they are in office. 

##### views.py:
This file contains the routes which the user will see on the frontend. The home route takes in data from forms on the homepage and stores it in the tracker table in the database. There is also some variables and a function which use the datetime package to pass through current dates to the frontend. The profile route simply returns the profile page. The edit-profile route takes in data from forms on the profile page and updates the user table in the database. The deletion route finds the user in the database, logs the user out, then deletes their data in both tables.

##### templates:
This folder contains all the HTML pages which the user sees. Bootstrap is throughout the project for elements and styling. The first is base.html which contains the core of the website. It has the head with all the metadata and links for styling. It also contains the navbar which appears in all other pages. Jijna is then used to extend the base for other pages. All other pages are have a basic but effective frontend. home.html has a couple of tables. The first displaying when each user will be in the office, this week and next. The second tables is for users to enter the days they will be in the office. All other pages have self explanatory names and are made up of forms which allow the user to input data.

##### static:
This folder contains an image for the icon on the taskbar and one for the profile page. Both in png format. There is also a css folder which has a CSS style sheet for a handful of customisations. 

##### .gitignore:
This file is in place to tell git which files and folders to ignore when pushing. I did this as I was running the project in a virtual environment and did not want that being uploaded to github. Additionally it prevented the database from being uploaded to github.