from Class.Client import Client
from getpass import getpass
import json
import datetime


def updateThing():
    print("Client: Update Thing")

    try:
        token = input("Ingrese token: ")
        print("Obteniendo lista de objetos ... \n")
        b = Client("blige")
        things = b.exec_client(debug=True, climsg=json.dumps({
            "token": token
        }))
        print(things, "\n")
        try:
            thing_id = input("Ingrese id del objeto: ")
            print("1. Modificar nombre")
            print("2. Modificar descripcion")
            opcion = input("Ingrese opcion: ")
            value = input("Ingrese nuevo valor: ")

            if opcion == "1":
                climsg = {
                    "thing_id": thing_id,
                    "token": token,
                    "name": value
                }
                a = Client("bloko")
                print("holaa")
                msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
                print("###################################\n\n",
                      msg, "\n\n###################################")
            elif opcion == "2":
                climsg = {
                    "thing_id": thing_id,
                    "token": token,
                    "description": value
                }
                a = Client("blugo")
                msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
                print("###################################\n\n",
                      msg, "\n\n###################################")
            else:
                print("Opcion invalida")
        except Exception as e:
            print("Error: ", e)

    except KeyboardInterrupt:
        print("\nCerrando cliente, hasta pronto ....")
        exit()
