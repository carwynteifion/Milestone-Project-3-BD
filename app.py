import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Collections
coll_users = mongo.db.users
coll_recipes = mongo.db.recipes
coll_cuisines = mongo.db.cuisines


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    """
    Pulls recipes list from the DB and displays on rendered
    home page.
    """
    recipes = list(coll_recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Pulls up register page for users to create an account.
    Validates inputs for username and password and posts
    to database before redirecting to user recipes page.
    """
    if request.method == "POST":
        existing_user = coll_users.find_one(
            {"username": request.form.get("username".lower())})

        # check if user exists already
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # check username length
        if len(request.form.get("username")) < 5 or len(request.form.get("username")) > 20:
            flash("Usernames must be between 5 and 20 characters long")
            return redirect(url_for("register"))
        
        # check password length
        if len(request.form.get("password")) < 8 or len(request.form.get("password")) > 20:
            flash("Passwords must be between 8 and 20 characters long")
            return redirect(url_for("register"))

        # populates and posts JSON object to DB
        user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "recipes": [],
            "favourites": []
        }
        coll_users.insert_one(user)

        # put the new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("get_recipes", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Checks inputted username and password against DB list.
    If username and password both match, logs the user
    into a session and redirects to their My Recipes page.
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = coll_users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "get_recipes", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    """
    Logs user out of session
    """
    flash("Successfully logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """
    Adds recipe to database
    """
    if "user" in session: 
        created_by = coll_users.find_one({"username": session["user"]})["_id"]
        if request.method == "POST":
            # Ingredients and Prep converted into lists
            ingredients = request.form.get("ingredients").splitlines()
            method = request.form.get("method").splitlines()

            # Creates JSON entry for recipe
            recipe = {
                "recipeName": request.form.get("recipe_name"),
                "cuisine": request.form.get("cuisine"),
                "recipeDescription": request.form.get("recipe_description") ,
                "method": method,
                "ingredients": ingredients,
                "createdBy": created_by
            }
            insertRecipe = coll_recipes.insert_one(recipe)
            coll_users.update_one(
                {"_id": ObjectId(created_by)},
                {"$push": {"recipes": insertRecipe.inserted_id}})
            flash("Recipe Successfully Added")
            return redirect(url_for("view_recipe",
            recipe_id=insertRecipe.inserted_id))

        cuisines = coll_cuisines.find().sort("cuisine_name", 1)
        return render_template("addrecipe.html", cuisines=cuisines)

    else:
        flash("You must be logged in to do this!")
        return redirect(url_for("login"))


@app.route("/view_recipe/<recipe_id>")
def view_recipe(recipe_id):
    """
    View recipe
    """
    recipe_name = coll_recipes.find_one({"_id": ObjectId(recipe_id)})
    created_by = coll_users.find_one(
        {"_id": ObjectId(recipe_name.get("createdBy"))})["username"]
    return render_template(
        "viewrecipe.html",
        recipe=recipe_name,
        created_by=created_by)



@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    Edits recipe
    """
    if "user" in session:
        if request.method == "POST":
            submit = {
                "recipeName": request.form.get("recipe_name"),
                "cuisine": request.form.get("cuisine"),
                "recipeDescription": recipe_description,
                "method": method,
                "ingredients": ingredients,
                "createdBy": created_by
            }
            coll_recipes.replace_one({"_id": ObjectId(recipe_id)}, submit)
            flash("Recipe Successfully Updated")

        recipe = coll_recipes.find_one({"_id": ObjectId(recipe_id)})
        cuisines = coll_cuisines.find().sort("cuisine_name", 1)
        return render_template("edit_recipe.html", recipe=recipe, cuisines=cuisines)
    else:
        flash("You must be logged in to do this")
        return url_for("login")


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    Deletes recipe from database
    """
    if "user" in session:
        coll_recipes.delete_one({"_id": ObjectId(recipe_id)})
        flash("Recipe Successfully Deleted")
        return redirect(url_for("get_recipes"))
    else:
        flash("You must be logged in to do this")
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)