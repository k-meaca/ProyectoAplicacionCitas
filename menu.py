def menu_ppal():

    # En esta funcion se encuentra el menu principal. Desde aca se cargarán los datos y se podrá
    # acceder al sistema

    datos_prueba = open("usuarios.csv","r+")
    usuarios_binario = open("usuarios_nuevos.pkl","rb+")
    mensajeria = open("mensajeria.pkl", "rb+")
    matches_y_likes = open("likes.pkl","rb+")

    import pickle

    from usuarios_X_pantalla import imprimir_usuarios
    from archivos_a_dicc import creando_diccionario
    from datos import cargar_datos
    from sistema import ingresar_sistema
    from likes_y_msj import cargar_diccionario
    from likes_y_msj import cargar_en_archivo

    en_menu = True
    se_cargo_en_pickle = False
    mostrar_usuarios = '1'
    nueva_cuenta = '2'
    ingreso_sistema = '3'
    terminar_programa = '0'
    top5 = '5'
    correspondencia = {}
    valores = []
    pseudonimo = ''


    usuarios = creando_diccionario(datos_prueba,usuarios_binario)
    correspondencia = cargar_diccionario(mensajeria,matches_y_likes,correspondencia)

    print("BIENVENIDO A TINDER")

    while en_menu:
        print("\n[1]Imprimir usuarios")
        print("[2]Crear una nueva cuenta")
        print("[3]Ingresar al sistema")
        print("[5]Para ver el TOP FIVE\n")
        print("[0]Para finalizar\n")
        accion = input("¿Que desea hacer? ")

        if accion == terminar_programa:

            en_menu = False

            mensajeria,matches_y_likes = cargar_en_archivo(mensajeria,matches_y_likes,correspondencia)
            datos_prueba.close()
            usuarios_binario.close()
            mensajeria.close()
            matches_y_likes.close

        else:

            if accion == mostrar_usuarios:

                if not se_cargo_en_pickle:

                    imprimir_usuarios(datos_prueba,usuarios_binario)

                else:
                    usuarios_binario.close()
                    usuarios_binario = open("usuarios_nuevos.pkl","rb+")
                    imprimir_usuarios(datos_prueba,usuarios_binario)
                    se_cargo_en_pickle = False

            elif accion == nueva_cuenta:

                (pseudonimo, valores, usuarios_binario) = cargar_datos(pseudonimo, valores, usuarios, usuarios_binario)
                usuarios[pseudonimo] = valores
                se_cargo_en_pickle=True

            elif accion == ingreso_sistema:

                ingresar_sistema(usuarios,correspondencia)

            elif accion == top5:
                from likes_y_msj import top_five
                top_five(correspondencia)

    return 'FIN DE PROGRAMA'

print(menu_ppal())
