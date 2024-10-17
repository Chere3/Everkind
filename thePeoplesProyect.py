from flask import Flask, render_template, url_for, request, redirect
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
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
            "INSERT INTO usuarios (nombre, correo, clave, fecha) VALUES (%s, %s, %s, %s)",
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
    if request.method == "POST":
       usuario = User(0, None, request.form["email"], request.form["clave"], None, None)
       usuarioAutenticado = ModelUser.signin(db, usuario)
       
       if usuarioAutenticado is not None:
           login_user(usuarioAutenticado)
           if usuarioAutenticado.clave:
               if usuarioAutenticado.perfil == "A":
                return render_template("admin.html")
               else:
                return render_template("user.html")
           else:
                return "CONTRASEÑA INCORRECTA"
       else:
            return "El usuario no existe"

           
    return render_template("signin.html")

@thePeoplesProyect.route("/auth/logout")
def logout():
    logout_user()
    return render_template("home.html")
    


@thePeoplesProyect.route("/api")
def api():
    return {
        "name": "thePeoplesProyect",
        "version": "1.0.0",
        "description": "A simple API for the people",
    }


if __name__ == "__main__":
    
    thePeoplesProyect.run(port=3300)
   
    
    