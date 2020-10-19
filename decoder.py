def two():
    text = input("\nEscriba la frase a descodificar: ")
    key = int(input("\nEscriba el desplazamiento: "))
    decodify(text, key)


def one():
    text = input("\nEscriba la frase a codificar: ")
    key = int(input("\nEscriba el desplazamiento: "))
    codify(text, key)


def switch(option):
    switcher = {
        1: one,
        2: two,
    }
    switcher.get(option)()


def codify(text, key):
    new_text = ""
    for letter in text:
        if letter.isupper():
            ascii = ord(letter)
            position = ascii - ord('A')
            new_position = (position + key) % 26 + ord('A')
            new_text += chr(new_position)

        elif letter.islower():
            ascii = ord(letter)
            position = ascii - ord('a')
            new_position = (position + key) % 26 + ord('a')
            new_text += chr(new_position)
        elif letter.isdigit():
            ascii = ord(letter)
            position = ascii - ord('0')
            new_position = (position + key) % 10 + ord('0')
            new_text += chr(new_position)
        else:
            new_text += letter
    return print(new_text)


def decodify(text, key):
    new_text = ""
    for letter in text:
        if letter.isupper():
            ascii = ord(letter)
            position = ascii - ord('A')
            new_position = (position - key) % 26 + ord('A')
            new_text += chr(new_position)

        elif letter.islower():
            ascii = ord(letter)
            position = ascii - ord('a')
            new_position = (position - key) % 26 + ord('a')
            new_text += chr(new_position)
        elif letter.isdigit():
            ascii = ord(letter)
            position = ascii - ord('0')
            new_position = (position - key) % 10 + ord('0')
            new_text += chr(new_position)
        else:
            new_text += letter
    return print(new_text)


option = -1
while option != 0:
    print("\n1, Codificar")
    print("2, Descodificar")
    option = int(input("Seleccione una opción: "))
    switch(option)
