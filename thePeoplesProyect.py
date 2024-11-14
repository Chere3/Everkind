from flask import Flask, render_template, request, flash, redirect
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user
from werkzeug.security import generate_password_hash
from config import config
from models.ModelUser import ModelUser
from models.entities.User import User

import datetime
import traceback

# Create the app
thePeoplesProyect = Flask(__name__)
db = MySQL(thePeoplesProyect)

# pythonAnywhere
thePeoplesProyect.config.from_object(config["development"])
adminSession = LoginManager(thePeoplesProyect)


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
        try:
            # Get the user info from the form
            email = request.form["email"]
            password = request.form["password"]
            repeatPassword = request.form["repeat-password"]

            if password != repeatPassword:
                flash("Passwords does not match")
                return redirect(request.url)

            encryptedPassword = generate_password_hash(password)

            # Check if user already exists
            cursor = db.connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s", [email])

            user = cursor.fetchone()
            if user:
                flash("User already exists")
                return redirect(request.url)

            # Insert user info the database
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (email, encryptedPassword),
            )

            # Close the cursor and commit the changes
            db.connection.commit()
            cursor.close()

            # Send to home page
            return render_template("home.html")

        except Exception:
            flash("An unexpected error occurred")
            traceback.print_exc()
            return redirect(request.url)

    return render_template("signup.html")


@thePeoplesProyect.route("/auth/login", methods=["GET", "POST"])
def signin():
    # Check if the request is a POST
    if request.method == "POST":
        try:
            # Get the user info from the form
            user = User(
                0, None, request.form["email"], request.form["clave"], None, None
            )
            # Get the user from the database
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
        except Exception:
            flash("An unexpected error occurred")
            traceback.print_exc()
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
    # Check if the request is a POST
    passwordHash = generate_password_hash(request.form["password"])
    date = datetime.datetime.now()

    createUser = db.connection.cursor()

    # Insert the user into the database
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
    # Close the cursor
    flash("The user has been created successfully")

    return redirect("/admin/users")


@thePeoplesProyect.route("/admin/users/update/<int:id>", methods=["POST"])
def update_user(id):
    try:
        # Update the user in the database
        cursor = db.connection.cursor()
        # Execute the query
        cursor.execute(
            "UPDATE usuarios SET nombre = %s, correo = %s, clave = %s, perfil = %s WHERE id = %s",
            (
                request.form["name"],
                request.form["email"],
                generate_password_hash(request.form["password"]),
                request.form["profile"],
                id,
            ),
        )

        db.connection.commit()
        cursor.close()

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
        # Delete the user from the database
        cursor = db.connection.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = %s", [id])

        db.connection.commit()
        cursor.close()

        # Send a message to the user
        flash("The user has been deleted successfully")

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


"""if __name__ == "__main__":
    thePeoplesProyect.run(port=3300)
"""
