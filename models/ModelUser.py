from models.entities.User import User
from werkzeug.security import check_password_hash


class ModelUser:
    """
    A class representing a user model.
    Methods:
    - signin(db, user): Sign in a user.
    - get_all(db): Get all users.
    - get_by_id(db, id): Get a user by ID.
    - create(db, user): Create a new user.
    - update(db, user): Update an existing user.
    - delete(db, id): Delete a user.
    - validatePassword(encriptedPassword, password): Validate a password.
    """

    @classmethod
    def signin(self, db, user):
        try:
            # Get the user info from the form
            selectedUser = db.connection.cursor()
            # Execute the SQL query to select a user by username
            selectedUser.execute(
                "SELECT * FROM users WHERE username = %s", (user.username,)
            )
            # Fetch the result from the executed query
            u = selectedUser.fetchone()

            # Check if user already exists
            if u is not None:
                # Return the user object if found
                return User(u[0], u[1], u[2], u[3], u[4], u[5])
            else:
                # Return None if user does not exist
                return None

        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def get_all(self, db):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to retrieve all users from the users table
            cursor.execute("SELECT * FROM users")
            # Fetch all the results from the executed query
            users = cursor.fetchall()
            # Return the list of users
            return users
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to retrieve a user by their ID from the users table
            cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
            # Fetch the result from the executed query
            user = cursor.fetchone()
            # Return the user object
            return User(user[0], user[1], user[2], user[3], user[4], user[5])
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def get_by_username(self, db, id):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to retrieve a user by their ID from the users table
            cursor.execute("SELECT * FROM users WHERE username = %s", (id,))
            # Fetch the result from the executed query
            user = cursor.fetchone()
            # Return the user object
            return User(user[0], user[1], user[2], user[3], user[4], user[5])
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def create(self, db, user):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to insert a new user into the users table
            cursor.execute(
                "INSERT INTO users (username, password, role_id) VALUES (%s, %s, %s)",
                (user.username, user.password, user.role_id),
            )
            # Commit the transaction to save the changes in the database
            db.connection.commit()
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def update(self, db, user):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to update a user in the users table
            cursor.execute(
                "UPDATE users SET username = %s, password = %s, role_id = %s WHERE id = %s",
                (user.username, user.password, user.role_id, user.id),
            )
            # Commit the transaction to save the changes in the database
            db.connection.commit()
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def delete(self, db, id):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to delete a user from the users table by ID
            cursor.execute("DELETE FROM users WHERE id = %s", (id,))
            # Commit the transaction to save the changes in the database
            db.connection.commit()
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def validatePassword(self, encriptedPassword, password):
        # Check if password is correct using werkzeug
        return check_password_hash(encriptedPassword, password)
