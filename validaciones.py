def espacios_en_string(palabra):
    # Esta funcion valide que la palabra ingresada no tenga
    # espacios ni saltos de renglon.

    palabra_valida = True

    while palabra_valida:
        palabra_valida = False

        if '\t' in palabra or ' ' in palabra:
            palabra = input("No puede haber espacios. Reingrese los datos:\t")
            palabra_valida = True
    return palabra


def validacion_string(palabra):
    # Esta funcion valida que la palabra ingresada tenga solo
    # letras minusculas y mayusculas.

    valido = True
    while valido:
        valido = False
        cont=0
        for letras in palabra:
            if letras.isalpha() == True:
                cont+=1
            elif letras.isspace() == True:
                cont+=1
        if cont != len(palabra):
            palabra = input("Hay un simbolo incorrecto. Reingrese los datos nuevamente:\t")
            valido = True
    return palabra


def verificar_pseudonimo(pseudonimo):
    # Esta funcion verifica que el pseudonimo tenga solo minuscula,
    # numeros y guion bajo.

    pseudonimo = espacios_en_string(pseudonimo)
    valido = True
    while valido:
        contador = 0
        valido = False
        for letras in pseudonimo:
            if letras.islower() == True:
                contador += 1
            if letras.isdigit() == True:
                contador += 1
            if letras == '_':
                contador += 1
        if contador != len(pseudonimo):
            pseudonimo = input("Solo minusculas, guion bajo y numeros. Reingrese los datos nuevamente:\t")
            valido = True
    return pseudonimo


def pseudonimo_valido(pseudonimo, diccionario):
    # Esta funcion valida que el pseudonimo sea unico.

    pseudonimo = verificar_pseudonimo(pseudonimo)
    for i in diccionario.keys():
        if i == pseudonimo:
            pseudonimo_nuevo = input("Usuario en uso, ingrese otro:\t")
            return pseudonimo_valido(pseudonimo_nuevo, diccionario)
    return pseudonimo


def verificar_contraseña(contraseña):
    # Esta funcion valida que la contraseña ingresada tenga al menos una mayuscula,
    # una minuscula, un numero y al menos 5 caracteres.

    contador_mayusculas = 0
    contador_minusculas = 0
    contador_numeros = 0

    while contador_mayusculas < 1 and contador_minusculas < 1 and contador_numeros < 1:
        for letras in contraseña:
            if letras.isupper() == True:
                contador_mayusculas += 1
            if letras.islower() == True:
                contador_minusculas += 1
            if letras.isdigit() == True:
                contador_numeros += 1
    if contador_mayusculas >= 1 and contador_minusculas >= 1 and contador_numeros >= 1 and len(contraseña) >= 5:
        return contraseña
    else:
        contraseña_nueva = input(
            "Contraseña incorrecta. Debe tener al menos 5 caracteres, una mayuscula,una minuscula y un numero:\t")
        return verificar_contraseña(contraseña_nueva)


def verificar_edad(numero):
    # Esta funcion valida que la edad ingresada este entre 18 y 99

    try:
        int(numero)
        if int(numero) >= 18 and int(numero) <= 99:
            return int(numero)
        else:
            edad = int(input("Ingrese una edad entre 18 y 99:\t"))
            return verificar_edad(edad)
    except ValueError:
        print("No ha ingresado correctamente su edad.\t")

    valido = True

    while valido:
        try:
            edad = int(input("Reingrese su edad entre 18 y 99:\t"))
            if edad >= 18 and edad <= 99:
                valido = False
            else:
                edad = int(input("Ingrese una edad entre 18 y 99:\t"))
                return verificar_edad(edad)
        except ValueError:
            print("No ha ingresado correctamente su edad.\v")

    return edad


def definir_sexo(letra):
    # Esta funcion le da a sexo el valor segun hayan ingresado 1, 2 o 3

    if letra == "1":
        sexo = "mujer"
    elif letra == "2":
        sexo = "hombre"
    elif letra == "3":
        sexo = "indefinido"
    else:
        ingresar_sexo = input("Ingrese una opcion correcta:\t")
        return definir_sexo(ingresar_sexo)
    return sexo


def verificar_flotante(numero):
    # Esta funcion recibe un dato ingresado por el usuario y verifica que sea un numero. Si es un numero entero, lo castea a flotante

    try:
        float(numero)
        return float(numero)
    except ValueError:
        print("ValueError.No ha ingresado correctamente su ubicacion.\t")

    valido = True

    while valido:
        try:
            flotante = float(input("Reingrese los datos nuevamente:\t"))
            valido = False
        except ValueError:
            print("ValueError.No ha ingresado correctamente su ubicacion.\t")

    return flotante


def verificar_intereses(intereses):
    # Esta funcion verifica que los intereses esten separadas
    # por comas y reemplaza los espacios por guiones

    lista_intereses = []
    lista = []
    for letras in intereses:
        if letras.isalpha() != True and letras != ',' and letras != ' ':
            intereses = input('Solo minusculas y comas. Ingrese sus intereses nuevamente:\t')
            return verificar_intereses(intereses)
    intereses = intereses.replace(' ', '-')

    lista.extend(intereses.split(','))
    for palabra in lista:
        palabra_nueva = ''
        if palabra[0] == '-':
            for i in range(len(palabra)):
                if i != 0:
                    palabra_nueva = palabra_nueva + palabra[i]

            lista_intereses.append(palabra_nueva)
        else:
            lista_intereses.append(palabra)
    return lista_intereses


def primer_matcheo(usuario_activo, coincidencias, mensajeria):
    # Esta función recibe, un usuario activo, sus coincidencias, y el diccionario de mensajeria. Lo que hace es verificar
    # que el usuario activo este dentro de la mensajeria. Evalua dos circunstancias:
    # Si no esta en la mensajeria,lo agrega a la mensajeria, con sus coincidencias y ademas agrega una lista vacia a la clave
    # del usuario activo para futuros mensajes y un espacio reservado para contar los likes recibidos.
    # Si ya se encontraba en la mensajeria, compara sus coincidencias actuales con las que ya tenia y si algun usuario no se encuentra
    # lo agrega a sus coincidencias anteriores.

    lista = []

    if usuario_activo not in mensajeria:

        mensajeria[usuario_activo] = [coincidencias]

        mensajeria[usuario_activo].append(lista)
        mensajeria[usuario_activo].append(0)
        mensajeria = contar_likes(usuario_activo,coincidencias,mensajeria)

    elif len(mensajeria[usuario_activo]) > 1:

        posicion_cero = lambda x: x[0]

        for usuario in coincidencias:

            if usuario not in posicion_cero(mensajeria[usuario_activo]):
                posicion_cero(mensajeria[usuario_activo]).append(usuario)
        mensajeria = contar_likes(usuario_activo,coincidencias,mensajeria)

    return mensajeria

def contar_likes(usuario_activo,coincidencias,mensajeria):

#Funcion que cuenta los likes de las coincidencias del usuario activo
    sin_likes = 0

    for usuario in coincidencias:
        if usuario in mensajeria and (usuario not in mensajeria[usuario_activo][0]):
                mensajeria[usuario][2]+=1
        elif usuario not in mensajeria:
            mensajeria[usuario]=[[],[],1]
        else:
            mensajeria[usuario][2]+=1
    return mensajeria


