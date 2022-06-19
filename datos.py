def cargar_datos (pseudonimo,valores,diccionario,binario):

#Funcion donde se podran crear nuevos usuarios. Dentro de ella se importan todas las validaciones.

    from validaciones import validacion_string
    from validaciones import pseudonimo_valido
    from validaciones import verificar_contraseña
    from validaciones import definir_sexo
    from validaciones import verificar_edad
    from validaciones import verificar_flotante
    from validaciones import verificar_intereses

    nombre = input("Ingrese su nombre: ")
    nombre = validacion_string(nombre)

    apellido = input("Ingrese su apellido: ")
    apellido = validacion_string(apellido)

    pseudonimo = input("Ingrese su usuario: ")
    pseudonimo = pseudonimo_valido(pseudonimo,diccionario)

    contraseña = input("Ingrese su contraseña con al menos 5 caracteres, una mayuscula,una minuscula y un numero: ")
    contraseña = verificar_contraseña(contraseña)

    sexo = input("Ingrese su sexo: [1]:Mujer [2]:Hombre [3]:Indefinido ")
    sexo = definir_sexo(sexo)

    edad = input("Ingrese su edad: ")
    edad = verificar_edad(edad)

    latitud = input("Ingrese su ubicacion latitudinal(en grados decimales ej: -34.615(lat CABA)): ")
    latitud = verificar_flotante(latitud)

    longitud = input("Ingrese su ubicacion longitudinal(en grados decimales ej: -58.628(long CABA)): ")
    longitud = verificar_flotante(longitud)

    ubicacion = (latitud,longitud)

    intereses = input("Ingrese sus intereses separados por comas: ")
    intereses = verificar_intereses(intereses)

    valores=[contraseña,nombre,apellido,sexo,edad,ubicacion,intereses]

    binario = cargar_usuarios_pickle(binario,pseudonimo,valores)

    return pseudonimo,valores,binario


import pickle

def cargar_usuarios_pickle(binario, pseudonimo, valores):

#Funcion que carga los usuarios creados al archivo pickle 'usuarios_nuevos.pkl'. Esto lo hace de manera ordenada
# alfabeticamente por pseudonimos

    fin_pickle = binario.seek(0, 2)

    comienzo = binario.seek(0)
    puntero = 0
    while comienzo < fin_pickle:

        lista = pickle.load(binario)

        if lista[0] < pseudonimo:
            puntero = binario.tell()

        comienzo = binario.tell()

    apuntalar = binario.seek(puntero)
    lista2 = []

    while apuntalar < fin_pickle:
        dato = pickle.load(binario)
        lista2.append(dato)
        apuntalar = binario.tell()

    binario.seek(puntero)

    pkl = pickle.Pickler(binario)
    usuario_pcargar = [pseudonimo, valores[0], valores[1], valores[2], valores[3], valores[4], valores[5], valores[6]]
    pkl.dump(usuario_pcargar)

    for i in range(len(lista2)):
        pkl.dump(lista2[i])

    return binario



