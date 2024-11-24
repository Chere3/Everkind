from models.entities.Guest import Guest


class ModelGuest:
    """
    A class representing a guest model.
    Methods:
    - create(db, guest): Creates a new guest in the database.
    - get_all(db): Retrieves all guests from the database.
    - get_by_id(db, id): Retrieves a guest by their ID from the database.
    - update(db, guest): Updates a guest in the database.
    - delete(db, id): Deletes a guest from the database.
    """

    @classmethod
    def create(self, db, guest):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to insert a new guest into the guests table
            cursor.execute(
                "INSERT INTO guests (name, contact_info) VALUES (%s, %s)",
                (guest.name, guest.contact_info),
            )
            # Commit the transaction to save the changes in the database
            db.connection.commit()
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def get_all(self, db):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to retrieve all guests from the guests table
            cursor.execute("SELECT * FROM guests")
            # Fetch all the results from the executed query
            guests = cursor.fetchall()
            # Return the list of guests
            return guests
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to retrieve a guest by their ID from the guests table
            cursor.execute("SELECT * FROM guests WHERE id = %s", (id,))
            # Fetch the result from the executed query
            guest = cursor.fetchone()
            # Return the guest object
            return Guest(guest[1], guest[2], guest[3], guest[4])
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def update(self, db, guest):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to update a guest in the guests table
            cursor.execute(
                "UPDATE guests SET name = %s, contact_info = %s WHERE id = %s",
                (guest.name, guest.contact_info, guest.id),
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
            # Execute the SQL query to delete a guest from the guests table by ID
            cursor.execute("DELETE FROM guests WHERE id = %s", (id,))
            # Commit the transaction to save the changes in the database
            db.connection.commit()
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)
