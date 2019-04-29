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

## 3. Application Construction

1. Tools used

   * Written in VSCode
   * The SQL database was created with heroku-postgresql (see database included with repository) and is hosted at amazonaws.com
   * CSS and JavaScript files were created and stored locally within the application as static files.  These static files were then added to the s3 bucket on Amazon
   * The app as tested using Chrome dev tools & VSCode debugger
   * HTML and CSS checked with help from the W3 Validation Service
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

3. Code Development
   
   ### Running Locally in VSCode

   * Download and install Python 3.7.2 and install in your windows environment if you haven't already installed the latest version of python.
   * Create a project environment for Django, by creating a virtual environment. Rin `python -m venv env`
   * In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Select Interpreter command.
   * Select the virtual environment python interpreter for your project.
   * Start the virtual environment from the terminal by typing in `env\scripts\activate` then press enter.
   * To setup the project files in this new virtual environment, type in `pip install -r requirements.txt` and press enter.
  
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

   1.  env
   2.  .vscode
   3.  config.py
   4.  __pycache__
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
        - then Create app.
    4. Select Resources tab, search for add-on
        - Add Heroku Postgres SQL database, choosing the free hobby plan.
    5. Select the Settings tab, then select Reveal Config Vars
        - Verify the new `DATABASE_URL` and value is there for the Postgres database.
        - Add in the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to the heroku Config Vars to enable connection to the AWS S3 bucket
        - Add in the `STRIPE_PUBLISHABLE` and `STRIPE_SECRET` keys to the heroku Config Vars to enable connection to Sripe.
        - Add in the `EMAIL_HOST_USER` and the `EMAIL_HOST_PASSWORD` details to the heroku Config Vars for the email password reset system.
        - Copy and paste the key, value, pairs into the workspace settings, but not the Postgres database URL in VSCode used for environmental settings (see above).
        - Add a new `SECRET_KEY` key, value pair from your VSCode environmental settings to the heroku Config Vars.
    6. Copy these config Vars from the .vscode/settings.json file and this time include the Postgres URL data.


    In VSCode - Part 2


    1. To stat the project using MySQL, load the project as a project workspace.
    or...
    1. To open it using the Postgres production database, right click the project folder in windows and open with VSCode.
    
    2. In the command line, start the virtual environment for the project.
    3. For deploying our models to the production database (we have already made our development models in MySQL), test connection to the new Postgres database by noting the instructions from the command line.
        - Connecting to the local MySQL database should not occur.
        - There will be an instruction to run python manage.py migrate
        - run migrate to create new models on the Postgres database.  The existing migrations will be used.
        - A new superuser will be required for the new Postgres database, run python manage.py creatsuperuser and fill in the required superuser details.
        - Run the app, python manage.py runserver and login as the administrator.  All your db models should be clean and empty.

## 4. MySQL / PostgreSQL Database Schema

The EER drawing for the project has been divided into two sections, namely the Blog models EER and the Issues models EER.

![Blog EER diagram](https://github.com/ddeveloper72/milestone-5-project/blob/master/static/readme/blog_eer.png "Blog model EER schema")

Figure of the Blog EER diagram.

![Issues EER diagram](https://github.com/ddeveloper72/milestone-5-project/blob/master/static/readme/issues_eer.png "Issues model EER schema")

## 5. Development & Testing

### Debugging Strategy

### _The issues found_

### _The fixes implemented_

## 6. Credits

### by Duncan Falconer for the Code Institute, 2019
