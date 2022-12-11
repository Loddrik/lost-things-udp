from Class.Client import Client
from getpass import getpass
import json
import datetime


def getFilteredThings():
    print("Service: Filter Things by faculty and state")

    try:

        state = input(
            "Ingrese el estado del objeto (lost,found): ")
        faculty = input("Ingrese la facultad del objeto: ")
        if state != "lost" and state != "found":
            print("Estado no válido, intente nuevamente")
            pass

        try:
            climsg = {
                "state": state,
                "faculty": faculty
            }
            a = Client("blego")
            msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
            print("###################################\n\n",
                  msg, "\n\n###################################")
        except Exception as e:
            print("Error: ", e)

    except KeyboardInterrupt:
        print("\nCerrando cliente, hasta pronto ....")
        exit()
