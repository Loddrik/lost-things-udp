from Class.Service import Service
from Database.session import session
from Database.models import User
import bcrypt
import os
import json
import jwt
import datetime
from time import sleep


class Login(Service):
    def __init__(self):
        print("Servicio de login de vendedores")
        super().__init__("blogi")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()

        try:
            climsg = json.loads(climsg)
            email = climsg["email"]
            password = climsg["password"]
            user = db.query(User).filter(
                User.email == email).first()

            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                token = jwt.encode({
                    'id': user.id,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
                }, os.environ['SECRET_KEY'])
                return token
            else:
                db.close()
                return "Contraseña incorrecta"
        except Exception as e:
            db.close()
            return str(e)


def main():
    try:
        Login()
    except Exception as e:
        print(e)
        sleep(30)
        main()


if __name__ == "__main__":
    main()
