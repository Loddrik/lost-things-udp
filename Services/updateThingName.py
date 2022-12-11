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


class updateThingName(Service):
    def __init__(self):
        print("Servicio para modificar nombre de objeto")
        super().__init__("bloko")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()

        try:
            climsg = json.loads(climsg)
            token = climsg["token"]
            decoded_token = jwt.decode(
                token, os.environ['SECRET_KEY'], algorithms=['HS256'])
            thing_id = climsg["thing_id"]
            name = climsg["name"]

            x = db.query(Thing).get(thing_id)
            x.name = name
            obj = db.query(Thing).filter(Thing.id == thing_id).first()
            varFinal = {
                "success": "Object modified",
                "object": {
                    "id": obj.id,
                    "name": obj.name,
                    "description": obj.description,
                    "state": obj.state,
                    "meeting_date": obj.meetingDate,
                    "published_date": obj.publishedDate,
                    "recovered_date": obj.recoveredDate,
                }
            }
            db.commit()
            db.close()
            return str({
                "success": "Object modified",
            })

        except Exception as e:
            db.close()
            return str({
                "error": "Error: " + str(e)
            })


def main():
    try:
        updateThingName()
    except Exception as e:
        print(e)
        sleep(30)
        main()


if __name__ == "__main__":
    main()
