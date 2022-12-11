from Class.Client import Client
from getpass import getpass
import json
import datetime

if __name__ == "__main__":
    print("Service: Get Things")
    keep_alive = True

    try:
        while(keep_alive):
            token = input("Ingrese token: ")
            print("Ingrese la opcion deseada: \n",
                  "1. Obtener todos los objetos\n",
                  "2. Obtener todos los objetos perdidos\n",
                  "3. Obtener todos los objetos encontrados\n",
                  "4. Obtener todos los objetos recuperados\n",)
            option = input("Ingrese su opción: ")
            try:
                climsg = {
                    "token": token,
                    "option": option
                }
                a = Client("blogo")
                msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
                print("###################################\n\n",
                      msg, "\n\n###################################")
            except Exception as e:
                print("Error: ", e)

    except KeyboardInterrupt:
        print("\nCerrando cliente, hasta pronto ....")
        keep_alive = False
        exit()
