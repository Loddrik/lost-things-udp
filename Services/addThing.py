from Class.Service import Service
from Database.session import session
from Database.models import Thing
import bcrypt
import os
import json
import jwt
import datetime
from time import sleep
import uuid


class addThing(Service):
    def __init__(self):
        print("Servicio para añadir objetos")
        super().__init__("bligi")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()

        try:
            climsg = json.loads(climsg)
            token = climsg["token"]
            decoded_token = jwt.decode(
                token, os.environ['SECRET_KEY'], algorithms=['HS256'])

            name = climsg["name"]
            state = climsg["state"]
            description = climsg["description"]
            meeting_date = climsg["meeting_date"]
            object = Thing(
                id=uuid.uuid4(),
                userId=decoded_token["id"],
                name=name,
                state=state,
                description=description,
                meetingDate=datetime.datetime.strptime(
                    meeting_date, "%Y-%m-%d %H:%M:%S"),
                publishedDate=datetime.datetime.utcnow()
            )

            db.add(object)
            var = {
                "id": object.id,
                "userId": object.userId,
                "name": object.name,
                "state": object.state,
                "description": object.description,
                "meetingDate": object.meetingDate,
                "publishedDate": object.publishedDate
            }

            db.commit()
            db.close()
            return str(var)

        except Exception as e:
            db.close()
            return str(e)


def main():
    try:
        addThing()
    except Exception as e:
        print(e)
        sleep(30)
        main()


if __name__ == "__main__":
    main()
