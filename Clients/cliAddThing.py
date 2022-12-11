from Class.Client import Client
from getpass import getpass
import json
import datetime


def addThing():
    print("Service: Add Thing")

    try:
        name = input("Ingrese nombre: ")
        state = input("Ingrese estado (lost, found): ")
        if state != "lost" and state != "found":
            print("Estado no válido")
            exit()
        description = input("Ingrese descripcion: ")
        meeting_date = input("Ingrese fecha de encuentro: ")
        token = input("Ingrese token: ")
        try:
            climsg = {
                "name": name,
                "state": state,
                "description": description,
                "meeting_date": meeting_date,
                "token": token
            }
            a = Client("bligi")
            msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
            print("###################################\n\n",
                  msg, "\n\n###################################")
        except Exception as e:
            print("Error: ", e)

    except KeyboardInterrupt:
        print("\nCerrando cliente, hasta pronto ....")
        exit()
