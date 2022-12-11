from Class.Service import Service
from Database.session import session
from Database.models import Thing, to_dict
import bcrypt
import os
import json
import jwt
import datetime
from time import sleep
import uuid


class getThings(Service):
    def __init__(self):
        print("Servicio para obtener objetos perdidos y encontrados del admin")
        super().__init__("blogo")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()

        try:
            climsg = json.loads(climsg)
            token = climsg["token"]
            decoded_token = jwt.decode(
                token, os.environ['SECRET_KEY'], algorithms=['HS256'])

            objects = db.query(Thing).filter(
                Thing.userId == decoded_token["id"]).filter(Thing.state != "recovered").all()
            arr = []
            for row in objects:
                arr.append(to_dict(row))
            return str(arr)

        except Exception as e:
            db.close()
            return str(e)


def main():
    try:
        getThings()()
    except Exception as e:
        print(e)
        sleep(30)
        main()


if __name__ == "__main__":
    main()
