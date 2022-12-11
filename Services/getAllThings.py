from Class.Service import Service
from Database.session import session
from Database.models import Thing, to_dict, User
import bcrypt
import os
import json
import jwt
import datetime
from time import sleep
import uuid


class getAllThings(Service):
    def __init__(self):
        print("Servicio para obtener todos los objetos de manera publica")
        super().__init__("gatpo")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()

        try:
            climsg = json.loads(climsg)

            result = db.query(Thing).filter(
                Thing.state != "recovered").all()

            arr = []
            for row in result:
                arr.append(to_dict(row))
            return str(arr)

        except Exception as e:
            db.close()
            return str(e)


def main():
    try:
        getAllThings()
    except Exception as e:
        print(e)
        sleep(30)
        main()


if __name__ == "__main__":
    main()
