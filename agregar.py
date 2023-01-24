def agregar_Contactos():
    nuevo = {
        'nombre': input("ingresa el nombre del contacto: "),
        'apellido': input("ingresa el apellido del contacto: "),
        'numero': int(input("ingresa el numero del contacto: "))
    }
    contactos.append(nuevo)
    print("\ncontacto guardado correctamente\n")
    return llamar_menu()