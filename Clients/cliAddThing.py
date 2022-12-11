from Class.Client import Client
from getpass import getpass
import json
import datetime

if __name__ == "__main__":
    print("Service: Add Thing")
    keep_alive = True

    try:
        while(keep_alive):
            name = input("Ingrese nombre: ")
            state = input("Ingrese estado (lost, found, recovered): ")
            if state != "lost" and state != "found" and state != "recovered":
                print("Estado no válido")
                continue
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
        keep_alive = False
        exit()
