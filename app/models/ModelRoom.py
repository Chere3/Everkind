from app.models.ModelsRoomOrders import RoomOrdersModel
import app.models.entities.Room as Room
import app.models.entities.RoomType as RoomType
import app.models.ModelRoomType as ModelRoomType
import app.models.entities.Occupant as Occupant
import app.models.ModelOccupant as ModelOccupant
import app.models.entities.RoomOrders as RoomOrders
import app.models.ModelOrderHistory as ModelOrderHistory
import app.models.entities.OrderHistory as OrderHistory
from app.models.entities.PartialRoom import PartialRoom
import datetime


class ModelRoom:
    """
    A class representing a room model.
    Methods:
    - create(db, room): Create a new room.
    - get_all(db): Get all rooms.
    - get_by_id(db, id): Get a room by ID.
    - update(db, room): Update an existing room.
    - delete(db, id): Delete a room.
    - book_room(db, room_id, user_id, order_date, status): Book a room.
    - cancel_room(db, room_id, user_id, order_date, status): Cancel a room.
    - get_by_user_id(db, user_id): Get all rooms by user ID.
    """

    @classmethod
    def create(self, db, room, type):
        try:
            # Make the objects
            partialRoom = PartialRoom(
                room.id,
                room.room_number,
                room.capacity,
                room.created_at,
                room.updated_at,
                room.room_type_id,
                room.room_type_photo,
            )
            roomType = RoomType.RoomType(
                type.id, type.type_name, type.description, type.photo
            )
            room = Room.Room(partialRoom, roomType)

            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to insert a new room into the rooms table
            cursor.execute(
                "INSERT INTO rooms (room_number, capacity, room_type_id, room_type_photo) VALUES (%s, %s, %s, %s)",
                (
                    partialRoom.room_number,
                    partialRoom.capacity,
                    partialRoom.room_type_id,
                    partialRoom.room_type_photo,
                ),
            )
            # Commit the transaction to save the changes in the database
            db.connection.commit()

            return room
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def get_all(self, db):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to retrieve all rooms from the rooms table and the room types from the room_types table
            cursor.execute(
                "SELECT * FROM rooms JOIN room_types ON rooms.room_type_id = room_types.id"
            )
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
            # Execute the SQL query to retrieve a room by its ID from the rooms table and get the room type from the room_types table
            cursor.execute(
                "SELECT * FROM rooms JOIN room_types ON rooms.room_type_id = room_types.id WHERE rooms.id = %s",
                (id,),
            )
            # Fetch the result from the executed query
            room = cursor.fetchone()
            # Return the room
            return room
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def update(self, db, room, type):
        try:
            # Make the objects
            partialRoom = PartialRoom(
                room.id,
                room.room_number,
                room.capacity,
                room.created_at,
                room.updated_at,
                room.room_type_id,
                room.room_type_photo,
            )
            roomType = RoomType.RoomType(
                type.id, type.type_name, type.description, type.photo
            )
            room = Room.Room(partialRoom, roomType)

            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to update an existing room in the rooms table
            cursor.execute(
                "UPDATE rooms SET room_number = %s, capacity = %s, room_type_id = %s, room_type_photo = %s WHERE id = %s",
                (
                    partialRoom.room_number,
                    partialRoom.capacity,
                    partialRoom.room_type_id,
                    partialRoom.room_type_photo,
                    partialRoom.id,
                ),
            )
            # Commit the transaction to save the changes in the database
            db.connection.commit()

            # Execute the SQL query to update an existing room type in the room_types table
            cursor.execute(
                "UPDATE room_types SET type_name = %s, description = %s, photo = %s WHERE id = %s",
                (
                    roomType.type_name,
                    roomType.description,
                    roomType.photo,
                    roomType.id,
                ),
            )

            # Commit the transaction to save the changes in the database
            db.connection.commit()

            return room
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def delete(self, db, id):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to delete a room from the rooms table by ID
            cursor.execute("DELETE FROM rooms WHERE id = %s", (id,))
            # Commit the transaction to save the changes in the database
            db.connection.commit()
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def book_room(self, db, room_id, user_id, order_date, status):
        try:
            # Update the room at occupant table
            occupant = ModelOccupant.ModelOccupant.get_by_user_id(db, user_id)[0]
            print(occupant)
            occupant = Occupant.Occupant(
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

            ModelOccupant.ModelOccupant.update(
                db,
                Occupant.Occupant(
                    occupant.id,
                    occupant.user_id,
                    room_id,
                    datetime.datetime.now(),
                    None,
                    occupant.created_at,
                    datetime.datetime.now(),
                    occupant.guest_id,
                    occupant.name,
                ),
            )

            # Make a new room order
            room_order = RoomOrdersModel.create(
                db,
                RoomOrders.RoomOrders(
                    0,
                    user_id,
                    room_id,
                    order_date,
                    status,
                    datetime.datetime.now(),
                    datetime.datetime.now(),
                ),
            )

            room_order = RoomOrdersModel.get_last_by_user_id(db, user_id)

            print(room_order)

            # Make a new order in order history
            ModelOrderHistory.ModelOrderHistory.create(
                db,
                OrderHistory.OrderHistory(
                    user_id,
                    occupant.id,
                    None,
                    room_order[0],
                    "booked",
                    room_order[6],
                    datetime.datetime.now(),
                    datetime.datetime.now(),
                ),
            )

        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def cancel_room(self, db, room_id, user_id, order_date, status):
        try:
            # Update the room at occupant table
            occupant = ModelOccupant.ModelOccupant.get_by_user_id(db, user_id)[0]
            occupant = Occupant.Occupant(
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

            ModelOccupant.ModelOccupant.update(
                db,
                Occupant.Occupant(
                    occupant.id,
                    occupant.user_id,
                    None,
                    None,
                    datetime.datetime.now(),
                    occupant.created_at,
                    datetime.datetime.now(),
                    occupant.guest_id,
                    occupant.name,
                ),
            )

            # Make a new room order
            room_order = RoomOrdersModel.create(
                db,
                RoomOrders.RoomOrders(
                    0,
                    user_id,
                    room_id,
                    order_date,
                    status,
                    datetime.datetime.now(),
                    datetime.datetime.now(),
                ),
            )

            room_order = RoomOrdersModel.get_last_by_user_id(db, user_id)

            # Make a new order in order history
            ModelOrderHistory.ModelOrderHistory.create(
                db,
                OrderHistory.OrderHistory(
                    user_id,
                    occupant.id,
                    None,
                    room_order[0],
                    "cancelled",
                    room_order[6],
                    datetime.datetime.now(),
                    datetime.datetime.now(),
                ),
            )

        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def get_by_user_id(self, db, user_id):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to retrieve all rooms by user ID from the rooms table and the room types from the room_types table
            cursor.execute(
                "SELECT * FROM rooms JOIN room_types ON rooms.room_type_id = room_types.id WHERE rooms.id IN (SELECT room_id FROM occupants WHERE user_id = %s)",
                (user_id,),
            )
            # Fetch all the results from the executed query
            rooms = cursor.fetchall()
            # Return the list of rooms
            return rooms
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)
