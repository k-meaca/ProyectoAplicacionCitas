def hay_mensaje(usuario_activo,mensajeria):

    # Función que determinará si el usuario que ingreso posee mensajes.
    # Si tiene, los imprime por pantalla.

    if usuario_activo in mensajeria and len(mensajeria[usuario_activo][1]) > 0:

        posicion_cero = lambda x: x[0]
        posicion_uno = lambda x: x[1]

        bandera = 0
        contestar = '1'
        ignorar = '0'
        mensajes_a_borrar = []

        for usuario,datos in mensajeria.items():

            if usuario_activo == usuario:

                for lista in datos:

                    if lista == posicion_uno(mensajeria[usuario_activo]):

                        for listas in lista:

                            sin_leer = 1
                            leido = 0
                            accion_valida = False
                            quien_mando = posicion_cero(listas)
                            mensaje = posicion_uno(listas)
                            estado_mensaje = listas[2]
                            if estado_mensaje == sin_leer:

                                print("USTED TIENE UN MENSAJE: \n")
                                print("\v{}\nDe:{}".format(mensaje,quien_mando))
                                listas[2] = leido
                                bandera = 1


                                print("[1] Para contestar el mensaje.\n[0] Para ignorarlo\n"
                                  "(Si el mensaje es ignorado, este se borrara automaticamente)")
                                accion = input("¿Que desea hacer?")

                                while not accion_valida:
                                    if accion == contestar:
                                        mensajeria = devolver_mensaje(usuario_activo,quien_mando,mensajeria)
                                        accion_valida = True
                                    elif accion == ignorar:
                                        mensajeria = mensaje_a_borrar(usuario_activo,quien_mando,mensaje,mensajeria)
                                        accion_valida = True
                                    else:
                                        print("Ingreso una opcion incorrecta")
                                        accion = input("¿Que desea hacer?")

        #mensajeria = borrar_mensajes(usuario_activo,mensajes_a_borrar,mensajeria)
        if bandera != 0:
            print("NO SE ENCONTRO NINGUN OTRO MENSAJE")
            return True
        else:
            print("HASTA EL MOMENTO USTED NO TIENE NINGUN MENSAJE")
    else:
        print("HASTA EL MOMENTO USTED NO TIENE NINGUN MENSAJE")
        return False

def mensajes_usuarios(usuario_activo,pseudonimo,diccionario,mensajeria):

    # Función que compara los matches entre usuarios y que permite mandar mensaje del usuario activo
    # al usuario encontrado en la busqueda. Devuelve la mensajeria actualizada.

    matches= lambda x: x[0]
    mensajes_recibidos = lambda x: x[1]
    dejar_mensaje = 's'

    if pseudonimo in mensajeria:
        if usuario_activo in matches(mensajeria[pseudonimo]):
            if diccionario[pseudonimo][3] == 'mujer':
                print("{} ya esta interesada en vos".format(pseudonimo))
            elif diccionario[pseudonimo][3] == 'hombre':
                print("{} ya esta interesado en vos".format(pseudonimo))
            else:
                print("{} ya esta interesade en vos".format(pseudonimo))
            accion = input("¿Queres dejarle un mensaje?(s/n) ")
            if accion == dejar_mensaje:
                mensaje = input("Escriba el mensaje aqui: ")
                mensaje_mandado = [usuario_activo,mensaje,1]
                #mensajes_recibidos(mensajeria[pseudonimo]).append(mensaje_mandado)
                mensajeria[pseudonimo][1].append(mensaje_mandado)
    return mensajeria

def devolver_mensaje(usuario_activo,quien_mando,mensajeria):

# Fundion que permite devolver el mensaje del usuario activo al usuario remitente

    mensaje = input("Escriba el mensaje aqui: ")

    mensajeria[quien_mando][1].append([usuario_activo,mensaje,1])

    return mensajeria

def mensaje_a_borrar(usuario_activo,quien_mando,mensaje,mensajeria):

#Funcion que cambia el estado del mensaje de leido '0' a ignorado'2'. En algun futuro, esos mensajes seran borrados

    i =0
    lista = mensajeria[usuario_activo][1]

    for j in range(len(lista)):

        if quien_mando == lista[j][0] and mensaje == lista[j][1]:
            mensajeria[usuario_activo][1][j][2]=2

    return mensajeria
