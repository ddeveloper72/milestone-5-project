# Milestone 5 Project

## [Custom Drone Systems](https://ddeveloper72-custom-drone.herokuapp.com/)

* for customizing your drone's navigation systems *


[![Build Status](https://travis-ci.org/ddeveloper72/milestone-5-project.svg?branch=master)](https://travis-ci.org/ddeveloper72/milestone-5-project)

## Preface

Custom Drone deBug is a fictitious organization that specialize in developing high-tech drone navigation systems.  The navigation systems of our imaginary drones can be programmed and customized to suit our customer's needs.  The drones are used for a variety different industry purposes, such as search and rescue and inspection.  

Customers of Custom Drone, use standard PC based systems to network to their drones by different means.  They are able to communicate by Satellite, 4G, and low frequency radio.  The various Drone models may be tasked to work in a variety of different environments, such as above ground, below ground in cave/tunnel systems and in aquatic environments.  Custom Drone navigation systems facilitate swarm management, establishing satellite peer to per communication in difficult communications environments.

This service provides a facility were customers can report a problem with a drone navigation system.  Problems or bugs can be logged through the Custom Drone deBug portal.  Bugs that have been found in the software will be fixed free of charge and rolled out to all users of that make and model of product.  Our site has a familiar blog look and feel.  Customers that have logged an issue, will be able to upvote a bug report made by another customer in a blog environment.  If there are many upvotes for a particular bug, these are monitored by the product development team will use this data to do as a risk assessment and reassign development time to resolving the bug. Bug resolution is prioritized by the number of votes a bug gets.

Our drone navigation systems are also customizable.  If a new feature is suggested by a customer, the feature can be logged as a Feature Request.  Our product development team will do their best to build this new feature.  There are three categories of software that we work on, namely 'auto-pilot', 'navigation' and 'flight controls'.  Each category will need a specific number of hours for development.  Our costs for assessment, feasibility study, development and testing of the software feature are all inclusive and are reflected in our time required.

## 1. Project Goals

In this project is about utilizing different coding skills to create a usable end product.  In this case, this project is a usable framework, how ever there are many aspects of it that I would like to develop further.

The project uses a django framework, which is the last module of the full-stack framework that was taught.  In it we learned to build as well as import pre-built apps from other projects.  This is what Django lets you do, so that development of a product can be turned around quickly in an ideal development environment.  I've had difficulty with this, so have had to foo some of the nice to aspect so of the development to keep inline with the project brief.

The unfinished work I have down for future is:

  1. Deployment of Slug in my URL patterns (the model framework is in place)
  2. Enabling and using reported and hidden Booleans for blog comments (in the model) - I've used approve or delete for now.
  3. Refining my media queries for transitioning from small to large screen.
  4. Deploying charts for rendering the statistics collected using a product like chart.js
  5. Improving the UX experience with JQuery and more attractive front end imagery.

I believe that the project fulfils the essentials required to meet the brief.  It utilizes multiple apps that use different online services, that come together to form a finished product.  These are outlined in the UX Design below.  This app manages all SQL database CRUD operations well and provides a seamless transition between my local development MySQL database and the Postgresql hosted by AWS through Heroku.  

The app makes use of the Amazon Web Services S3 bucket to host both my dynamic and static files, as well as integrates with Stripe for managing the apps checkout features.  The authentication app is also tied into a Gmail account so that we can facilitate doing a password reset for a user.

I hope that anyone using this app will enjoy using it.  Its is a starter app and has the potential to change and develop.

## 2. The UX Design

### Strategy

| Focus                                                       | User Needs                                                            | Business Objectives                             |
|-------------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------|
| What are you aiming to achieve?                             | Report a bug/issue, prolonging their use of the product.  | To gather user feedback for continues product improvement. To engage with the customer that will maintain and grow our customer base.|
|                                                             |   | Track the bugs being dealt with, from a status indicator. |
|                                                             |   | Track the features being dealt with, from a status indicator |
|                                                             |   | See when a task is marked complete |
|                                                             | To be able to see if other users have similar experiences.  | Gather statistics from likes from user feedback for product development and marketing. |
|                                                             | Provide a familiar Blog medium for reading about service updates and end-user feedback. | To provide customers with a facility to input their feedback on our products. |
| For whom?                                                   | Organizations can learn about "Custom Drone" systems.  |  |
| TARGET AUDIENCE                                             | Drone Techs, drone Pilots, Drone research and development audiences.  | To learn and understand the technical needs of the customer, by providing a facility where customers can write feedback in a familiar blog style interface |
|                                                             | Company purchasing authority |  |
|                                                             | Customer development authority | Collaborate on needs so we can develop of turnkey features |

### Scope

| Focus                                                       | Functional Specification                                              | Content Requirements                            |
|-------------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------|
| Which features?                                             | User Account  | An app for registering a new user, that facilitates login and log-out |
| What’s on the table?                                        | The Blog App  | A medium where the staff of custom drone can publish information about the service. |
|                                                             | A Issues App | The core of Custom Drone, which lets users submit bugs as well as features for development. |
|                                                             |   | Provide a facility for a user to suggest a new feature upgrade and then pay for the feature once development is complete. |
|                                                             |   | To provide a facility where other users can comment on a blog entry by another user. |
|                                                             |   | Provide a likes button for a blog entry so that another user can up-vote a feature or a bug |
|                                                             |   | Provide a admin statistics dashboard that will present the number of bugs/issues being resolved. |
|                                                             | A Crat App  | A place where users can see all the features and cost of the features that they have selected. |
|                                                             |  Checkout App | A payment app that integrated Stripe for managing the financial transaction |
|                                                             |   | A place where user information can be recorded for payment and shipping of the purchased products. |
|                                                             |  A Profile App | For recording the user bio which is for future development. |

### Structure

| Focus                                                       | Interaction Design                                                     | Information Architecture                       |
|-------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------|
| How is the information structured?                          | Where am I? / How did I get here? / What can I do here? / Where can I go?  | Organizational / Navigational schemas (tree / nested list / hub and spoke / dashboard) |
|                                                             | An index/landing page.  | Tree Structure |
|                                                             | User registration pages for loin, register |  |
|                                                             | Password reset pages, for emailing a password reset link |  |
| How is it logically grouped?                                | A user profile page. Their profile name and email address will need to be unique, different from all the other profiles. An email address is required for doing a password reset.  | Start/home page |
|                                                             | Blog delete page  |  |
|                                                             | Blog Comment approve/delete |  |
|                                                             | Issue delete |  |
|                                                             | Issue Comment approve/delete |  |
|                                                             | Issue status update from 'To do', 'In Progress' & 'Complete' |  |

### Skeleton

| Focus                                                       | Interface Design                                       | Navigational Design  | Information Design  |
|-------------------------------------------------------------|--------------------------------------------------------|----------------------|---------------------|
| How will the information be represented?                    | See wireframes |  | Title and informational typescripts |
| How will the user navigate to the information and features? | See wireframes | Links from the navbar |  |
|                                                             |  | Selecting add feature to  |  |

### Surface

| Focus                                                       | Visual Design                       |
|-------------------------------------------------------------|-------------------------------------|
| What will the finished product look like?                   |  |
|                                                             |  |
| What colours, typography and design elements will be used?  |  |

### Wireframes

![1-Login](https://github.com/ddeveloper72/milestone-5-project/blob/master/static/readme/1-Login.png "Login mockups")

Figure of the login design.

![2-Register](https://github.com/ddeveloper72/milestone-5-project/blob/master/static/readme/2-Register.png "Registration form mockups")

Figure of the registration form design.

![3-Index](https://github.com/ddeveloper72/milestone-5-project/blob/master/static/readme/3-Index_Page.png "Index page mockups")

Figure of the index page proposal.

![4-User_Profile](https://github.com/ddeveloper72/milestone-5-project/blob/master/static/readme/4-User_Profile.png "User Profile page")

Figure of the index page proposal.

![5-Blog_Admin_Staff](https://github.com/ddeveloper72/milestone-5-project/blob/master/static/readme/5-Blog_Admin_Staff.png "Blog page for Admin-Staff page")

Figure of the blog page as seen by the Admin of Staff.

![6-Blog_Admin_Staff](https://github.com/ddeveloper72/milestone-5-project/blob/master/static/readme/6-Blog_Admin_Staff.png "Blog form for Admin-Staff")

Figure of the blog form as seen by the Admin of Staff.



![8-Bug_by_User](https://github.com/ddeveloper72/milestone-5-project/blob/master/static/readme/8-Bug_by_User.png "Bug view by Admin-Staff")

Figure of the bug view as seen by the Admin of Staff.


## 3. Application Construction

1. Tools used

   * Written in VSCode
   * Python 3.7.2
   * jQuery
   * CSS and JavaScript files were created and stored locally within the application as static files.  These static files were then added to the s3 bucket on Amazon
   * The SQL database was created with heroku-postgresql (see database included with repository) and is hosted at amazonaws.com
   * The app as tested using Chrome dev tools & VSCode debugger
   * HTML and CSS checked with help from the W3 Validation Service
   * [Darkly](https://bootswatch.com/darkly/) Bootswatch theme. 
   * Version management and test branches created in git
   * Web deployment is hosted on Heroku

   

2. Reference Literature

   * [django Framework Documentation](https://www.djangoproject.com/)
   * [PostgreSQL](https://www.postgresql.org/)
   * [django-bootstrap4](https://readthedocs.org/projects/django-bootstrap4/)
   * [Django Girls Tutorial: Extensions](https://tutorial-extensions.djangogirls.org/en/)
   * [Amazon AWS](https://aws.amazon.com/)
   * [Deploying with Git \| Heroku Dev Centre](https://devcenter.heroku.com/articles/git)
   * [How to Extend Django User Model](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#abstractuser)
   * [How to count All Objects of a Database Table in Django](http://www.learningaboutelectronics.com/Articles/How-to-count-all-objects-of-a-database-table-in-Django.php)
   * [Stack Overflow](http://stackoverflow.com)

3. Code Development
   
   ### Running Locally in VSCode

    1. Download and install Python 3.7.2 and install in your windows environment if you haven't already installed the latest version of python.
    2. Create a project environment for Django, by creating a virtual environment. 
       1. Run `python -m venv env`
    3. In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Select Interpreter command.
    4. Select the virtual environment python interpreter for your project.
    5. Start the virtual environment from the terminal by typing in:
       1. `env\scripts\activate`
    6. To setup the project files in this new virtual environment, type in:
       1. `pip install -r requirements.txt`
    7. Create a proc file
       1. `echo web: gunicorn django_debug.wsgi:application > Procfile`
  
    You wil need to setup the environmental variabes in VSCode for production and debug versions of the project.

    Cteate a new project workspace file and add the following infomation into it for running the project in developer mode:

    VSCode Project.cose-workspace

    ```javascript
    {
    "terminal.integrated.env.windows":
                {
                    "DEVELOPMENT": "",
                    "SECRET_KEY": "<my_secret_key>",
                    "ADMIN": "admin_pass",
                    "DJANGO_SETTINGS_MODULE": "drone_debug.settings",
                    "STRIPE_PUBLISHABLE": "<my_stripe_publishable_key>",
                    "STRIPE_SECRET": "<my_stripe_secret_key>",
                    "AWS_ACCESS_KEY_ID": "<my_aws_access_key>",
                    "AWS_SECRET_ACCESS_KEY": "<my_aws_secret_access_key>",
                    "EMAIL_ADDRESS": "<my_email_address>",
                    "EMAIL_PASSWORD": "<my_email_password>",
                    "USER": "<MySQL_db_user_name>",
                    "HOST": "<MySQL_locsl_address eg. 127.0.0.1>",
                    "PORT": "<MySQL_locsl_port eg. 3306>"
                },
    }

    ```

    Then in the .vscode folder, locate the settings.json file and add the following infomation into it:

    SCode settings.js

    ```javascript
    {
    "terminal.integrated.env.windows":
                {
                    "DEVELOPMENT": "",
                    "SECRET_KEY": "<my_secret_key>",
                    "DATABASE_URL": "<my_postgres_db_url>",
                    "ADMIN": "admin_pass",
                    "DJANGO_SETTINGS_MODULE": "drone_debug.settings",
                    "STRIPE_PUBLISHABLE": "<my_stripe_publishable_key>",
                    "STRIPE_SECRET": "<my_stripe_secret_key>",
                    "AWS_ACCESS_KEY_ID": "<my_aws_access_key>",
                    "AWS_SECRET_ACCESS_KEY": "<my_aws_secret_access_key>",
                    "EMAIL_ADDRESS": "<my_email_address>",
                    "EMAIL_PASSWORD": "<my_email_password>"
                },
    }

    ```
    Update the gitignore file to to exclude the following file types:
    Use the following command line command:
    * `echo env.py >> .gitignore`

   1.  env
   2.  .vscode
   3.  config.py
   4.  '__pycache__'
   5.  *.sqlite3
   6.  media/
   7.  .coverage
   8.  *.code-workspace
   9.  *.pyc
   10. *.db
   11. *.mwb
   12. *.mwb.bak
   13. *.mwb.beforefix

4.  Production Deployment Instructions

    1. Instructions for deployment to a hosing site: [Heroku](https://www.heroku.com/)

    In Heroku - Part 1

    1. Log into Heroku
    2. Select New and Create new App.
    3. Create a App name, select the region.
   
        * then Create app.
  
    4. Select Resources tab, search for add-on
   
        * Add Heroku Postgres SQL database, choosing the free hobby plan.
  
    5. Select the Settings tab, then select Reveal Config Vars
   
        * Verify the new `DATABASE_URL` and value is there for the Postgres database.
        * Add in the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to the heroku Config Vars to enable connection to the AWS S3 bucket
        * Add in the `STRIPE_PUBLISHABLE` and `STRIPE_SECRET` keys to the heroku Config Vars to enable connection to Sripe.
        * Add in the `EMAIL_HOST_USER` and the `EMAIL_HOST_PASSWORD` details to the heroku Config Vars for the email password reset system.
        * Copy and paste the key, value, pairs into the workspace settings, but not the Postgres database URL in VSCode used for environmental settings (see above).
        * Add a new `SECRET_KEY` key, value pair from your VSCode environmental settings to the heroku Config Vars.
        * Our static files are not hosted on Heroku, so set DISABLE_COLLECTSTATIC to 1 in the Config Vars.
  
    6. Copy these config Vars from the .vscode/settings.json file and this time include the Postgres URL data.
    7. Don't forget to update the allowed hosts for Heroku in your Django settings file.
    8. Lastly, becasse our code is deployed to GitHub, select the deploy tab in Heroku and connect the app to the GitHub repository.  Then select automatic deploment from the _master_ branch.  This way deployments from VSCode to the master branch, will be automatically pulled by Heroku.

    ```Python

    ALLOWED_HOSTS = [
    os.environ.get('localhost', '127.0.0.1'),
    'ddeveloper72-custom-drone.herokuapp.com'
    ]

    ```

    In VSCode - Part 2


    1. To stat the project using MySQL, load the project as a project workspace.
    or...
    1. To open it using the Postgres production database, right click the project folder in windows and open with VSCode.

    2. In the command line, start the virtual environment for the project.
    3. For deploying our models to the production database (we have already made our development models in MySQL), test connection to the new Postgres database by noting the instructions from the command line.

        * Connecting to the local MySQL database should not occur.
        * There will be an instruction to `run python manage.py migrate`,
        * Then run `run python manage.py makemigrations`
        * Then run `run python manage.py migrate` again.
        * run migrate to create new models on the Postgres database.  The existing migrations will be used.
        * A new superuser will be required for the new Postgres database, run `python manage.py creatsuperuser` and fill in the required superuser details to create  super user.
        * Run the app, `python manage.py runserver` and login as the administrator.  All your db models should be clean and empty.
  
    4. 

## 4. MySQL / PostgreSQL Database Schema (using MySQL Workbench)

The EER drawing for the project has been divided into two sections, namely the Blog models EER and the Issues models EER.

![Blog EER diagram](https://github.com/ddeveloper72/milestone-5-project/blob/master/static/readme/blog_eer.png "Blog model EER schema")

Figure of the Blog EER diagram.

![Issues EER diagram](https://github.com/ddeveloper72/milestone-5-project/blob/master/static/readme/issues_eer.png "Issues model EER schema")

Figure of the Issues EER diagram.

## 5. Development & Testing

### Debugging Strategy

    I thought that the best way to test this application as I have done in the past, was to run a beta test by putting the application on Heroku and then letting everyone in my college try it. While doing so, I asked for feedback on the application. This is the feedback I got:
    
   ### *Issues Found*

1. The blog page is conciderd to to be the main front end of the site and wasan't publically accessible.
2. The main user registration page wasn't showing error messages.  Once the user had registed, the errors remaind queued on their profile page.
3. I had trouble counting stats data accumulating in the issues model for the different categories of bugs and features.
4. I had trouble trying to assign a inteerger value for hours required to do a particular taks.  There were three different task types and so need 3 different ammounts of time assigned to each one.  I was unable to to use a list then refence a time in the model.
5. Collegues have come back to me wth problems that they ahve noticed with the media queries for transitioning between mobile viw, table and larger sccreens.
6. The shopping cart is meant to bable to align all the items in the cart horizontally, to where it meed the user asside on the right.  This stopped working after all refactored all the injected partials. Instead the shopping cart items line up below each other like to blog cards.
7. I have implemented a 3rd party add-in for using Markdown with the blog entries.  I've notiched how ever that if use `{{ post.get_content_as_markdown|truncatewords:30 }}`, the Markdwon text will be sliced if any partial tags are left, they disrupt my html framework.


   ### *The Fixes Implemented*

1. Moved a copu of the blog URL to the public side of the login.  I then removed login required form the `get_posts` view.  I then tested the links on the page to insure the from the insecure/public side of the site, that the user is diverted to the login page.
2. Mesagin was added to the registration page and the login page. Messaging wasn't working due to an error with the messaging block tags.
3. I used a django filter find function to find the Boolean values and then used a either count in the html framework, as well as in places, kept the count in the view function.
4. To assign a unit of time to a particular type of work, changed the view functions that log a new feature as well as edit and existing bug/feature.  When the user selected a type of task that was a feature, such as 'Navigation', an enf elif cunction now evaluated the genre, and if it matches the genre chosen; then that genre = hours_required.  The hours_required was then saved to the table along with all the other information needed to log the issue.
5. I am still working on debuggin the media queries.
6. I need to implement a change to the cart framework to make the changes.
7. I haven't found a way yet to safey truncate the Markdown text.  For the purpose of this excercise, I have had to remove truncate words till a solution can be found.



## 6. Credits


### by Duncan Falconer for the Code Institute, 2019
