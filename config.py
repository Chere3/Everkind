import os


def _as_bool(value: str | None, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


class Config:
    DEBUG = _as_bool(os.environ.get("FLASK_DEBUG"), True)
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-me")
    PORT = int(os.environ.get("PORT", "3300"))


class DevelopmentConfig(Config):
    MYSQL_HOST = os.environ.get("DB_HOST", "localhost")
    MYSQL_USER = os.environ.get("DB_USER", "root")
    MYSQL_PASSWORD = os.environ.get("DB_PASSWORD", "")
    MYSQL_DB = os.environ.get("DB_NAME", "everkind")


class MailConfig(Config):
    DEBUG = _as_bool(os.environ.get("MAIL_DEBUG"), True)
    MAIL_SERVER = os.environ.get("MAIL_SERVER", "smtp.gmail.com")
    MAIL_PORT = int(os.environ.get("MAIL_PORT", "587"))
    MAIL_USE_TLS = _as_bool(os.environ.get("MAIL_USE_TLS"), True)
    MAIL_USE_SSL = _as_bool(os.environ.get("MAIL_USE_SSL"), False)
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_USERNAME")


config = {"development": DevelopmentConfig, "mail": MailConfig}
