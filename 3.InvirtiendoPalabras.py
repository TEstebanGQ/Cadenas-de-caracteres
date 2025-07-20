"""
Autor: Tomas Esteban Gonzalez Quintero - J3
Fecha: 19/07/2025
Descripcion: Escribe un programa que pida al usuario una palabra y muestre la palabra invertida.
"""
palabra = input("Escribe una palabra o frase: ")
espacios = palabra.replace(" ", "")
if espacios.isalpha():
    invertida = palabra[::-1]
    print(f"La frase invertida es: {invertida}")
else:
    print("Solo se permiten letras.")