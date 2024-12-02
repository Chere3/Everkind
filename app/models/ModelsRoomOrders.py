from app.models.entities.RoomOrders import RoomOrders


class RoomOrdersModel:
    """
    A class representing a room orders model.
    Methods:
    - create(db, room_order): Create a new room order.
    - get_all(db): Get all room orders.
    - get_by_id(db, id): Get a room order by ID.
    - update(db, room_order): Update an existing room order.
    - delete(db, id): Delete a room order.
    """

    @classmethod
    def create(self, db, room_order):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to insert a new room order into the room_orders table
            cursor.execute(
                "INSERT INTO room_orders (user_id, room_id, order_date, status) VALUES (%s, %s, %s, %s)",
                (
                    room_order.user_id,
                    room_order.room_id,
                    room_order.order_date,
                    room_order.status,
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
            # Execute the SQL query to retrieve all room orders from the room_orders table
            cursor.execute("SELECT * FROM room_orders")
            # Fetch all the results from the executed query
            room_orders = cursor.fetchall()
            # Return the list of room orders
            return room_orders
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to retrieve a room order by its ID from the room_orders table
            cursor.execute("SELECT * FROM room_orders WHERE id = %s", (id,))
            # Fetch the result from the executed query
            room_order = cursor.fetchone()
            # Return the room order
            return room_order
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def update(self, db, room_order):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to update an existing room order in the room_orders table
            cursor.execute(
                "UPDATE room_orders SET room_id = %s, order_date = %s, status = %s WHERE id = %s",
                (
                    room_order.room_id,
                    room_order.order_date,
                    room_order.status,
                    room_order.id,
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
            # Execute the SQL query to delete a room order by its ID from the room_orders table
            cursor.execute("DELETE FROM room_orders WHERE id = %s", (id,))
            # Commit the transaction to save the changes in the database
            db.connection.commit()
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def get_last_by_user_id(self, db, user_id):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to retrieve a room order by its ID from the room_orders table
            cursor.execute(
                "SELECT * FROM room_orders WHERE user_id = %s ORDER BY id DESC LIMIT 1",
                (user_id,),
            )
            # Fetch the result from the executed query
            room_order = cursor.fetchone()
            # Return the room order
            return room_order
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)
