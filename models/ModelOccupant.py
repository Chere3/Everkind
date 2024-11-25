from models.entities.Occupant import Occupant


class ModelOccupant:
    """
    A class representing an occupant model.
    Methods:
    - create(db, occupant): Create a new occupant.
    - get_all(db): Get all occupants.
    - get_by_id(db, id): Get an occupant by ID.
    - update(db, occupant): Update an existing occupant.
    - delete(db, id): Delete an occupant.
    """

    @classmethod
    def create(self, db, occupant):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to insert a new occupant into the occupants table
            cursor.execute(
                "INSERT INTO occupants (user_id, room_id, start_date, end_date, guest_id, name) VALUES (%s, %s, %s, %s, %s, %s)",
                (
                    occupant.user_id,
                    occupant.room_id,
                    occupant.start_date,
                    occupant.end_date,
                    occupant.guest_id,
                    occupant.name,
                ),
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
            # Execute the SQL query to retrieve all occupants from the occupants table
            cursor.execute("SELECT * FROM occupants")
            # Fetch all the results from the executed query
            occupants = cursor.fetchall()
            # Return the list of occupants
            return occupants
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to retrieve an occupant by their ID from the occupants table
            cursor.execute("SELECT * FROM occupants WHERE id = %s", (id,))
            # Fetch the result from the executed query
            occupant = cursor.fetchone()
            # Return the occupant object
            return Occupant(
                occupant[0],
                occupant[1],
                occupant[2],
                occupant[3],
                occupant[4],
                occupant[5],
                occupant[6],
                occupant[7],
                occupant[8],
            )
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def update(self, db, occupant):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to update an occupant in the occupants table
            cursor.execute(
                "UPDATE occupants SET user_id = %s, room_id = %s, start_date = %s, end_date = %s, guest_id = %s, name = %s WHERE id = %s",
                (
                    occupant.user_id,
                    occupant.room_id,
                    occupant.start_date,
                    occupant.end_date,
                    occupant.guest_id,
                    occupant.name,
                    occupant.id,
                ),
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
            # Execute the SQL query to delete an occupant from the occupants table by ID
            cursor.execute("DELETE FROM occupants WHERE id = %s", (id,))
            # Commit the transaction to save the changes in the database
            db.connection.commit()
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def get_by_room_id(self, db, room_id):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to retrieve an occupant by their room ID from the occupants table
            cursor.execute("SELECT * FROM occupants WHERE room_id = %s", (room_id,))
            # Fetch the result from the executed query
            occupants = cursor.fetchall()
            # Return the occupant object
            return occupants
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def get_by_user_id(self, db, user_id):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to retrieve an occupant by their user ID from the occupants table
            cursor.execute("SELECT * FROM occupants WHERE user_id = %s", (user_id,))
            # Fetch the result from the executed query
            occupants = cursor.fetchall()
            # Return the occupant object
            return occupants
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def get_by_guest_id(self, db, guest_id):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to retrieve an occupant by their guest ID from the occupants table
            cursor.execute("SELECT * FROM occupants WHERE guest_id = %s", (guest_id,))
            # Fetch the result from the executed query
            occupants = cursor.fetchall()
            # Return the occupant object
            return occupants
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def get_by_name(self, db, name):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to retrieve an occupant by their name from the occupants table
            cursor.execute("SELECT * FROM occupants WHERE name = %s", (name,))
            # Fetch the result from the executed query
            occupants = cursor.fetchall()
            # Return the occupant object
            return occupants
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)
