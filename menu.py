menu = ['Ver la lista de contactos[ver]', 'Buscar un contacto[buscar]', 'Agregar un contactos[agregar]',
 'Eliminar un contacto[eliminar]', 'Editar contacto[editar]']

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

