"""Un programa para encriptar según el modelo de cifras afines."""

dictionary = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
              'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
              'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21,
              'w': 22, 'x': 23, 'y': 24, 'z': 25}

# Creé las variables keyA (a), keyB (b) y message como los inpur donde el
# usuario ingresará los números y el mensaje. Error_list es la lista donde se
# encuentran todos los caracteres no incluidos en el diccionario
# y que puedan causar un KeyError. Keys_list es la variable que devolverá
# una lista con las keys del diccionario.

key_a = int(input("Escribe la primera llave de tu encriptación "))
key_b = int(input("Escribe la segunda llave de tu encriptación "))
message = input("Escribe el mensaje que quieres encriptar ")

keys_list = list(dictionary.keys())


def encript_letter(dic_key, a, b, cripting_list, lista_llaves):

    try:

        was_upper = False

        if dic_key.isupper() is True:
            dic_key = dic_key.lower()
            was_upper = True
        result = (a * dictionary[dic_key] + b) % 25

        if was_upper is True:
            cripting_list.append(lista_llaves[result].upper())
            return

        cripting_list.append(lista_llaves[result])

    except KeyError:

        cripting_list.append(dic_key)


def encript_message(a_message):
    encripted_list = []
    for letter in message:
        encript_letter(letter, key_a, key_b, encripted_list, keys_list)

    caracter = ""
    print ("El mensaje se leería así: \n" + caracter.join(encripted_list))


encript_message(message)

# Lograr, de cualquier modo, incluir espacios, comas, puntos, apóstrofes, y
# signos de exclamación e interrogación.
