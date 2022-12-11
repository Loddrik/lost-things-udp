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


class updateState(Service):
    def __init__(self):
        print("Servicio para marcar objeto como recuperado")
        super().__init__("blugu")
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

            x = db.query(Thing).get(thing_id)
            if(x.state == "recovered"):
                db.close()
                return str({
                    "error": "This object is already recovered"
                })

            x.state = "recovered"
            x.recoveredDate = datetime.datetime.now()
            var = db.query(Thing).filter(Thing.id == thing_id).first()
            varFinal = {
                "success": "Object recovered",
                "object": {
                    "id": var.id,
                    "name": var.name,
                    "description": var.description,
                    "state": var.state,
                    "meetingDate": var.meetingDate,
                    "recoveredDate": var.recoveredDate,
                    "publisehdDate": var.publishedDate,
                    "userId": var.userId,
                }
            }
            db.commit()
            db.close()
            return str(varFinal)

        except Exception as e:
            db.close()
            return str(e)


def main():
    try:
        updateState()
    except Exception as e:
        print(e)
        sleep(30)
        main()


if __name__ == "__main__":
    main()
