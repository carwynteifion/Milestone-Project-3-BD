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
@app.route("/home")
def home():
    """
    Pulls recipes list from the DB and displays on rendered
    home page.
    """
    recipes = list(coll_recipes.find())
    return render_template("home.html", recipes=recipes)


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
        return redirect(url_for("home", username=session["user"]))

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
                        "home", username=session["user"]))
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
                "recipeDescription": request.form.get("recipe_description"),
                "ingredients": ingredients,
                "method": method,
                "imgUrl": request.form.get("img_url"),
                "createdBy": created_by
            }
            insert_recipe = coll_recipes.insert_one(recipe)
            coll_users.update_one(
                {"_id": ObjectId(created_by)},
                {"$push": {"recipes": insert_recipe.inserted_id}})
            flash("Recipe Successfully Added")
            return redirect(
                url_for("view_recipe", recipe_id=insert_recipe.inserted_id))

        cuisines = coll_cuisines.find().sort("cuisineName", 1)
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
    print(created_by)
    return render_template(
        "viewrecipe.html",
        recipe=recipe_name,
        created_by=created_by)


@app.route("/update_recipe_details/<recipe_id>")
def update_recipe_details(recipe_id):
    """
    Populates Edit Recipe page with current recipe
    details from database
    """
    if "user" in session:
        recipe_to_edit = coll_recipes.find_one({"_id": ObjectId(recipe_id)})
        user = coll_users.find_one({"username": session["user"]})["_id"]
        if user == recipe_to_edit.get("createdBy"):
            ingredients = recipe_to_edit.get("ingredients")
            method = recipe_to_edit.get("method")
            cuisines = coll_cuisines.find().sort("cuisineName", 1)
            return render_template(
                "editrecipe.html",
                recipe_to_edit=recipe_to_edit,
                ingredients=ingredients,
                method=method,
                cuisines=cuisines)
        else:
            flash("Only the recipe author can do this")
            return redirect(url_for("view_recipe", recipe_id=recipe_id))
    else:
        flash("You must be logged in to do this")
        return redirect(url_for("login"))



@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    Posts update to selected recipe to database
    """
    if "user" in session:
        recipe_to_edit = coll_recipes.find_one({"_id": ObjectId(recipe_id)})
        user = coll_users.find_one({"username": session["user"]})["_id"]
        if user == recipe_to_edit.get("createdBy"):
            if request.method == "POST":
                recipe = coll_recipes.find_one({"_id": ObjectId(recipe_id)})
                ingredients = request.form.get("ingredients").splitlines()
                method = request.form.get("method").splitlines()
                created_by = recipe.get("created_by")
                submit = {
                    "recipeName": request.form.get("recipe_name"),
                    "cuisine": request.form.get("cuisine"),
                    "recipeDescription": request.form.get("recipe_description"),
                    "ingredients": ingredients,
                    "method": method,
                    "createdBy": created_by,
                    "imgUrl": request.form.get("img_url")
                }
                coll_recipes.replace_one({"_id": ObjectId(recipe_id)}, submit)
                flash("Recipe Successfully Updated")

            recipe = coll_recipes.find_one({"_id": ObjectId(recipe_id)})
            cuisines = coll_cuisines.find().sort("cuisineName", 1)
            return render_template(
                "viewrecipe.html", recipe=recipe, cuisines=cuisines)
        else:
            flash("Only the recipe author can do this")
            return redirect(url_for("view_recipe", recipe_id=recipe_id))
    else:
        flash("You must be logged in to do this")
        return redirect(url_for("login"))


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    Deletes recipe from database and removes recipe
    entry from user recipe list.
    """
    if "user" in session:
        recipe_to_delete = coll_recipes.find_one({"_id": ObjectId(recipe_id)})
        user = coll_users.find_one({"username": session["user"]})["_id"]
        if user == recipe_to_delete.get("createdBy"):
            created_by = coll_recipes.find_one({"_id": ObjectId(recipe_id)})["createdBy"]
            coll_recipes.delete_one({"_id": ObjectId(recipe_id)})
            coll_users.update_one(
                {"_id": ObjectId(created_by)},
                {"$pull": {"recipes": ObjectId(recipe_id)}})
            return redirect(url_for("home"))
        else:
            flash("Only the recipe author can do this")
            return redirect(url_for("view_recipe", recipe_id=recipe_id))
    else:
        flash("You must be logged in to do this")
        return redirect(url_for("login"))


@app.route("/my_recipes/<username>")
def my_recipes(username):
    """
    Renders user's own recipes.
    """
    if "user" in session:
        current_user = coll_users.find_one({"username": session["user"]})["_id"]
        user_id = coll_users.find_one({"username": username})["_id"]
        if current_user == user_id:
            return render_template("myrecipes.html")              
        else:
            flash("You do not have access to this page")
            return redirect(url_for("home"))
    else:
        flash("You must be logged in first")
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)