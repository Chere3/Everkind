from app.models.entities.RoomType import RoomType


class ModelRoomType:
    """
    A class representing a room type model.
    Methods:
    - create(db, room_type): Create a new room type.
    - get_all(db): Get all room types.
    - get_by_id(db, id): Get a room type by ID.
    - update(db, room_type): Update an existing room type.
    - delete(db, id): Delete a room type.
    """

    @classmethod
    def create(self, db, room_type):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to insert a new room type into the room_types table
            cursor.execute(
                "INSERT INTO room_types (type_name, description, photo) VALUES (%s, %s, %s)",
                (
                    room_type.type_name,
                    room_type.description,
                    room_type.photo,
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
            # Execute the SQL query to retrieve all room types from the room_types table
            cursor.execute("SELECT * FROM room_types")
            # Fetch all the results from the executed query
            room_types = cursor.fetchall()
            # Return the list of room types
            return room_types
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to retrieve a room type by its ID from the room_types table
            cursor.execute("SELECT * FROM room_types WHERE id = %s", (id,))
            # Fetch the result from the executed query
            room_type = cursor.fetchone()
            # Return the room type
            return room_type

        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def update(self, db, room_type):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query
            cursor.execute(
                "UPDATE room_types SET type_name = %s, description = %s, photo = %s WHERE id = %s",
                (
                    room_type.type_name,
                    room_type.description,
                    room_type.photo,
                    room_type.id,
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
            # Execute the SQL query to delete a room type by its ID from the room_types table
            cursor.execute("DELETE FROM room_types WHERE id = %s", (id,))
            # Commit the transaction to save the changes in the database
            db.connection.commit()
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)
