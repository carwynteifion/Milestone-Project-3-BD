# Isadora's Kitchen
Link to the live project here: https://milestone-project-3-bd.herokuapp.com/

This is a website for Isadora's Kitchen, designed as a responsive site for people to create, read, update and delete their own cooking recipes, as well as view those created by other users.

<h2 align="center"><img src="assets/img/responsive.png"></h2> - REMEMBER TO ADD THIS

# Table of Contents
1. [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
  - [Wireframes](#wireframes)

2. [Features](#features)

3. [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)

4. [Testing](testing)
  - [HTML and CSS Validation](#html-and-css-validation)
  - [Testing User Stories from UX Section](#testing-user-stories-from-ux-section)
  - [Further Testing](#further-testing)
  - [Known Bugs](#known-bugs)
  - [Fixed Bugs](#fixed-bugs)

5. [Deployment](#deployment)
  - [GitHub Pages](#github-pages)
  - [Forking the GitHub Repository](#forking-the-github-repository)
  - [Making a Local Clone](#making-a-local-clone)

6. [Credits](#credits)
  - [Code](#code)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)


## User Experience
- User stories
  - First Time Visitor Goals
    
    a. As a first time visitor, I want to understand the site's purpose so I can determine if it is relevant to what I need.

  - Returning Visitor Goals

  - Frequent Visitor Goals

- Design
  - Colour Scheme
  - Typography
  - Imagery

- Wireframes - can be viewed here - WIREFRAME LINK

## Features
- Responsive on mobile, tablet and desktop sizes
- Interactive elements
- CRUD functionality

[Back to top](#isadora's-kitchen)

## Technologies Used
### Languages Used
- HTML5
- CSS3
- JavaScript
- Python 3

### Frameworks, Libraries and Programs used
1. [Materialize](https://materializecss.com/) - used as the visual framework for this project.
2. [Balsamiq Wireframes](https://balsamiq.com/wireframes/) - used in the design process to draw the site's wireframes.
3. [Flask](https://flask.palletsprojects.com/) - used to build the web pages for this project as templates.
4. [Font Awesome](https://fontawesome.com/) - used to add icons on each page of the site to improve UX.
5. [Git](https://gitpod.io/) - used for version control via Gitpod. The terminal was used to commit and push code to GitHub.
6. [GitHub](https://www.github.com/) - used to store the project's pushed code from Git.
7. [Werkzeug](https://werkzeug.palletsprojects.com/) - used for password hashing, installed as a Flask dependency.
8. [Jinja](https://jinja.palletsprojects.com/) - a HTTP templating language for Python.
9. [jQuery](https://jquery.com/) - used to enable Materialize dynamic effects such as the navbar.
10. [Heroku](https://dashboard.heroku.com/) - hosts the deployed project.
11. [PyMongo](https://pymongo.readthedocs.io/) - Python distribution containing tools for working with MongoDB.
12. [MongoDB Atlas](https://www.mongodb.com/) - used to host the project's NoSQL databases.

[Back to top](#isadora's-kitchen)

## Testing

### Code Validation
The W3C Markup and CSS Validators, JSHint JavaScript Validator and PEP8 Validator were used to validate the code to ensure the project was free from errors.

- [W3C Markup Validator Results]()
- [W3C CSS Validator Results]()
- [JSHint Validator Results]()
- [PEP8 Compliance Results]()

### Testing User Stories from UX Section

  - First Time Visitor Goals
    
    - a. As a first time visitor, I want to understand the site's purpose so I can determine if it is relevant to what I need.

  - Returning Visitor Goals

  - Frequent Visitor Goals

### Further Testing
The site has been tested on Chrome, Edge, Firefox and DuckDuckGo on mobile, desktop and tablet devices of varying screen widths.

Pages all link to each other without issue, and external links open a new tab as expected.

Family also assisted in testing the site, and reported no major issues.

### Known Bugs

### Fixed Bugs

[Back to top](#isadora's-kitchen)

## Deployment

### Local Deployment

Before you are able to deploy and run this application locally, you must have the following installed on your system:

- [Python3](https://www.python.org/downloads) to run the application.
- [PIP](https://pip.pypa.io/en/stable/installing) to install all app requirements.
- An IDE of your choice, such as [Microsoft Visual Studio Code](https://code.visualstudio.com).
- [GIT](https://www.atlassian.com/git/tutorials/install-git) for cloning and version control.
- [MongoDB CLI](https://www.mongodb.com) to develop your own database either locally or remotely on MongoDB Atlas.

Next, perform the following steps:

Clone this GitHub repository by either clicking the green *Clone or download* button and downloading the project as a zip-file (remember to unzip it first), or by entering the following into the Git CLI terminal:
    - `git clone https://github.com/carwynteifion/Milestone-Project-3-BD.git`.
- Navigate to the correct file location after unpacking the files.
    - `cd <path to folder>`
- Create a `env.py` file containing your *MONGO_URI* and *SECRET_KEY* environmental variables.
- Install all requirements from the [requirements.txt](https://github.com/carwynteifion/Milestone-Project-3-BD/blob/main/requirements.txt) file using this command:
    - `pip3 -r requirements.txt`
- Sign up for a free account on [MongoDB](https://www.mongodb.com) and create a new Database called **milestone_project_3**. The *Collections* in that database should be as follows:

```
DATABASE DETAILS HERE
```

- At the terminal prompt, type ```python3 app.py```. This should now start running a development server which you can open from your IDE's remote explorer.

### Remote Deployment

To implement this project on Heroku, the following must be completed:

1. Create a **requirements.txt** file so Heroku can install the required dependencies to run the app.
    - `pip3 freeze --local > requirements.txt`
    - My file can be found [here](https://github.com/carwynteifion/Milestone-Project-3-BD/blob/main/requirements.txt).
2. Create a **Procfile** to tell Heroku what type of application is being deployed, and how to run it.
    - `echo web: python run.py > Procfile`
    - My file can be found [here](https://github.com/carwynteifion/Milestone-Project-3-BD/blob/main/Procfile).
3. Sign up for or log into your Heroku account, create your project app, and click the **Deploy** tab. Select *Connect GitHub* as the Deployment Method, and select *Enable Automatic Deployment*.
4. In the Heroku **Settings** tab, click on the *Reveal Config Vars* button to configure environmental variables as follows:
    - **IP** : `0.0.0.0`
    - **PORT** : `8080`
    - **MONGO_URI** : `<link to your Mongo DB>`
    - **SECRET_KEY** : `<your own secret key>`
5. The app will now be deployed and built by Heroku and will be ready to run.

[Back to top](#isadora's-kitchen)

## Credits

### Code

### Content

All code was written by the developer.

### Media

[Background image](https://www.teahub.io/down/JJmTow_spice-indian-spices-hd/)
Food images taken from [BBC Good Food](https://www.bbcgoodfood.com)
[Default food image](https://www.hiclipart.com/free-transparent-background-png-clipart-mhidw/download)

### Acknowledgements

My mentor, Chris, for once again being a huge help while I was putting this together.

My fiancee, Isadora, and her mum, Kay, for UX/bug testing this site.

[Back to top](#isadora's-kitchen)