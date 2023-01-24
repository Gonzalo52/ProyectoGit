def eliminar_Contacto():
    nombre = input("ingresa el nombre del contacto: ")
    apellido = input("ingresa el apellido del contacto: ")
    esta = False
    for i in contactos:
        if nombre == i['nombre'] and apellido == i['apellido']:
            contactos.remove(i)
            print()
            esta = True
            return llamar_menu()
    if esta == False:
            print("\nel contacto no existe")
            return llamar_menu()