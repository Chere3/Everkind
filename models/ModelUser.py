from models.entities.User import User


class ModelUser:

    @classmethod
    def signin(self, db, usuario):
        try:
            # Get the user info from the form
            selectedUser = db.connection.cursor()
            selectedUser.execute(
                "SELECT * FROM usuarios WHERE correo = %s", (usuario.correo,)
            )
            u = selectedUser.fetchone()
            # Check if user already exists
            if u is not None:
                return User(
                    u[0], u[1], u[2], User.validarClave(u[3], usuario.clave), u[4], u[5]
                )
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    # Get the user by his id
    @classmethod
    def get_by_id(self, db, id):
        try:
            selectedUser = db.connection.cursor()
            selectedUser.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
            u = selectedUser.fetchone()

            # If the user exists, return it
            if u is not None:
                return User(u[0], u[1], u[2], u[3], u[4], u[5])
            else:
                # If the user does not exist, return None
                return None

        # If an error occurs, raise an exception on the console
        except Exception as ex:
            raise Exception(ex)
