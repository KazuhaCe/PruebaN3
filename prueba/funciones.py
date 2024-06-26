import json

def abrirCarpeta():
    with open("bliblioteca.json",mode="r") as Carpeta:
        datos = json.read(Carpeta)
        return datos

def agregarAutor(datos):
    IDAutor = int(input("Ingrese el ID del autor que quiere agregar:"))
    NombreAutor = int(input("Ingrese el ID del autor que quiere agregar:"))
    PaisAutor = int(input("Ingrese el ID del autor que quiere agregar:"))
    autor = {
        "IDautor" : IDAutor,
        "NombreAutor" : NombreAutor,
        "PaisAutor" : PaisAutor
    }
    with open("bliblioteca.json",mode="w"):
        json.dump(autor)

def editarAutor():
    print()
    
def eliminarAutor():
    print()

def buscarAutor(datos):
    buscautor = int(input("Ingrese la ID del autor que desea buscar"))
    for i in datos:
        if buscautor == ["AutorID"]:
            print("Se ha encontrado el autor")
        else:
            print("No se ha encontrado el autor")

