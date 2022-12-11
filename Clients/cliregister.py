from Class.Client import Client
from getpass import getpass
import json


def register():
    print("Service: Registro")
    try:
        email = input("Ingrese email: ")
        password = getpass("Ingrese contraseña: ")
        faculty = input("Ingrese facultad: ")
        address = input("Ingrese dirección: ")
        try:
            climsg = {
                "email": email,
                "password": password,
                "faculty": faculty,
                "address": address,
            }
            a = Client("bregi")
            msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
            print("###################################\n\n",
                  msg, "\n\n###################################")
        except Exception as e:
            print("Error: ", e)
    except KeyboardInterrupt:
        print("\nCerrando cliente, hasta pronto ....")
        exit()
