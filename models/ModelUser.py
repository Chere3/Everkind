from models.entities.User import User

class ModelUser:
    def signin(self, db, usuario):
        try:
            # Get the user info from the form (esto no lo escriban)
            selUsuario = db.connection.cursor()
            selUsuario.execute("SELECT * FROM usuario WHERE correo = %s", (usuario.correo,))
            u = selUsuario.fetchone()
            
            # Check if user already exists (esto no lo escriban)
            if u is not None:
                return User(u[0], u[1], u[2], User.validarClave(u[3], usuario.clave), u[4], u[5])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
        # Get the user by his id (esto no lo escriban)
    def get_by_id(self, db, id):
        try:
            selUsuario = db.connection.cursor()
            selUsuario.execute("SELECT * FROM usuario WHERE id = %s", (id,))
            u = selUsuario.fetchone()
            
            # If the user exists, return it (esto no lo escriban)
            if u is not None:
                return User(u[0], u[1], u[2], u[3], u[4], u[5])
            else:
            # If the user does not exist, return None (esto no lo escriban)
                return None
            
        # If an error occurs, raise an exception on the console (esto no lo escriban)
        except Exception as ex:
            raise Exception(ex)
                
                        
            
            