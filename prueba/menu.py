import os
import time
import funciones
import json
while True:
    print ("*******************************")
    print ("*   M U N D O  L I B R O 📚   *")
    print ("*******************************")
    print ()
    print ("[1] - Mantenedor de autores")
    print ("[2] - Reportes")
    print ("[3] - Salir")
    try:
        eleccion = int(input("Ingrese una opcion: "))
        os.system ("cls")
        if eleccion == 1 :
            
            
            print ("********************************")
            print ("*      Mantenedor Autores      *")
            print ("********************************")
            print ()
            print ("[1] - Agregar autor")
            print ("[2] - Editar autor")
            print ("[3] - Eliminar autor")
            print ("[4] - Buscar autor")
            print ("[5] - Volver")
            try:
                eleccion2 = int(input("Ingrese una opcion: "))
                if eleccion2 == 1:
                    funciones.agregarAutor()
                if eleccion2 == 2:
                    funciones.editarAutor
                if eleccion2 == 3:
                    funciones.eliminarAutor
                if eleccion2 == 4:
                    funciones.buscarAutor
                if eleccion2 == 5:
                    print("Volviendo...")
                    time.sleep(3)
                    os.system ("cls")
            except ValueError as e:
             print(f"Error: {e}. Por favor, ingrese un valor numérico válido.")      
        elif eleccion == 2:
            with open ("Reportes.json",mode="w") as archivojson:
                report:{
                    "IDautor",["AutorID"],
                    "Nombre",["Nombre"],
                    "Pais",["Nacionalidad"]

                }
                json.dump(report,archivojson,indent=4)
            with open("Reportes.json",mode="r") as archivojson:
                leerJson = json.load(archivojson)
                print(leerJson[report])
                for i in leerJson[report]:
                    print(i)
        
        elif eleccion == 3:
            print("Saliendo...")
            break
    except ValueError as e:
        print(f"Error: {e}. Por favor, ingrese un valor numérico válido.")        