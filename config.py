import os


class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
    PORT = 3300


class DevelopmentConfig(Config):

    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "thepeoplelproyect"

    """
    # pythonanywhere
    MYSQL_HOST = "thepeoplesproyect.mysql.pythonanywhere-services.com"
    MYSQL_USER = "thepeoplesproyec"
    MYSQL_PASSWORD = "ucw8kgn6unt4znz@MVY"
    MYSQL_DB = "thepeoplesproyec$thepeoplesproyect"
    """


class MailConfig(Config):
    DEBUG = True
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_USERNAME")


config = {"development": DevelopmentConfig, "mail": MailConfig}
