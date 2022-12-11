from Class.Service import Service
from Database.session import session
from Database.models import User
import bcrypt
import json
import os
import jwt
import datetime
from time import sleep


class Registro(Service):
    def __init__(self):
        print("Servicio de registro de usuarios")
        super().__init__("bregi")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()
        try:
            climsg = json.loads(climsg)
            email = climsg["email"]
            password = climsg["password"]
            faculty = climsg["faculty"]
            if not db.query(User).filter(User.email == email).first():
                salt = bcrypt.gensalt()
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
                usuario = User(
                    id=os.urandom(16).hex(),
                    email=email,
                    password=hashed_password.decode('utf-8'),
                    faculty=faculty,
                    addres=climsg["address"],
                )
                var = {
                    'id': usuario.id,
                    'email': usuario.email,
                    'facultad': usuario.faculty,
                }
                db.add(usuario)
                db.commit()
                db.close()
                return str(var)
            else:
                db.close()
                return "Usuario ya existe"
        except Exception as e:
            db.close()
            return str(e)


def main():
    try:
        Registro()
    except Exception as e:
        print(e)
        sleep(30)
        main()


if __name__ == "__main__":
    main()
