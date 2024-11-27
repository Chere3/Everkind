from flask import Flask, render_template, request, flash, redirect
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash
from config import config
from flask_mail import Mail, Message

from models.ModelOrderHistory import ModelOrderHistory
from models.ModelUser import ModelUser
from models.ModelOccupant import ModelOccupant
from models.ModelGuest import ModelGuest
from models.ModelPartialRooms import ModelPartialRooms
from models.ModelRoom import ModelRoom

from models.entities import Room
from models.entities.PartialRoom import PartialRoom
from models.entities.User import User
from models.entities.Occupant import Occupant
from models.entities.Guest import Guest


import datetime
import traceback


# Create the app
thePeoplesProyect = Flask(__name__)


# pythonanywhere
thePeoplesProyect.config.from_object(config["development"])
thePeoplesProyect.config.from_object(config["mail"])
db = MySQL(thePeoplesProyect)
mail = Mail(thePeoplesProyect)
adminSession = LoginManager(thePeoplesProyect)


@adminSession.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


@thePeoplesProyect.route("/")
def home():
    if current_user.is_authenticated:
        if current_user.role_id == 2:
            orders = ModelOrderHistory.get_all(db)
            return render_template("admin/admin.html", user=current_user, orders=orders)
        else:
            if current_user.role_id == 1:
                return redirect("/onboarding")
            if current_user.role_id >= 3:
                user = ModelOccupant.get_by_user_id(db, current_user.id)
                orders = ModelOrderHistory.get_by_user_id(db, current_user.id)

                return render_template(
                    "dashboards/dashboard.html", user=user[0], orders=orders
                )
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

            # Send a message to the user
            message = Message(
                "Welcome to the People's Project",
                recipients=[user.username],
            )

            message.html = render_template("mails/register.html", user=user)
            mail.send(message)

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
            return redirect("/")
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


@thePeoplesProyect.route("/rooms")
def rooms():
    rooms = ModelRoom.get_all(db)
    # Convert tuple to array
    rooms = [list(i) for i in rooms]
    # Sort the array by room number
    rooms.sort(key=lambda x: int(x[2]))
    return render_template("rooms/rooms.html", rooms=rooms)


@thePeoplesProyect.route("/admin/room/create", methods=["GET", "POST"])
def create_room():
    if current_user.role_id != 2:
        return render_template("404.html")
    if request.method == "POST":
        try:
            # Get the room info from the form
            name = request.form["name"]
            roomNumber = request.form["number"]
            capacity = request.form["capacity"]
            roomTypeId = request.form["room-type-id"]
            roomTypePhoto = request.form["room-type-photo"]

            ModelPartialRooms.create(
                db,
                PartialRoom(
                    0,
                    name,
                    roomNumber,
                    capacity,
                    datetime.datetime.now(),
                    datetime.datetime.now(),
                    roomTypeId,
                    roomTypePhoto,
                ),
            ),

            # Send a message to the user
            flash("The room has been created successfully")

            # Send to home page
            return redirect("/")

        except Exception:
            flash("An unexpected error occurred")
            traceback.print_exc()
            return redirect(request.url)

    return render_template("admin/create-room.html")


@thePeoplesProyect.route("/admin/room/update/<int:id>", methods=["GET", "POST"])
def update_room(id):
    if current_user.role_id != 2:
        return render_template("404.html")
    if request.method == "POST":
        try:
            # Get the room info from the form
            name = request.form["name"]
            roomNumber = request.form["number"]
            capacity = request.form["capacity"]
            roomTypeId = request.form["room-type-id"]
            roomTypePhoto = request.form["room-type-photo"]

            ModelPartialRooms.update(
                db,
                PartialRoom(
                    id,
                    name,
                    roomNumber,
                    capacity,
                    datetime.datetime.now(),
                    datetime.datetime.now(),
                    roomTypeId,
                    roomTypePhoto,
                ),
            )

            # Send a message to the user
            flash("The room has been updated successfully")

            # Send to home page
            return redirect("/")

        except Exception:
            flash("An unexpected error occurred")
            traceback.print_exc()
            return redirect(request.url)

    room = ModelPartialRooms.get_by_id(db, id)
    return render_template("admin/update-room.html", room=room)


@thePeoplesProyect.route("/admin/room/delete/<int:id>", methods=["POST"])
def delete_room(id):
    if current_user.role_id != 2:
        return render_template("404.html")
    try:
        ModelPartialRooms.delete(db, id)
        return redirect("/")

    except Exception:
        flash("An unexpected error occurred")
        traceback.print_exc()
        return redirect("/")


@thePeoplesProyect.route("/rooms/<int:id>")
def room(id):
    room = ModelRoom.get_by_id(db, id)
    return render_template("rooms/room.html", room=room)


@thePeoplesProyect.route("/rooms/<int:id>/book")
def book_room(id):
    if not current_user.is_authenticated:
        return redirect("/auth/login")
    user_id = current_user.id
    order_date = datetime.datetime.now()
    status = 1

    try:
        ModelRoom.book_room(db, id, user_id, order_date, status)
        flash("Room booked successfully")
        return redirect("/")
    except Exception:
        flash("An unexpected error occurred")
        traceback.print_exc()
        return redirect("/")


@thePeoplesProyect.route("/rooms/<int:id>/cancel")
def cancel_room(id):
    if not current_user.is_authenticated:
        return redirect("/auth/login")
    user_id = current_user.id
    order_date = datetime.datetime.now()
    status = 0

    try:
        ModelRoom.cancel_room(db, id, user_id, order_date, status)
        flash("Room canceled successfully")
        return redirect("/")
    except Exception:
        flash("An unexpected error occurred")
        traceback.print_exc()
        return redirect("/")


@thePeoplesProyect.route("/rooms/manage")
def manage_rooms():
    if not current_user.is_authenticated:
        return redirect("/auth/login")

    if current_user.role_id == 2:
        rooms = ModelRoom.get_all(db)
        return render_template("admin/manage-rooms.html", rooms=rooms)

    if current_user.role_id < 3:
        return render_template("404.html")
    rooms = ModelRoom.get_by_user_id(db, current_user.id)
    return render_template("rooms/manage.html", rooms=rooms)


@thePeoplesProyect.route("/orders")
def orders():
    if not current_user.is_authenticated:
        return redirect("/auth/login")

    if current_user.role_id == 2:
        orders = ModelOrderHistory.get_all(db)
        return render_template("admin/orders.html", orders=orders)

    orders = ModelOrderHistory.get_by_user_id(db, current_user.id)
    return render_template("dashboards/orders.html", orders=orders)


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
            request.form["username"],
            request.form["password"],
            request.form["role-id"],
            datetime.datetime.now(),
            datetime.datetime.now(),
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
                request.form["username"],
                request.form["password"],
                request.form["role-id"],
                None,
                datetime.datetime.now(),
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


@thePeoplesProyect.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


"""
if __name__ == "__main__":
    thePeoplesProyect.run(port=3300)
"""
