# Isadora's Kitchen
Link to the live project here: https://milestone-project-3-bd.herokuapp.com/

This is a website for Isadora's Kitchen, designed as a responsive site for people to create, read, update and delete their own cooking recipes, as well as view those created by other users. I conceived this site as my fiancee loves to cook and wanted somewhere to share her recipes, and have other users share theirs too.

<h2 align="center"><img src="static/img/responsive.PNG"></h2>

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
    
    b. As a first time visitor, I want to create an account so I can share recipes to the site.

    c. As a first time visitor, I want to explore other recipes.

  - Returning Visitor Goals

    a. As a returning visitor, I want to be able to log in quickly and easily.

    b. As a returning visitor, I want to edit my existing recipes.

    c. As a returning visitor, I want to delete a recipe I have previously added to the site.

  - Frequent Visitor Goals

    a. As a frequent visitor, I want to view all the recipes I have uploaded.

- Design
  - Colour Scheme
    - The colour scheme is yellow for the header and footer with white text, with dark blue text for titles and form labels. Buttons are green for confirming adding or editing a recipe, red for cancelling or deleting and yellow for the edit button on a recipe's View page. The bright colours are meant to evoke the brightly coloured spices used in Indian cooking, mainly turmeric which is yellow.
  - Typography
    - The font throughout is the standard Materialize font, Segoe UI, which is presentable and clear.
  - Imagery
    - The background image is of various spices, tying in with the food theme. In the same vein, the default image if an image is not uploaded for a new recipe entry is of a food icon.

- [Wireframes can be viewed here](https://github.com/carwynteifion/Milestone-Project-3-BD/tree/main/static/img/wireframes)

## Features
- Responsive on mobile, tablet and desktop sizes
- Interactive elements
- CRUD functionality
- Tailored view of user's own recipes
- Registration/Login functionality

If I had more time, I would have liked to have added the following:
- A favourites function so users could favourite their recipes for easy access
- The ability to delete an account and optionally its associated recipes
- The ability for a user to change their password when logged in
- More defensive programming overall, to prevent accidental deleting of recipes etc.
- Pagination, to better organise recipe entries on the home page.

[Back to top](#isadoras-kitchen)

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

[Back to top](#isadoras-kitchen)

## Testing

### Code Validation
The W3C Markup and CSS Validators, JSHint JavaScript Validator and PEP8 Validator were used to validate the code to ensure the project was free from errors.

- [W3C Markup Validator](https://validator.w3.org/) Results - No errors. One warning regarding no headings within sections appearing on all pages. This is likely an issue with Jinja templating.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) Results - No issues.
- [JSHint Validator](https://jshint.com/) Results - No issues.
- [PEP8 Compliance](https://pep8online.com/checkresult) - No issues.

### Testing User Stories from UX Section

  - First Time Visitor Goals
    
    a. As a first time visitor, I want to understand the site's purpose so I can determine if it is relevant to what I need.
      
      - i. The site's home page invites users to search for a recipe or browse the page. The user can click on a recipe's View Recipe link to view more of its details.
      
      - ii. The navbar clearly shows the site's name, identifying it as being based around making food.
      <h2 align="center"><img src="static/img/screenshot1.PNG"></h2>
    
    b. As a first time visitor, I want to create an account so I can share recipes to the site.

      - i. When not logged in, the navbar has a registration button that the user can click to create an account.
      
      - ii. Registration is quick and easy, only requiring a username and password within the provided limitations to sign up.
      <h2 align="center"><img src="static/img/screenshot2.PNG"></h2>

      - iii. Users can start adding recipes as soon as they have signed up using the Add New Recipe option which appears in the navbar when logged in.
      <h2 align="center"><img src="static/img/screenshot3.PNG"></h2>

      - iv. On the Add Recipe page, users can fill in the information about the recipe, and add an image URL if they want. If they do not add one, a default image is used instead.
      <h2 align="center"><img src="static/img/screenshot4.PNG"></h2>

      - v. When finished, the user can log out using the Log Out button on the navbar.

    c. As a first time visitor, I want to explore other recipes.

      - i. Scrolling down the home page will show more recipes to the user. Clicking on each of their View Recipe options will show each recipe in further detail.
      <h2 align="center"><img src="static/img/screenshot5.PNG"></h2>

      - ii. Users can also search for recipes using the search bar on the home page.

  - Returning Visitor Goals

    a. As a returning visitor, I want to be able to log in quickly and easily.

      - i. When not logged in, the navbar displays a login button. This takes the user to a form page where they enter their username and password to log in.
      <h2 align="center"><img src="static/img/screenshot6.PNG"></h2>

    b. As a returning visitor, I want to edit my existing recipes.

      - i. When logged in, users can click on the Edit Recipe button which appears at the bottom of any recipe's View page. If the logged in user is also the creator of the recipe, the site will allow them to edit the entry.
      <h2 align="center"><img src="static/img/screenshot7.PNG"></h2>

      - ii. The user will be presented with a pre-populated form where they can edit all the data they have entered previously, and resubmit or cancel at the bottom of the form.
      <h2 align="center"><img src="static/img/screenshot8.PNG"></h2>

    c. As a returning visitor, I want to delete a recipe I have previously added to the site.

      - i. When logged in, users can click on the Delete Recipe button which appears at the bottom of any recipe's View page. If the logged in user is also the creator of the recipe, the site will allow them to delete the entry.

  - Frequent Visitor Goals

    a. As a frequent visitor, I want to view all the recipes I have uploaded.

      - i. When logged in, the My Recipes option appears in the navbar where the user can see all recipes uploaded by themselves.
      <h2 align="center"><img src="static/img/screenshot9.PNG"></h2>

### Further Testing
The site has been tested on Chrome, Edge, Firefox and DuckDuckGo on mobile, desktop and tablet devices of varying screen widths.

Pages all link to each other without issue, and external links open a new tab as expected.

Family also assisted in testing the site, and reported no major issues.

### Known Bugs
- Materialize's form placeholder text overflows to a new line on smaller resolutions.

### Fixed Bugs
- Search initially was not working. This was fixed by adding a search index in MongoDB.
- View Recipe was initially displaying the recipe creator's ID instead of their username - this was fixed by changing the database target on line 185 in app.py.
- Navbar title was wrapping onto the next line on smaller resolutions. This was fixed with CSS media queries.
- The Cuisine dropdown menu on Add Recipe and Edit Recipe was initially showing the entire cuisine array as one option. This was fixed by targeting the array in app.py (lines 169 & 247) and making a nested for loop in addrecipe.html (line 22) and editrecipe.html (line 24).
- Data from the database returned unwanted whitespace in some Edit Recipe form fields and appeared to be not pulling through at all on imgUrl and description fields - this was fixed by both changing the fields' values into textarea content (eg. editrecipe.html, line 39), and removing indents from Jinja for loops in editrecipe.html (lines 50-52, 64-66)
- createdBy became a null value when editing a recipe, fixed by checking reference is createdBy instead of created_by.
- In Edit Recipe, the cuisine dropdown caused update button to not work if not interacted with due to form validation issues - fixed by adding the default value to selected option and removing disabled attribute (editrecipe.html, line 22).

[Back to top](#isadoras-kitchen)

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
cuisines
_id: <ObjectId>
cuisineType: <Array>

recipes
_id: <ObjectId>
recipeName: <string>
cuisine: <string>
recipeDescription: <string>
ingredients: <Array>
method: <Array>
createdBy: <ObjectId>
imgUrl: <string>

users
_id: <ObjectId>
username: <string>
password: <string>
recipes: <Array>
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

[Back to top](#isadoras-kitchen)

## Credits

### Code

### Content

All code was written by the developer.

### Media

- [Background image](https://www.teahub.io/down/JJmTow_spice-indian-spices-hd/)
- Food images taken from [BBC Good Food](https://www.bbcgoodfood.com)
- [Default food image](https://www.hiclipart.com/free-transparent-background-png-clipart-mhidw/download)
- Favicon designed by my fiancee in [Canva](https://www.canva.com)

### Acknowledgements

My mentor, Chris, for once again being a huge help while I was putting this together.

Scott, Rebecca and James from Tutor Support for their excellent ability in nudging me in the right direction towards figuring out solutions for myself.

My fiancee, Isadora, and her mum, Kay, for UX/bug testing this site.

[Back to top](#isadoras-kitchen)