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


class getPublicThings(Service):
    def __init__(self):
        print("Servicio publico para filtrar objetos por facultad y estado")
        super().__init__("blego")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()

        try:
            climsg = json.loads(climsg)
            state = climsg["state"]
            faculty = climsg["faculty"]

            result = db.query(Thing).join(User).filter(
                User.faculty == faculty).filter(Thing.state == state).all()

            arr = []
            for row in result:
                arr.append(to_dict(row))
            return str(arr)

        except Exception as e:
            db.close()
            return str(e)


def main():
    try:
        getPublicThings()
    except Exception as e:
        print(e)
        sleep(30)
        main()


if __name__ == "__main__":
    main()
