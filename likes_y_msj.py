import pickle

def cargar_en_archivo(archivo1,archivo2,diccionario):

#Funcion que carga en los archivos 'mensajeria.pkl' y 'likes.pkl' los mensajes y likes de los diccionarios
#correspondientes

    mensajeria = archivo1

    likes_y_matches = archivo2

    pkl_mensajes = pickle.Pickler(mensajeria)
    pkl_likes = pickle.Pickler(likes_y_matches)

    mensajeria.seek(0)
    likes_y_matches.seek(0)

    diccionario1 = guardar_mensajes(diccionario)
    diccionario2 = guardar_likes(diccionario)

    pkl_mensajes.dump(diccionario1)
    pkl_likes.dump(diccionario2)

    return mensajeria,likes_y_matches

def cargar_diccionario(mensajeria,matches,diccionario):

# Funcion que carga de los archivos 'mensajeria.pkl' y 'likes.pkl' en un diccionario para utilizar durante el programa

    fin_mensajeria = mensajeria.seek(0, 2)
    fin_matches = matches.seek(0,2)
    no_hay_datos = 0

    mensajeria.seek(0)
    matches.seek(0)

    if fin_mensajeria == no_hay_datos and fin_matches == no_hay_datos:

        return diccionario
    else:
        mensajes = pickle.load(mensajeria)
        likes_y_matches = pickle.load(matches)
        diccionario = apareo_diccionario(mensajes,likes_y_matches)
        return diccionario

def top_five(diccionario):

# Funcion que recorre una unica vez el diccionario que se esta usando en el programa y imprime por pantalla el TOP FIVE

    num_1 = 0
    num_2 = 0
    num_3 = 0
    num_4 = 0
    num_5 = 0
    clave_1 = ''
    clave_2 = ''
    clave_3 =''
    clave_4 = ''
    clave_5 = ''
    lista = []
    desordenado = True
    n = len(diccionario.keys())
    if diccionario != {} and n>=5:

        for clave in diccionario:

            iterar = True


            num = diccionario[clave][2]

            if num_1 == 0:
                num_1 = num
                clave_1 = clave
                lista.append([num_1,clave_1])
            elif num_2 == 0:
                clave_2 = clave
                num_2 = num
                lista.append([num_2,clave_2])
            elif num_3 == 0:
                num_3 = num
                clave_3 = clave
                lista.append([num_3,clave_3])
            elif num_4 == 0:
                clave_4 = clave
                num_4 = num
                lista.append([num_4,clave_4])
            elif num_5 == 0:
                clave_5 = clave
                num_5 = num
                lista.append([num_5,clave_5])
            else:

                if desordenado:
                    lista.sort(key=lambda x: x[0], reverse=True)
                    num_1 = lista[0][0]
                    clave_1 = lista[0][1]
                    num_2 = lista[1][0]
                    clave_2 = lista[1][1]
                    num_3 = lista[2][0]
                    clave_3 = lista[2][1]
                    num_4 = lista[3][0]
                    clave_4 = lista[3][1]
                    num_5 = lista[4][0]
                    clave_5 = lista[4][1]
                    desordenado = False
                    #iterar = True
                while iterar:
                    if num > num_1:
                        num_5 = num_4
                        clave_5 = clave_4
                        num_4 = num_3
                        clave_4 = clave_3
                        num_3 = num_2
                        clave_3 = clave_2
                        num_2 = num_1
                        clave_2 = clave_1
                        num_1 = num
                        clave_1 = clave
                        iterar = False
                    elif num > num_2:
                        num_5 = num_4
                        clave_5 = clave_4
                        num_4 = num_3
                        clave_4 = clave_3
                        num_3 = num_2
                        clave_3 = clave_2
                        num_2 = num
                        clave_2 = clave
                        iterar = False
                    elif num > num_3:
                        num_5 = num_4
                        clave_5 = clave_4
                        num_4 = num_3
                        clave_4 = clave_3
                        num_3 = num
                        clave_3 = clave
                        iterar = False
                    elif num > num_4:
                        num_5 = num_4
                        clave_5 = clave_4
                        num_4 = num
                        clave_4 = clave
                        iterar = False
                    elif num > num_5:
                        num_5 = num
                        clave_5 = clave
                        iterar = False
                    else:
                        iterar = False

        print("TOP FIVE: \n")
        print("#1 {}, con {} likes".format(clave_1,num_1))
        print("#2 {}, con {} likes".format(clave_2,num_2))
        print("#3 {}, con {} likes".format(clave_3,num_3))
        print("#4 {}, con {} likes".format(clave_4,num_4))
        print("#5 {}, con {} likes".format(clave_5,num_5))
    else:
        print("TOP FIVE: ")
        print("Hasta el momento ningun usuario tuvo likes o hay menos de cinco usuarios\n")

def apareo_diccionario(mensajes,likes_y_matches):

# Funcion que aparea los diccionarios de likes y mensajes para utilizar durante en el programa.

    diccionario_nuevo = {}

    for clave2 in likes_y_matches:

        matches = likes_y_matches[clave2][0]

        cant_likes_recibidos = likes_y_matches[clave2][1]

        if mensajes != {}:

            for clave1 in mensajes:

                mensajes_recibidos = mensajes[clave1]

                if clave1 == clave2:

                    diccionario_nuevo[clave1]=[matches,mensajes_recibidos,cant_likes_recibidos]

                elif clave2 not in mensajes:

                    diccionario_nuevo[clave2]=[matches,[],cant_likes_recibidos]
        else:

            diccionario_nuevo[clave2] = [matches, [], cant_likes_recibidos]

    return diccionario_nuevo



def guardar_mensajes(diccionario):

#Funcion que guarda en un diccionario nuevo los mensajes que tuvieron los usuarios durante el programa

    conversacion = {}

    for clave in diccionario:

        mensajes_recibidos = diccionario[clave][1]

        if mensajes_recibidos != []:

            if clave not in conversacion:

                conversacion[clave]=[]

            for lista in mensajes_recibidos:

                remitente = lista[0]
                mensajes_enviado = lista[1]
                estado_mensaje = lista[2]

                if remitente in diccionario[clave]:

                    conversacion[clave][1].append(mensajes_enviado)
                else:
                    conversacion[clave].append([remitente,mensajes_enviado,estado_mensaje])

    return conversacion

def guardar_likes(diccionario):

# Fundion que guarda en un diccionario nuevo los likes y matches que hubo durante el programa

    likes_y_matches = {}

    for clave in diccionario:

        matches = diccionario[clave][0]
        cant_likes_recibidos = diccionario[clave][2]

        likes_y_matches[clave]=[matches,cant_likes_recibidos]

    return likes_y_matches