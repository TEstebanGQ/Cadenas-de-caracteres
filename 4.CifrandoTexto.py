"""
Autor: Tomas Esteban Gonzalez Quintero - J3
Fecha: 19/07/2025
Descripcion: Crea un programa que solicite al usuario una frase y reemplace todas las vocales por un carácter especial (*).
"""
frase = input('Escribe una frase: ')
contieneLetra = False

for caracter in frase:
    if caracter.isalpha():
        contieneLetra = True
        break 
if not contieneLetra:
    print('La frase debe contener letras')
else:
    fraseCifrada = frase.replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*")
    fraseCifrada = fraseCifrada.replace("A", "*").replace("E", "*").replace("I", "*").replace("O", "*").replace("U", "*")
    print(f"La frase cifrada es: {fraseCifrada}")