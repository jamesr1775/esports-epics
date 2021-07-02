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

@app.route("/")

@app.route("/home")
def home():
    epics = list(mongo.db.epics.find())
    events = list(mongo.db.events.find())
    return render_template("index.html", epics=epics, events=events)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user_exists = mongo.db.users.find_one({"username": request.form.get("username").lower()})
        password_match =  request.form.get("password").lower() == request.form.get("pwconfirm").lower()
        if user_exists:
            flash("Invalid Username: That username already exists!")
            return redirect(url_for("register"))
        if not password_match:
            flash("Password Error: Confirmation Password does not match.")
            return redirect(url_for("register"))
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email")
        }
        mongo.db.users.insert_one(register)
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect( url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
    # check if username exists in db
        existing_user = mongo.db.users.find_one(
        {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect( url_for("profile", username=session["user"] ))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")

@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    if session["user"]:
        epics = list(mongo.db.epics.find())
        return render_template("profile.html", username=username, epics=epics)
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash("You have successfully logged out.")
    session.pop("user")
    return redirect(url_for("login"))

@app.route("/submit_epic", methods=["GET", "POST"])
def submit_epic():
    if request.method == "POST":
        epic_info = {
            "username": session['user'],
            "title": request.form.get("title"),
            "game": request.form.get("game"),
            "game_category": request.form.get("game_category"),
            "featured_player": request.form.get("featured_player"),
            "description": request.form.get("description"),
            "short_description": request.form.get("short_description"),
            "tournament": request.form.get("tournament"),
            "tournament_year": request.form.get("tournament_year"),
            "video": request.form.get("video"),
            "image": request.form.get("image"),
        }
        mongo.db.epics.insert_one(epic_info)
        flash("Submission Successful!")
        return redirect(url_for("profile", username=session['user']))
    else:
        return render_template("submit_epic.html")

@app.route("/submit_event", methods=["GET", "POST"])
def submit_event():
    if request.method == "POST":
        event_info = {
            "username": session['user'],
            "title": request.form.get("title"),
            "game": request.form.get("game"),
            "description": request.form.get("description"),
            "start_date": request.form.get("start_date"),
            "start_time": request.form.get("start_time"),
            "end_date": request.form.get("end_date"),
            "location": request.form.get("location"),
            "event_website": request.form.get("event_website"),
            "event_image": request.form.get("event_image"),
        }
        mongo.db.events.insert_one(event_info)
        flash("Submission Successful!")
        epics = list(mongo.db.epics.find())
        return redirect(url_for("home", epics=epics))
    else:
        return render_template("submit_event.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
