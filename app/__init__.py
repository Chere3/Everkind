from flask import Flask
from flask_mysqldb import MySQL
from flask_login import LoginManager
from config import config
from flask_mail import Mail

from models.ModelUser import ModelUser


# Create the app
app = Flask(__name__)

app.config.from_object(config["development"])
app.config.from_object(config["mail"])

db = MySQL(app)
mail = Mail(app)
adminSession = LoginManager(app)


@adminSession.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


if __name__ == "__main__":
    app.run()
