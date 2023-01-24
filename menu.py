menu = ['Ver la lista de contactos[ver]', 'Buscar un contacto[buscar]', 'Agregar un contactos[agregar]',
 'Eliminar un contacto[eliminar]', 'Editar contacto[editar]']

def ver_Contactos():
    print("\nlos contactos son: \n")
    print(contactos)
    return llamar_menu()

def buscar_Contactos():
    nombre1 = input("ingresa el nombre del contacto: ")
    apellido1 = input("ingresa el apellido del contacto: ")
    esta = False
    for i in contactos:
        if (i['nombre'] == nombre1 and i['apellido'] == apellido1):
            print("\n")
            print("nombre: ", i['nombre'])
            print("apellido: ", i['apellido'])
            print("numero: ", i['numero'])
            print("\n")
            esta = True
    if esta == False: 
            print("\nel contacto no existe")
    return llamar_menu()

def mostrar_menu():
    for i in menu:
        print(i)

 def elegir_opcion():
    elige = input("\ningresa una opcion: ")
    while elige == "ver" or "buscar" or "agregar" or "eliminar" or "editar":
        if elige == "ver":
            return ver_Contactos()
        if elige == "buscar":
            return buscar_Contactos()
        if elige == "agregar":
            return agregar_Contactos()
        if elige == "eliminar":
            return eliminar_Contacto()
        if elige == "editar":
            return editar_Contacto()
        else:
            print("\nno eligio una opcion correcta\n")
            return llamar_menu()

def llamar_menu():
    print("\nopciones: \n")
    mostrar_menu()
    elegir_opcion()

contactos = []

llamar_menu()