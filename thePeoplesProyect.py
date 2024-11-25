from flask import Flask, render_template, request, flash, redirect
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash
from config import config

from models.ModelUser import ModelUser
from models.ModelOccupant import ModelOccupant
from models.ModelGuest import ModelGuest

from models.entities.User import User
from models.entities.Occupant import Occupant
from models.entities.Guest import Guest

import datetime
import traceback


# Create the app
thePeoplesProyect = Flask(__name__)

# pythonAnywhere
thePeoplesProyect.config.from_object(config["development"])
adminSession = LoginManager(thePeoplesProyect)
db = MySQL(thePeoplesProyect)


@adminSession.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


@thePeoplesProyect.route("/")
def home():
    if current_user.is_authenticated:
        if current_user.role_id == 2:
            return render_template("admin/admin.html")
        else:
            if current_user.role_id == 1:
                return redirect("/onboarding")
            if current_user.role_id >= 3:
                return render_template("dashboards/dashboard.html")
    return render_template("home.html")


@thePeoplesProyect.route("/home")
def homepage():
    if not current_user.is_authenticated:
        return redirect("/")
    else:
        return render_template("home.html")


# Auth routes
@thePeoplesProyect.route("/auth/register", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect("/onboarding")
    if request.method == "POST":
        try:
            # Get the user info from the form
            username = request.form["username"]
            password = request.form["password"]
            repeatPassword = request.form["repeat-password"]

            if password != repeatPassword:
                flash("Passwords does not match")
                return redirect(request.url)

            encryptedPassword = generate_password_hash(password)

            # Check if user already exists
            cursor = db.connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s", [username])

            user = cursor.fetchone()
            if user:
                flash("User already exists")
                return redirect(request.url)

            # Insert user info the database
            ModelUser.create(
                db,
                User(
                    0,
                    username,
                    encryptedPassword,
                    1,
                    datetime.datetime.now(),
                    datetime.datetime.now(),
                ),
            )

            # Close the cursor and commit the changes
            db.connection.commit()
            cursor.close()

            user = ModelUser.signin(
                db,
                User(
                    0,
                    username,
                    password,
                    None,
                    None,
                    None,
                ),
            )

            login_user(user)

            # Send to home page
            return redirect("/")

        except Exception:
            flash("An unexpected error occurred")
            traceback.print_exc()
            return redirect(request.url)

    return render_template("auth/signup.html")


@thePeoplesProyect.route("/onboarding", methods=["GET", "POST"])
def complete_profile():
    if not current_user.is_authenticated:
        return redirect("/auth/login")

    if current_user.role_id >= 3:
        return redirect("/")

    if request.method == "POST":
        try:
            # Get the user info from the form
            firstName = request.form["first-name"]
            lastName = request.form["last-name"]
            userTypeId = request.form["user-type"]

            if userTypeId == "3":
                userTypeId = 3
            elif userTypeId == "4":
                userTypeId = 4

            # Insert user info the database
            ModelUser.update(
                db,
                User(
                    current_user.id,
                    current_user.username,
                    current_user.password,
                    userTypeId,
                    datetime.datetime.now(),
                    datetime.datetime.now(),
                ),
            )

            if userTypeId == 4:
                ModelOccupant.create(
                    db,
                    Occupant(
                        0,
                        current_user.id,
                        None,
                        None,
                        None,
                        datetime.datetime.now(),
                        datetime.datetime.now(),
                        None,
                        firstName + " " + lastName,
                    ),
                )
                db.connection.commit()
            elif userTypeId == 3:
                ModelGuest.create(
                    db,
                    Guest(
                        0,
                        firstName + " " + lastName,
                        None,
                        datetime.datetime.now(),
                        datetime.datetime.now(),
                    ),
                )
                db.connection.commit()

            # Send to home page
            return render_template("home.html")
        except Exception:
            flash("An unexpected error occurred")
            traceback.print_exc()
            return redirect(request.url)

    else:
        return render_template("auth/complete_profile.html")


@thePeoplesProyect.route("/auth/login", methods=["GET", "POST"])
def signin():
    if current_user.is_authenticated:
        return redirect("/onboarding")
    # Check if the request is a POST
    if request.method == "POST":
        try:
            # Get the user info from the form
            user = User(
                0, request.form["username"], request.form["password"], None, None, None
            )
            # Get the user from the database
            authUser = ModelUser.signin(db, user)

            # Check if the user exists
            if authUser is not None:
                login_user(authUser)
                if authUser.password:
                    # Check if the profile is admin or user
                    if authUser.role_id == 2:
                        return render_template("admin/admin.html")
                    else:
                        if authUser.role_id == 1:
                            return redirect("/onboarding")
                        if authUser.role_id >= 3:
                            return redirect("/")
                else:
                    # Send a message if the username or password is incorrect
                    flash("Email or password incorrect")
                    return redirect(request.url)
            else:
                # Send a message if the user does not exist
                flash("The user does not exist")
                return redirect(request.url)
        except Exception:
            flash("An unexpected error occurred")
            traceback.print_exc()
            return redirect(request.url)

    return render_template("auth/signin.html")


@thePeoplesProyect.route("/auth/logout")
def logout():
    logout_user()
    # Send to home page
    return redirect("/")


@thePeoplesProyect.route("/admin/users", methods=["GET", "POST"])
def users():
    if current_user.role_id != 2:
        return render_template("404.html")
    # Get all the users from the database
    u = ModelUser.get_all(db)

    # Send the users to the template
    return render_template("admin/users.html", users=u)


@thePeoplesProyect.route("/admin/users/create", methods=["GET", "POST"])
def create_user():
    # Check if the request is a POST
    ModelUser.create(
        db,
        User(
            0,
            request.form["name"],
            request.form["username"],
            request.form["password"],
            request.form["profile"],
            None,
            None,
        ),
    )
    # Close the cursor
    flash("The user has been created successfully")

    return redirect("/admin/users")


@thePeoplesProyect.route("/admin/users/update/<int:id>", methods=["POST"])
def update_user(id):
    try:
        ModelUser.update(
            db,
            User(
                id,
                request.form["name"],
                request.form["username"],
                request.form["password"],
                request.form["profile"],
                None,
                None,
            ),
        )

        # Send a message to the user
        flash("The user has been updated successfully")
        return redirect("/admin/users")
    except Exception:
        # Send a message to the user saying that an error occurred
        flash("An unexpected error occurred")
        # Print the error pretty in the console
        traceback.print_exc()

        return redirect("/admin/users")


@thePeoplesProyect.route("/admin/users/delete/<int:id>", methods=["POST"])
def delete_user(id):
    try:
        ModelUser.delete(db, id)
        return redirect("/admin/users")

    except Exception:
        # Send a message to the user saying that an error occurred
        flash("An unexpected error occurred")
        # Print the error pretty in the console
        traceback.print_exc()

        return redirect("/admin/users")


@thePeoplesProyect.route("/api")
def api():
    return {
        "name": "thePeoplesProyect",
        "version": "1.0.0",
        "description": "A simple API for the people",
    }


@thePeoplesProyect.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    thePeoplesProyect.run(port=3300)
