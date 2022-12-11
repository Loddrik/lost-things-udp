from Class.Client import Client
from getpass import getpass
import json


def login():
    print("Service: Login")

    try:
        email = input("Ingrese email: ")
        password = getpass("Ingrese contraseña: ")

        try:
            climsg = {
                "email": email,
                "password": password
            }
            a = Client("blogi")
            msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
            print("###################################\n\n",
                  msg, "\n\n###################################")
        except Exception as e:
            print("Error: ", e)

    except KeyboardInterrupt:
        print("\nCerrando cliente, hasta pronto ....")
        exit()
