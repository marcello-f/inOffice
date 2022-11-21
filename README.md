# inOffice
### Video Demo:  <URL HERE>
### Description:

##### Introduction:
In this new era of hyrbid/remote working it can be difficult to arrange time in the office together. I built this project to enable users to easily keep track of when all their colleagues, and themselves, are going to be in the office. 

In this document I will explain what each file in this project accomplishes. 

##### main.py:
This file simply imports the project from the package and runs it.

##### __init__.py:
This file marks the folder as a Python package directory. Having a package is beneficial as it allows us to split the project into multiple files and folders, which helps with organisation. Within this file we also initialise a whole host of features including; the database which stores our data, the login manager which manages user sessions and the scheduler which allows us to run a job on Monday morning which moves data within the database. We also create the application itself in this file.

##### auth.py:
This file contains the routes for the signup, login and logout features. I chose to have a separate file for these routes as they are all focused on authorisation and authentication so it made sense to group them together for better organisation.

##### models.py:
This file contains the models which are used to build the tables in the database. We have two tables, user and tracker. The user table stores all the user details such as email, password and names when a user registers. The tracker table stores data for which days of the week the user will be in the office. The primary key for the database is the user id and the two tables are related to each other through this.

##### tasks.py:
This file contains a single task for the scheduler to run. This task is set to run every Monday at 00:00 hours. What it does is transfer all the 'next week' data to 'this week' and sets all the next weeks data to none so users do not have to automatically reset the days they are in office. 

##### views.py:
This file contains the routes which the user will see on the frontend. The home route takes in data from forms on the homepage and stores it in the tracker table in the database. There is also some variables and a function which use the datetime package to pass through current dates to the frontend. The profile route simply returns the profile page. The edit-profile route takes in data from forms on the profile page and updates the user table in the database. The deletion route finds the user in the database, logs the user out, then deletes their data in both tables.

##### templates: