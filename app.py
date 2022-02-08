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


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(coll_recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/register.html", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = coll_users.find_one(
            {"username": request.form.get("username".lower()})
        
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        coll_users.insert_one(register)

        # put the new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("my_recipes", username=session["user"]))

    return render_template("register.html")




if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)