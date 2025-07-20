"""
Autor: Tomas Esteban Gonzalez Quintero - J3
Fecha: 19/07/2025
Descripcion: Escribe un programa que cuente cuántas vocales hay en una frase ingresada por el usuario.
"""
frase = input("Escribe una frase: ")
contiene_letra = False
for caracter in frase:
    if caracter.isalpha():
        contiene_letra = True
        break
if not contiene_letra:
    print("la frase debe contener letras.")
else:
    a = frase.count("a") + frase.count("A")
    e = frase.count("e") + frase.count("E")
    i = frase.count("i") + frase.count("I")
    o = frase.count("o") + frase.count("O")
    u = frase.count("u") + frase.count("U")

    total_vocales = a + e + i + o + u

    print(f"La frase tiene {total_vocales} vocales.")