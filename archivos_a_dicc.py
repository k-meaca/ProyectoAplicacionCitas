def creando_diccionario(archivo_txt,archivo_binario):

    from usuarios_X_pantalla import leer_txt
    from usuarios_X_pantalla import leer_pickle

    usuarios_fijos = archivo_txt
    usuarios_binario = archivo_binario

    diccionario = {}

    fin_lectura = ''
    fin_pickle = usuarios_binario.seek(0,2)
    señalador = usuarios_binario.seek(0)

    lista_fijos = leer_txt(usuarios_fijos,fin_lectura)

    while lista_fijos != fin_lectura:

        clave = lista_fijos[0]
        valores = [lista_fijos[1],lista_fijos[2],lista_fijos[3],lista_fijos[4],int(lista_fijos[5]),
                   (float(lista_fijos[6]),float(lista_fijos[7])),lista_fijos[8].split(',')]
        diccionario[clave]=valores
        lista_fijos = leer_txt(usuarios_fijos,fin_lectura)

    cargados = True
    lista_cargados = leer_pickle(usuarios_binario,señalador,fin_pickle,fin_lectura)

    while lista_cargados != fin_lectura:

        clave = lista_cargados[0]
        valores = [lista_cargados[1], lista_cargados[2], lista_cargados[3], lista_cargados[4], lista_cargados[5],
                   lista_cargados[6],lista_cargados[7]]
        if clave not in diccionario:
            diccionario[clave]=valores
        señalador = usuarios_binario.tell()
        lista_cargados = leer_pickle(usuarios_binario,señalador,fin_pickle,fin_lectura)

    return diccionario