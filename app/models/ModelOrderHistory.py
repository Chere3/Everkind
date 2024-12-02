from app.models.entities.OrderHistory import OrderHistory


class ModelOrderHistory:
    """
    A class representing an order history model.
    Methods:
    - create(db, order_history): Create a new order history.
    - get_all(db): Get all order histories.
    - get_by_id(db, id): Get an order history by ID.
    - update(db, order_history): Update an existing order history.
    - delete(db, id): Delete an order history.
    - get_by_user_id(db, user_id): Get all order histories by user ID.
    """

    @classmethod
    def create(self, db, order_history):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to insert a new order history into the order_history table
            cursor.execute(
                "INSERT INTO order_history (user_id, occupant_id, visit_id, order_id, action, action_date) VALUES (%s, %s, %s, %s, %s, %s)",
                (
                    order_history.user_id,
                    order_history.occupant_id,
                    order_history.visit_id,
                    order_history.order_id,
                    order_history.action,
                    order_history.action_date,
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
            # Execute the SQL query to retrieve all order histories from the order_history table
            cursor.execute("SELECT * FROM order_history")
            # Fetch all the results from the executed query
            order_history = cursor.fetchall()
            # Return the list of order histories
            return order_history
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to retrieve an order history by its ID from the order_history table
            cursor.execute("SELECT * FROM order_history WHERE id = %s", (id,))
            # Fetch the result from the executed query
            order_history = cursor.fetchone()
            # Return the order history
            return order_history
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def update(self, db, order_history):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to update an existing order history in the order_history table
            cursor.execute(
                "UPDATE order_history SET user_id = %s, occupant_id = %s, visit_id = %s, order_id = %s, action = %s, action_date = %s WHERE id = %s",
                (
                    order_history.user_id,
                    order_history.occupant_id,
                    order_history.visit_id,
                    order_history.order_id,
                    order_history.action,
                    order_history.action_date,
                    order_history.id,
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
            # Execute the SQL query to delete an order history by its ID from the order_history table
            cursor.execute("DELETE FROM order_history WHERE id = %s", (id,))
            # Commit the transaction to save the changes in the database
            db.connection.commit()
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)

    @classmethod
    def get_by_user_id(self, db, user_id):
        try:
            # Get the cursor from the database connection
            cursor = db.connection.cursor()
            # Execute the SQL query to retrieve all order histories by user ID from the order_history table
            cursor.execute("SELECT * FROM order_history WHERE user_id = %s", (user_id,))
            # Fetch all the results from the executed query
            order_history = cursor.fetchall()
            # Return the list of order histories
            return order_history
        except Exception as ex:
            # Raise an exception if any error occurs
            raise Exception(ex)
