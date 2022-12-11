from Class.Client import Client
from getpass import getpass
import json
import datetime


def getAllThings():
    print("Public Service: Get All Lost and Found Things")

    try:

        a = Client("gatpo")
        msg = a.exec_client(debug=True, climsg=json.dumps({}))
        print("###################################\n\n",
              msg, "\n\n###################################")

    except KeyboardInterrupt:
        exit()
