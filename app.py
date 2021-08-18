import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps
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
    news = list(mongo.db.news.find())
    return render_template("index.html", epics=epics[-5:], events=events, news=news)

@app.route("/browse")
def browse():
    epics = list(mongo.db.epics.find())
    return render_template("browse.html", epics=epics)

@app.route("/browse/search", methods=["GET", "POST"])
def search():
    query_request = request.get_json()
    query = query_request["query"]
    epics = list(mongo.db.epics.find({"$text": {"$search": query}}))
    return dumps(epics)

@app.route("/get_epics")
def get_epics():
    epics = list(mongo.db.epics.find())
    return render_template("browse.html", epics=epics)

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
            "email": request.form.get("email"),
            "is_journalist": False,
            "is_moderator":False
        }
        mongo.db.users.insert_one(register)
        session["user"] = request.form.get("username").lower()
        session["is_journalist"] = False
        session["is_moderator"] = False
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
                session["is_journalist"] = mongo.db.users.find_one({"username": request.form.get("username").lower()})["is_journalist"]
                session["is_moderator"] = mongo.db.users.find_one({"username": request.form.get("username").lower()})["is_moderator"]
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("home"))
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
        user = mongo.db.users.find_one({"username": username})
        epics = list(mongo.db.epics.find({"username": username}))
        news = list(mongo.db.news.find({"username": username}))
        events = list(mongo.db.events.find())
        return render_template("profile.html", username=username, epics=epics,news=news, events=events, user=user)
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash("You have successfully logged out.")
    session.pop("user")
    session.pop("is_moderator")
    session.pop("is_journalist")
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

@app.route("/submit_news", methods=["GET", "POST"])
def submit_news():
    if request.method == "POST":
        post_info = {
            "username": session['user'],
            "title": request.form.get("title"),
            "post_body": request.form.get("post_body"),
            "post_image": request.form.get("post_image"),
        }
        mongo.db.news.insert_one(post_info)
        flash("Submission Successful!")
        return redirect(url_for("home"))
    else:
        return render_template("submit_news.html")

@app.route("/manage_site/<username>", methods=["GET", "POST"])
def manage_site(username):
    if session["user"]:
        epics = list(mongo.db.epics.find())
        users = list(mongo.db.users.find())
        return render_template("manage_site.html", username=username, epics=epics, users=users)
    return redirect(url_for("login"))

@app.route("/manage_user/<username>", methods=["GET", "POST"])
def manage_user(username):
    epics = list(mongo.db.epics.find())
    users = list(mongo.db.users.find())
    if request.method == "POST":
        data = request.form.to_dict()
        for user in users:
            if str(user["_id"]) + '_is_moderator' in data.keys() or str(user["_id"]) + '_is_journalist' in data.keys():
                if request.form.get(str(user["_id"]) + '_is_journalist') == 'on':
                    mongo.db.users.update({"_id": ObjectId(user["_id"])}, {'$set': {"is_journalist" : True}})
                else:
                    mongo.db.users.update({"_id": ObjectId(user["_id"])}, {'$set': {"is_journalist" : False}})
                if request.form.get(str(user["_id"]) + '_is_moderator') == 'on':
                    mongo.db.users.update({"_id": ObjectId(user["_id"])}, {'$set': {"is_moderator" : True}})
                else:
                    mongo.db.users.update({"_id": ObjectId(user["_id"])}, {'$set': {"is_moderator" : False}})

        flash("User Permissions Successfully Updated")
    users = list(mongo.db.users.find())
    return render_template("manage_site.html", username=username, epics=epics, users=users)


@app.route("/edit_epic/<epic_id>", methods=["GET", "POST"])
def edit_epic(epic_id):
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
        mongo.db.epics.update({"_id": ObjectId(epic_id)}, epic_info)
        flash("Epic Successfully Updated")
        return redirect( url_for("profile", username=session["user"]))
    epic = mongo.db.epics.find_one({"_id": ObjectId(epic_id)})
    return render_template("edit_epic.html", epic=epic)

@app.route("/edit_news/<story_id>", methods=["GET", "POST"])
def edit_news(story_id):
    if request.method == "POST":
        post_info = {
            "username": session['user'],
            "title": request.form.get("title"),
            "post_body": request.form.get("post_body"),
            "post_image": request.form.get("post_image"),
        }
        mongo.db.news.update({"_id": ObjectId(story_id)}, post_info)
        flash("News Post Successfully Updated")
        return redirect( url_for("profile", username=session["user"]))
    story = mongo.db.news.find_one({"_id": ObjectId(story_id)})
    return render_template("edit_news.html", story=story)


@app.route("/edit_events/<event_id>", methods=["GET", "POST"])
def edit_events(event_id):
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
    if request.method == "POST":
        mongo.db.events.update({"_id": ObjectId(event_id)}, event_info)
        flash("News Post Successfully Updated")
        return redirect( url_for("profile", username=session["user"]))
    event = mongo.db.events.find_one({"_id": ObjectId(event_id)})
    return render_template("edit_events.html", event=event)

@app.route("/delete_epic/<epic_id>", methods=["GET", "POST"])
def delete_epic(epic_id):
    mongo.db.epics.remove({"_id": ObjectId(epic_id)})
    flash("Post successfully deleted")
    return redirect( url_for("profile", username=session["user"]))

@app.route("/delete_event/<event_id>", methods=["GET", "POST"])
def delete_event(event_id):
    mongo.db.events.remove({"_id": ObjectId(event_id)})
    flash("Event successfully deleted")
    return redirect( url_for("profile", username=session["user"]))

@app.route("/delete_news/<story_id>", methods=["GET", "POST"])
def delete_news(story_id):
    mongo.db.news.remove({"_id": ObjectId(story_id)})
    flash("News Post successfully deleted")
    return redirect( url_for("profile", username=session["user"]))

@app.route("/delete_user/<user_id>", methods=["GET", "POST"])
def delete_user(user_id):
    mongo.db.users.remove({"_id": ObjectId(user_id)})
    flash("Hope to see you back again")
    session.pop("user")
    session.pop("is_moderator")
    session.pop("is_journalist")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
