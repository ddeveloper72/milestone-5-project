# Milestone 5 Project

## Custom Drone deBug

![Index](https://github.com/ddeveloper72/milestone-5-project/blob/master/static/readme/landing_page.png "Django Landing Page")

## 1. Project Goals

Custom Drone deBug is a fictitious organization that specialize in developing high-tech drone navigation systems.  The navigation systems of our imaginary drones can be programmed and customized to suit our customer's needs.  The drones are used for a variety different industry purposes, such as search and rescue and inspection.  

Customers of Custom Drone, use standard PC based systems to network to their drones by different means.  They are able to communicate by Satellite, 4G, and low frequency radio.  The various Drone models may be tasked to work in a variety of different environments, such as above ground, below ground in cave/tunnel systems and in aquatic environments.  Custom Drone navigation systems facilitate swarm management, establishing satellite peer to per communication in difficult communications environments.

This service provides a facility were customers can report a problem with a drone navigation system.  Problems or bugs can be logged through the Custom Drone deBug portal.  Bugs that have been found in the software will be fixed free of charge and rolled out to all users of that make and model of the affected products as an opt-in upgrade.

Our drone navigation systems are also customizable.  If a new feature is suggested by a customer, the feature can be logged as a New Feature Request.  Our product development team will do their best to build this new feature into the next product model, so making it available to everyone buying that model.  

If however the new feature is required immediately, our development team will be very happy to focus on developing the New Product Feature.  New product upgrades are considered to be on demand will be charged  development fee dependant on the amount of time required to process the upgrade.  The development fee covers a Coding Feasibility Assessment, Coding Development, System Testing and Simulation, Quality Assessment and finally Product dispatch.

Customers will be able to upvote a bug report made by another customer, should they have the same issue. If there are many upvotes for a particular bug, the product development team will use this statistical data to do as a risk assessment and reassign development time to resolving the bug.

## 2. The UX Design
*(This template is with thanks from 
@sarahloh)*

#### Strategy

| Focus                                                       | User Needs                                                            | Business Objectives                             |
|-------------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------|
| What are you aiming to achieve?                             |   |  |
|                                                             |   |  |
|                                                             |   |  |
| For whom?                                                   |   |  |
| TARGET AUDIENCE                                             |   |  |
|                                                             |   |  |
|                                                             |   |  |
|                                                             |   |  |
|                                                             |   |  |
|                                                             |   |  |

#### Scope

| Focus                                                       | Functional Specification                                              | Content Requirements                            |
|-------------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------|
| Which features?                                             |   |  |
| What’s on the table?                                        |   |  |
|                                                             |   |  |
|                                                             |   |  |
|                                                             |   |  |
|                                                             |   |  |
|                                                             |   |  |
|                                                             |   |  |
|                                                             |   |  |
|                                                             |   |  |
|                                                             |   |  |
|                                                             |   |  |

#### Structure

| Focus                                                       | Interaction Design                                                     | Information Architecture                       |
|-------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------|
| How is the information structured?                          |   |  |
|                                                             |   |  |
| How is it logically grouped?                                |   |  |
|                                                             |   |  |
|                                                             |   |  |
|                                                             |   |  |
|                                                             |   |  |

#### Skeleton

| Focus                                                       | Interface Design                                       | Navigational Design  | Information Design  |
|-------------------------------------------------------------|--------------------------------------------------------|----------------------|---------------------|
| How will the information be represented?                    |  |  |  |
| How will the user navigate to the information and features? |  |  |  |
|                                                             |  |  |  |
|                                                             |  |  |  |
|                                                             |  |  |  |
|                                                             |  |  |  |
|                                                             |  |  |  |

#### Surface

| Focus                                                       | Visual Design                       |
|-------------------------------------------------------------|-------------------------------------|
| What will the finished product look like?                   |  |
|                                                             |  |
| What colours, typography and design elements will be used?  |  |

##### Wireframes

#### 3. Application Construction

1. Tools used

   * Written in VSCode
   * The SQL database was created with heroku-postgresql (see database included with repository) and is hosted at amazonaws.com
   * CSS files were created and stored locally within the application as static files.  These static files were then added to the s3 bucket on Amazon
   * The app as tested using Chrome dev tools & VSCode debugger
   * HTML and CSS checked with help from the Mark-up Validation Service
   * Version management and test branches created in git
   * Web deployment is hosted on Heroku

2. Reference Literature

   * [django Framework Documentation](https://www.djangoproject.com/)
   * [PostgreSQL](https://www.postgresql.org/)
   * [django-bootstrap4](https://readthedocs.org/projects/django-bootstrap4/)
   * [Amazon AWS](https://aws.amazon.com/)
   * [Deploying with Git \| Heroku Dev Centre](https://devcenter.heroku.com/articles/git)

3. Code Development
4. Deployment Instructions

#### 4. SQLite3 / PostgreSQL Database Schema

#### 5. Development & Testing

### Debugging Strategy

### _The issues found_

### _The fixes implemented_

#### 6. Credits

### by Duncan Falconer for the Code Institute, 2019

[![Build Status](https://travis-ci.org/ddeveloper72/milestone-5-project.svg?branch=master)](https://travis-ci.org/ddeveloper72/milestone-5-project)