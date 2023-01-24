def editar_Contacto():
    nombre = input("ingresa el nombre del contacto: ")
    apellido = input("ingresa el apellido del contacto: ")
    esta = False
    for x in contactos:
        if nombre == x['nombre'] and apellido == x['apellido']:
            elige = input("\nque quieres editar? \nnombre apellido numero :")
            while elige == "nombre" or "apellido" or "numero":
                if elige == "nombre":
                    nombre1 = input("ingresa el nombre del contacto: ")
                    x['nombre'] = nombre1
                    print("\nel contacto se edito correctamente\n")
                    esta = True
                    return llamar_menu()
                if elige == "apellido": 
                    apellido1 = input("ingresa el apellido del contacto: ")   
                    x['apellido'] = apellido1
                    print("\nel contacto se edito correctamente\n")
                    esta = True
                    return llamar_menu()
                if elige == "numero":
                    numero1 = input("ingresa el numero correcto: ")
                    x['numero'] = numero1
                    print("\nel contacto se edito correctamente\n")
                    esta = True
                    return llamar_menu()    
                else:
                    print("seleccione una opcion correcta")
                    elige = input("\nque quieres editar? \nnombre apellido numero :")