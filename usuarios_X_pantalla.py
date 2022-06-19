import pickle

def imprimir_usuarios(archivo_txt,archivo_binario):

    usuarios_fijos = archivo_txt
    usuarios_binario = archivo_binario

    usuarios_fijos.seek(0)

    #fin_archivo = ''
    fin_pickle = usuarios_binario.seek(0,2)
    señalador = usuarios_binario.seek(0)
    fin_lectura = 'zzzzzzzz'

    nombre_fijo,apellido_fijo,edad_fijo,pseudonimo_fijo = leer_txt(usuarios_fijos,fin_lectura)

    if fin_pickle > 0:

        nombre_binario,apellido_binario,edad_binario,pseudonimo_binario = leer_pickle(usuarios_binario,señalador,fin_pickle,fin_lectura)
        #nombre_cargado, apellido_cargado, edad_cargado, pseudonimo_cargado = leer_pickle(usuarios_cargados)

        while (pseudonimo_fijo != fin_lectura) or (señalador < fin_pickle):


            pseudonimo_ant = ordenar_pseudonimo(pseudonimo_fijo,pseudonimo_binario)

            while pseudonimo_fijo == pseudonimo_ant and pseudonimo_fijo != fin_lectura:

                print(pseudonimo_fijo,nombre_fijo,apellido_fijo,edad_fijo)
                nombre_fijo, apellido_fijo, edad_fijo, pseudonimo_fijo = leer_txt(usuarios_fijos,fin_lectura)

            while pseudonimo_binario == pseudonimo_ant and pseudonimo_binario != fin_lectura:

                print(pseudonimo_binario,nombre_binario,apellido_binario,edad_binario)
                señalador = usuarios_binario.tell()
                nombre_binario, apellido_binario, edad_binario, pseudonimo_binario = leer_pickle(usuarios_binario,señalador,fin_pickle,fin_lectura)

    else:
        while (pseudonimo_fijo != fin_lectura):

            print(pseudonimo_fijo,nombre_fijo,apellido_fijo,edad_fijo)
            nombre_fijo, apellido_fijo, edad_fijo, pseudonimo_fijo = leer_txt(usuarios_fijos,fin_lectura)

def leer_txt(archivo, fin_lectura):

    linea = archivo.readline().rstrip("\n")

    if fin_lectura == 'zzzzzzzz':

        if linea:
            linea = linea.split(';')

            nombre = linea[2]
            apellido = linea[3]
            edad = linea[5]
            pseudonimo = linea[0]

            return nombre,apellido,edad,pseudonimo
        else:

            return 0,0,0,fin_lectura
    else:
        if linea:
            linea = linea.split(';')

            return linea
        else:
            return fin_lectura

def leer_pickle(binario,señalador,fin_pickle,fin_lectura):

    if fin_lectura == 'zzzzzzzz':
        if señalador < fin_pickle:

            datos = pickle.load(binario)

            nombre = datos[2]
            apellido = datos[3]
            edad = datos[5]
            pseudonimo = datos[0]

            return nombre,apellido,edad,pseudonimo
        else:
            return 0,0,0,fin_lectura
    else:
        if señalador < fin_pickle:

            datos = pickle.load(binario)

            return datos
        else:
            return fin_lectura

def ordenar_pseudonimo(pseudonimo_fijo,pseudonimo_cargado):

    i = 0
    j = 0
    contador_fijo = 0
    contador_cargado = 0
    iterar = True

    while (i<len(pseudonimo_fijo)) and (j<len(pseudonimo_cargado)) and iterar:

        if pseudonimo_fijo[i] != pseudonimo_cargado[j]:

            if pseudonimo_fijo[i] < pseudonimo_cargado[j]:

                contador_fijo +=1
            else:
                contador_cargado +=1

            iterar = False
        i += 1
        j += 1
    if contador_fijo > contador_cargado:
        return pseudonimo_fijo
    elif contador_fijo < contador_cargado:
        return pseudonimo_cargado
    else:
        if len(pseudonimo_fijo) < len(pseudonimo_cargado):
            return pseudonimo_fijo
        else:
            return pseudonimo_cargado
