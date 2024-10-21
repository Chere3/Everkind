from flask import Flask, render_template, request, flash, redirect
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user
from werkzeug.security import generate_password_hash
from config import config
from models.ModelUser import ModelUser
from models.entities.User import User

import datetime

thePeoplesProyect = Flask(__name__)
db = MySQL(thePeoplesProyect)
adminSession = LoginManager(thePeoplesProyect)

thePeoplesProyect.config.from_object(config["development"])


@adminSession.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


@thePeoplesProyect.route("/")
def home():
    return render_template("home.html")


# Auth routes
@thePeoplesProyect.route("/auth/register", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Get the user info from the form
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        encryptedPassword = generate_password_hash(password)
        registeredDate = datetime.datetime.now()

        # Check if user already exists
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s", [email])
        user = cursor.fetchone()
        if user:
            return "User already exists"

        # Insert user info the database
        cursor.execute(
            "INSERT INTO usuarios (nombre, correo, clave, fechareg) VALUES (%s, %s, %s, %s)",
            (name, email, encryptedPassword, registeredDate),
        )

        # Close the cursor and commit the changes
        db.connection.commit()
        cursor.close()

        # Send to home page
        return render_template("home.html")

    return render_template("signup.html")


@thePeoplesProyect.route("/auth/login", methods=["GET", "POST"])
def signin():
    # Check if the request is a POST
    if request.method == "POST":
        user = User(0, None, request.form["email"], request.form["clave"], None, None)
        authUser = ModelUser.signin(db, user)

        # Check if the user exists
        if authUser is not None:
            login_user(authUser)
            if authUser.clave:
                # Check if the profile is admin or user
                if authUser.perfil == "A":
                    return render_template("admin.html")
                else:
                    return render_template("user.html")
            else:
                # Send a message if the email or password is incorrect
                flash("Email or password incorrect")
                return redirect(request.url)
        else:
            # Send a message if the user does not exist
            flash("The user does not exist")
            return redirect(request.url)

    return render_template("signin.html")


@thePeoplesProyect.route("/auth/logout")
def logout():
    logout_user()
    # Send to home page
    return render_template("home.html")


@thePeoplesProyect.route("/admin/users", methods=["GET", "POST"])
def users():
    # Get all the users from the database
    users = db.connection.cursor()
    users.execute("SELECT * FROM usuarios")
    u = users.fetchall()
    users.close()

    # Send the users to the template
    return render_template("users.html", usuarios=u)


@thePeoplesProyect.route("/admin/users/create", methods=["GET", "POST"])
def create_user():
    passwordHash = generate_password_hash(request.form["password"])
    date = datetime.datetime.now()

    createUser = db.connection.cursor()
    createUser.execute(
        "INSERT INTO usuarios (nombre, correo, clave, fechareg, perfil) VALUES (%s, %s, %s, %s, %s)",
        (
            request.form["name"],
            request.form["email"],
            passwordHash,
            date,
            request.form["profile"],
        ),
    )

    db.connection.commit()
    flash("The user has been created successfully")

    return redirect("/admin/users")


@thePeoplesProyect.route("/api")
def api():
    return {
        "name": "thePeoplesProyect",
        "version": "1.0.0",
        "description": "A simple API for the people",
    }


if __name__ == "__main__":

    thePeoplesProyect.run(port=3300)
