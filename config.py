class Config:
    DEBUG = True
    SECRET_KEY = "sbxJfPvf27kmD-X2UpkipWlK7KIA"
    PORT = 3300


class DevelopmentConfig(Config):
    '''MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "thepeoplelproyect"'''

    # pythonanywhere
    MYSQL_HOST = "thepeoplesproyect.mysql.pythonanywhethepeopleproyectre-services.com"
    MYSQL_USER = "thepeoplesproyec"
    MYSQL_PASSWORD = "ucw8kgn6unt4znz@MVY"
    MYSQL_DB = "thepeoplesproyec$thepeoplesproyect"


config = {"development": DevelopmentConfig}
