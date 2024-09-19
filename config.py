class Config:
    DEBUG = True
    SECRET_KEY = "sbxJfPvf27kmD-X2UpkipWlK7KIA"
    PORT = 3300


class DevelopmentConfig(Config):
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "thepeoplelproyect"
