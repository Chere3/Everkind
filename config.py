class Config:
    DEBUG = True
    SECRET_KEY = "sbxJfPvf27kmD-X2UpkipWlK7KIA"
    PORT = 3300


class DevelopmentConfig(Config):
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "thepeoplelproyect"

    """# pythonanywhere
    MYSQL_HOST = "thepeoplesproyect.mysql.pythonanywhethepeopleproyectre-services.com"
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
    MAIL_USERNAME = "diego.romero1798@alumnos.udg.mx"
    MAIL_PASSWORD = "cefu pjtk lvbw irhn"
    MAIL_DEFAULT_SENDER = "diego.romero1798@alumnos.udg.mx"


config = {"development": DevelopmentConfig, "mail": MailConfig}
