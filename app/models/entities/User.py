from werkzeug.security import check_password_hash
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id, username, password, role_id, created_at, updated_at) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.role_id = role_id
        self.created_at = created_at
        self.updated_at = updated_at

    # Check if the password is correct
    @classmethod
    def validatePassword(self, encriptedPassword, password):
        # Check if password is correct using werkzeug
        return check_password_hash(encriptedPassword, password)
