from Class.Client import Client
from getpass import getpass
import json
import datetime


def getThings():
    print("Service: Get Things")

    try:
        token = input("Ingrese token: ")
        try:
            climsg = {
                "token": token,
            }
            a = Client("blige")
            msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
            print("###################################\n\n",
                  msg, "\n\n###################################")
        except Exception as e:
            print("Error: ", e)

    except KeyboardInterrupt:
        print("\nCerrando cliente, hasta pronto ....")
        exit()
