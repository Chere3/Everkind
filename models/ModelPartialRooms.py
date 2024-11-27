from models.entities import RoomType
from models.entities.PartialRoom import PartialRoom


class ModelPartialRooms:
    """
    A class representing a room model.
    Methods:
    - create(db, room): Create a new room.
    - get_all(db): Get all rooms.
    - get_by_id(db, id): Get a room by ID.
    - update(db, room): Update an existing room.
    - delete(db, id): Delete a room.
    """

    @classmethod
    def create(self, db, room):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to insert a new room into the rooms table
            cursor.execute(
                "INSERT INTO rooms (name, room_number, capacity, room_type_id, room_type_photo) VALUES (%s, %s, %s, %s, %s)",
                (
                    room.name,
                    room.room_number,
                    room.capacity,
                    room.room_type_id,
                    room.room_type_photo,
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
            # Execute the SQL query to retrieve all rooms from the rooms table
            cursor.execute("SELECT * FROM rooms")
            # Fetch all the results from the executed query
            rooms = cursor.fetchall()
            # Return the list of rooms
            return rooms
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to retrieve a room by its ID from the rooms table
            cursor.execute("SELECT * FROM rooms WHERE id = %s", (id,))
            # Fetch the result from the executed query
            room = cursor.fetchone()
            # Return the room
            return room
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def update(self, db, room):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to update an existing room in the rooms table
            cursor.execute(
                "UPDATE rooms SET name = %s, room_number = %s, capacity = %s, room_type_id = %s, room_type_photo = %s WHERE id = %s",
                (
                    room.name,
                    room.room_number,
                    room.capacity,
                    room.room_type_id,
                    room.room_type_photo,
                    room.id,
                ),
            )
            # Commit the transaction to save the changes in the database
            db.connection.commit()
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def delete(self, db, room_id):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to delete a room by its ID from the rooms table
            cursor.execute("DELETE FROM rooms WHERE id = %s", (room_id,))
            # Commit the transaction to save the changes in the database
            db.connection.commit()
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def get_all_rooms_with_type(self, db):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to retrieve all rooms and their types from the rooms table and room_types table
            cursor.execute(
                "SELECT * FROM rooms JOIN room_types ON rooms.room_type_id = room_types.id"
            )
            # Fetch all the results from the executed query
            rooms = cursor.fetchall()

            # Create a list of Room objects
            room_list = []
            for room in rooms:
                room_list.append(
                    PartialRoom(
                        room["id"],
                        room["room_number"],
                        room["capacity"],
                        room["created_at"],
                        room["updated_at"],
                        room["room_type_id"],
                        room["room_type_photo"],
                    ),
                    RoomType(
                        room["id"],
                        room["type_name"],
                        room["description"],
                        room["photo"],
                        room["created_at"],
                        room["updated_at"],
                    ),
                )

            # Return the list of rooms
            return room_list
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)
