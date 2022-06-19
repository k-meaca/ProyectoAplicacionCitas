def ingresar_sistema(diccionario,mensajeria):

    # Funcion donde el usuario va a ingresar su ID y PWS. En caso de ser correctos, llama a la función
    # buscar_personas pasando como parametros el usuario que ingreso, su ubicacion, sus intereses y la mensajería.
    # De lo contrario, vuelve al menu principal.

    usuario_activo = input("Ingrese su usuario: ")
    ingresar_contraseña = input("Ingrese su contraseña: ")
    password = lambda x: x[0]
    ubicacion = lambda x: x[5]
    intereses = lambda x: x[6]
    valido = True
    if usuario_activo in diccionario:
        if ingresar_contraseña == password(diccionario[usuario_activo]):
            from casilla_mensajes import hay_mensaje
            if hay_mensaje(usuario_activo, mensajeria):
                    ubicacion_activo = ubicacion(diccionario[usuario_activo])
                    intereses_activo = intereses(diccionario[usuario_activo])
                    accion = input("¿Listo para comenzar con la busqueda?(s/n) ")
                    while valido:
                        if accion == 's':
                            buscar_personas(usuario_activo,ubicacion_activo,intereses_activo,diccionario, mensajeria)
                            valido = False
                        elif accion == 'n':
                            valido = False
                        else:
                            print("Usted ingreso algo distinto a 's' o 'n'.")
                            accion = input("¿Listo para comenzar con la busqueda?(s/n) ")

            else:
                    ubicacion_activo = ubicacion(diccionario[usuario_activo])
                    intereses_activo = intereses(diccionario[usuario_activo])
                    accion = input("¿Listo para comenzar con la busqueda?(s/n) ")
                    while valido:
                        if accion == 's':
                            buscar_personas(usuario_activo, ubicacion_activo, intereses_activo, diccionario, mensajeria)
                            valido = False
                        elif accion == 'n':
                            valido = False
                        else:
                            print("Usted ingreso algo distinto a 's' o 'n'.")
                            accion = input("¿Listo para comenzar con la busqueda?(s/n) ")
                   
        else:
            print("Contraseña equivocada. Reingrese los datos nuevamente.\v")
            return 0
    else:
        print("Usuario invalido. Reingrese los datos nuevamente.\v")

def parametros_busqueda():

    # Función donde el usuario ingresará los parametros para buscar a las personas.
    # Devuelve una lista

    from validaciones import verificar_flotante
    from validaciones import verificar_edad
    from validaciones import definir_sexo

    #print("Esta por comenzar la busqueda de personas:\v")

    radio_de_busqueda = (input("¿A que distancia maxima(en kilometros) debe estar la otra persona? "))
    radio_de_busqueda = verificar_flotante(radio_de_busqueda)

    busqueda_por_sexo = input("¿Que sexó tiene la otra persona? [1]:Mujer [2]:Hombre [3]:Indefinido ")
    busqueda_por_sexo = definir_sexo(busqueda_por_sexo)

    edad_minima = input("¿Que edad minima debe tener la otra persona? ")
    edad_minima = verificar_edad(edad_minima)

    edad_maxima = input("¿Que edad maxima debe tener la otra persona? ")
    edad_maxima = verificar_edad(edad_maxima)

    lista_parametros = [radio_de_busqueda,busqueda_por_sexo,edad_minima,edad_maxima]

    return lista_parametros

def buscar_personas(usuario_activo,ubicacion_activo,intereses_activo, diccionario, mensajeria):

    # En esta función se van a comparar los parametros ingresados en la función 'parametros_busqueda'
    # entre los parametros recibidos del usuario activo por la funcion 'ingresar_sistema' y los datos
    # que estén en el diccionario de usuarios. Además si hay coincidencias entre estos, se llama a la
    # funcion 'mensajes_usuarios'.
    # Al finalizar devuelve el diccionario y la mensajeria actualizada

    from haversine import distance
    from validaciones import primer_matcheo
    from casilla_mensajes import mensajes_usuarios

    sexo = lambda x: x[3]
    edad = lambda x: x[4]
    ubicacion = lambda x: x[5]
    intereses = lambda x: x[6]
    hay_match = 's'
    continuar = 's'
    coincidencias = []
    lista_parametros = parametros_busqueda()
    valido = True

    for pseudonimo in diccionario.keys():

        if  sexo(diccionario[pseudonimo]) == lista_parametros[1]:

            edad_usuario = int(edad(diccionario[pseudonimo]))
            edad_min = lista_parametros[2]
            edad_max = lista_parametros[3]

            if edad_usuario >= edad_min and edad_usuario <= edad_max:

                distancia_usuarios = distance((ubicacion_activo),ubicacion(diccionario[pseudonimo]))
                distancia_max = lista_parametros[0]
                if distancia_usuarios <= distancia_max:

                    #if mensajeria != {} and pseudonimo in mensajeria[usuario_activo][0]:
                        
                        #print("Ya has matcheado con {}".format(pseudonimo))

                        #mensajes_usuarios(usuario_activo,pseudonimo,diccionario,mensajeria)

                    if usuario_activo != pseudonimo:

                        intereses_pseudonimo = intereses(diccionario[pseudonimo])
                        porcentaje = porcentaje_coincidencia(intereses_activo,intereses_pseudonimo)

                        print("¡Se ha encontrado una persona con esos parametros!")
                        print("La persona es {} y entre ustedes tienen {}% de coincidencia".format(pseudonimo,porcentaje))

                        accion = input("¿¡Hay match o no hay match!?(s/n): ")
                        if accion == hay_match:
                            coincidencias.append(pseudonimo)
                            mensajes_usuarios(usuario_activo,pseudonimo,diccionario,mensajeria)
                            
                         
                        accion2 = input("¿Desea continuar con la busqueda?(s/n)")
                        if accion2 == 'n':
                            print('USTED HA FINALIZADO LA BUSQUEDA')
                            primer_matcheo(usuario_activo,coincidencias,mensajeria)
                            return diccionario, mensajeria
                            
    print('NO SE ENCONTRO A NADIE MAS CON ESOS PARAMETROS.\nFIN DE BUSQUEDA')
    primer_matcheo(usuario_activo,coincidencias,mensajeria)
    return diccionario,mensajeria


def porcentaje_coincidencia(intereses_activo,intereses_pseudonimo):

    # Función que recibe como parametros los intereses del usuario que esta activo
    # y los intereses del usuario que coincidio con en la busqueda. Con estos datos se calcula
    # el porcentaje de coinciencias y se devuelve un entero

    coincidencia = 0
    cant_intereses_activo = len(intereses_activo)
    cant_intereses_pseudonimo = len(intereses_pseudonimo)

    for interes1 in intereses_activo:

        if interes1 in intereses_pseudonimo:
            coincidencia+=1
    porcentaje = 100 * coincidencia // (cant_intereses_activo+cant_intereses_pseudonimo)

    return porcentaje
