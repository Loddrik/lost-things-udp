import cliAddThing
import cliUpdateThing
import cliDeleteThing
import cliGetThings
import cliUpdateState
import clilogin
import cliGetFilteredThings
import cliGetAllThings
import time
import cliregister

if __name__ == "__main__":
    print("Public Service: Get All Lost and Found Things")

    keep_alive = True

    while keep_alive:
        time.sleep(2.4)
        print("#################### MENU #################### \n\n")
        print("AUTH SERVICES:\n")
        print("1. Añadir objeto.")
        print("2. Actualizar objeto.")
        print("3. Eliminar objeto.")
        print("4. Marcar Objeto como recuperado.")
        print("5. Obtener objetos del usuario actual.\n")
        print("--------------------------------------------------")
        print("PUBLIC SERVICES:")
        print("6. Iniciar sesión.")
        print("7. Obtener objetos usando filtros.")
        print("8. Obtener todos los objetos encontrados y perdidos.")

        option = input("Ingrese una opción:")

        if option == "1":
            try:
                cliAddThing.addThing()
            except:
                print("Error: ", e)
        elif option == "2":
            try:
                cliUpdateThing.updateThing()
            except:
                print("Error: ", e)
        elif option == "3":
            try:
                cliDeleteThing.deleteThing()
            except:
                print("Error: ", e)
        elif option == "4":
            try:
                cliUpdateState.updateState()
            except:
                print("Error: ", e)
        elif option == "5":
            try:
                cliGetThings.getThings()
            except:
                print("Error: ", e)
        elif option == "6":
            try:
                clilogin.login()
            except:
                print("Error: ", e)
        elif option == "7":
            try:
                cliGetFilteredThings.getFilteredThings()
            except:
                print("Error: ", e)
        elif option == "8":
            try:
                cliGetAllThings.getAllThings()
            except:
                print("Error: ", e)
        elif option == "9":
            try:
                cliregister.register()
            except:
                print("Error: ", e)
