# 🌐Taller guiado con cadenas de caracteres en python 

####  ESTUDIANTE: Tomas Esteban Gonzalez Quintero J-3

### 🔖Ejercicio 1: Contando caracteres

Se nos pide un programa que sea capaz de solicitar al usuario una frase y que este muestre la cantidad total de caracteres en la frase mostrando también los espacios en blanco.

##### CÓDIGO:

```
frase = input("Escribe una frase: ")
total_caracteres = len(frase)
espacios = frase.count(" ")

print(f"La frase tiene {total_caracteres} caracteres en total.")
print(f"La frase tiene {espacios} espacios.")
```

##### 📄 EXPLICACIÓN:

```
frase = input("Escribe una frase: ")
```

###### frase = es la variable que estamos definiendo para darle uso en otros momentos, ella se encarga de guardar el resultado para ser utilizado después.

###### input = esta es una función de entrada encargada de transcribir lo que escribió el usuario

###### "Escribe una frase: " = este resultado es el impreso al usuario donde este va a escribir lo que se esta solicitando

```
total_caracteres = len(frase)
```

###### total_caracteres = esta variable es la encargada de indicar cuantos caracteres hay en la frase que escribió el usuario.

###### len = esta es una función que esta incorporada que cuenta la cantidad de caracteres(letras, espacios, signos, etc) que se encuentre en una cadena osea, la frase del usuario.

###### frase = aquí lo que cumple esta variable es que 'len' lea los caracteres escritos en la variable 'frase' .

```
espacios = frase.count(" ")
```

###### espacios = esta es la variable que va a almacenar la función a realizar.

###### frase = lee anteriormente la frase escrita por el usuario.

###### count(" ") = este es un método de cadenas de texto que su principal función es ver cuantas veces aparece un carácter especifico en la frase, en este caso el espacio especifico es ' ', osea el espacio en blanco de las frases.

```
print(f"La frase tiene {total_caracteres} caracteres en total.")
```

###### print = este imprime al usuario el resultado

######  (f"La frase tiene {total_caracteres} caracteres en total.") = 'f' su nombre técnico es f-string osea cadena formateada es aquella que permite colocar o llamar a una variable dentro el resultado del texto con { }.  el resultado que se imprime es: 'La frase tiene {total_caracteres} caracteres en total.' al usuario se le esta imprimiendo cuantos caracteres tiene la frase escrita anteriormente por el usuario

```
print(f"La frase tiene {espacios} espacios.")
```

###### print = este imprime el resultado final al usuario

###### f"La frase tiene {espacios} espacios." =   'f' su nombre técnico es f-string osea cadena formateada es aquella que permite colocar o llamar a una variable dentro el resultado del texto con { }. El resultado que imprime es: La frase tiene {espacios} espacios. el da el resultado de 'espacios' y nos dice cuantos espacios habían.

### 🔖Ejercicio 2: Validando nombres

Se solicita un programa donde el usuario escriba su nombre completo y se verifique que la primera letra del usuario empiece en mayúscula donde este no contenga números.

##### CÓDIGO:

```
nombre = input("Escribe tu nombre completo: ")

if nombre.replace(" ", "").isalpha():
    if nombre.istitle():
        print("El nombre es válido.")
    else:
        print("El nombre debe comenzar con mayúscula ejemplo(Pepe Ramirez).")
else:
    print("El nombre solo debe contener letras.")
```

##### 📄 EXPLICACIÓN:

```
nombre = input("Escribe tu nombre completo: ")
```

###### nombre = es la variable que estamos definiendo para darle uso en otros momentos, ella se encarga de guardar el resultado para ser utilizado después.

###### input = esta es una función de entrada encargada de transcribir lo que escribió el usuario

###### "Escribe tu nombre completo: " = este resultado es el impreso al usuario donde este va a escribir lo que se esta solicitando

```
if nombre.replace(" ", "").isalpha():
```

###### if = es como colocar  si todo es verdadero en este caso se va a imprimir el resultado puesto en 'if'.

###### nombre.replace(" ", "") = este lo que su función principal es eliminar los espacios en blanco, ejemplo: 'Tomas Gonzalez' lo cambia a 'TomasGonzalez'.

###### .isalpha() = este es una cadena de texto donde verifica que el resto de texto escrito sea solamente letras.

```
 if nombre.istitle():
```

###### if = este 'if ' dentro de que ya cumple una función verdadera tiene que cumplir otra función verdadera para que el resultado sea optimo.

###### nombre.istitle() = llama a la variable nombre osea este muestra el resultado ya guardado. '.istitle', este es el en encargado de que cada palabra ingresada empiece su primera letra con mayúscula y el resto minúscula, ejemplo: 'Tomas Gonzalez' esta opción es correcta.

```
 print("El nombre es válido.")
```

######  print = este función es la encargada de mostrar el resultado al usuario si las dos condiciones son correctas.

###### "El nombre no es valido" = Es el mensaje que se le muestra al usuario

```
else:
```

###### else = si la segunda condición no se cumple va a colocarlo como FALSE donde imprime el resultado colocado en 'else'

 

```
print("El nombre debe comenzar con mayúscula ejemplo(Pepe Ramirez).")
```

###### print = este función es la encargada de mostrar el resultado al usuario si la segunda condición es falsa.

###### "El nombre debe comenzar con mayúscula ejemplo(Pepe Ramirez)." = Es el mensaje que se le muestra al usuario

```
else:
    print("El nombre solo debe contener letras.")
```

###### else = este 'else' es si en la primera condición no es correcta va a imprimir el resultado colocado aquí

###### "El nombre solo debe contener letras." = Es el mensaje que se le muestra al usuario

### 🔖Ejercicio 3: Invirtiendo palabras

Se nos pide un programa que le pida al usuario una palabra y esta la invierta, mostrando el resultado (yo quería intentar con una frase, por eso el código).

##### CÓDIGO:

```
palabra = input("Escribe una palabra o frase: ")
espacios = palabra.replace(" ", "")
if espacios.isalpha():
    invertida = palabra[::-1]
    print(f"La frase invertida es: {invertida}")
else:
    print("Solo se permiten letras. ")
```

##### 📄 EXPLICACIÓN:

```
palabra = input("Escribe una palabra o frase: ")
```

###### palabra = es la variable que estamos definiendo para darle uso en otros momentos, ella se encarga de guardar el resultado para ser utilizado después.

###### input = esta es una función de entrada encargada de transcribir lo que escribió el usuario

###### "Escribe una palabra o frase:  " = este resultado es el impreso al usuario donde este va a escribir lo que se esta solicitando

```
espacios = palabra.replace(" ", "")
```

###### 

###### palabra.replace(" ", "") = este lo que su función principal es eliminar los espacios en blanco, ejemplo: 'Feisal Umbarila' lo cambia a 'FeisalUmbarila', esto lo hace imprimiendo el resultado puesto en la variable 'palabra'.

```
if espacios.isalpha():
```

###### if =  es como colocar  si todo es verdadero en este caso se va a imprimir el resultado puesto en 'if'.

###### espacios.isalpha() = este es una cadena de texto donde verifica que el resto de texto escrito sea solamente letras, conforme a lo puesto y guardado en la variable 'espacios'.

```
invertida = palabra[::-1]
```

###### invertida = esta variable es la encargada de guardar el resultado de la palabra o frase invertida

###### palabra[::-1] =  que significa desde el principio al final, pero con paso '-1' (es decir, hacia atrás), para poder tener el resultado ya casi lista.

```
print(f"La frase invertida es: {invertida}")
```

###### print = este imprime el resultado final al usuario

###### f"La frase invertida es: {invertida}" =   'f' su nombre técnico es f-string osea cadena formateada es aquella que permite colocar o llamar a una variable dentro el resultado del texto con { }. El resultado que imprime es: "La frase invertida es: {invertida}",  el da el resultado de 'invertida' y nos muestra la frase o palabra invertida

```
else:
    print("Solo se permiten letras. ")
```

###### else = Si en la condición no es correcta va a imprimir el resultado colocado aquí.

###### "Solo se permiten letras. " = Es el mensaje que se le muestra al usuario

### 🔖Ejercicio 4: Cifrado texto

Se nos pide un programa que que solicite al usuario una frase y reemplace todas las vocales por un carácter especial (*)

##### CÓDIGO:

```
frase = input("Escribe una frase: ")
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
```

##### 📄 EXPLICACIÓN:

```
frase = input("Escribe una frase: ")
```

###### frase = es la variable que estamos definiendo para darle uso en otros momentos, ella se encarga de guardar el resultado para ser utilizado después.

###### input = esta es una función de entrada encargada de transcribir lo que escribió el usuario

###### "Escribe una frase: " = este resultado es el impreso al usuario donde este va a escribir lo que se esta solicitando

```
contieneLetra = False
```

###### contieneLetra = False : contiene que la variable 'contineLetra ' sea falsa , con el fin si se escribe o dar enter no bote error

```
for caracter in frase:
```

###### for caracter in frase = crea un bucle que recorre de manera individual por cada letra, guardada en 'frase'.

```
if caracter.isalpha()
```

###### verifica si es un carácter del alfabeto y lo devuelve como verdadero

```
contieneLetra = True
break 
```

###### lo que hace que si al menos contiene una letra esta lo toma como falso para que automáticamente se pueda seguir operando y no bote como un error y se cierra el bucle

```
if not contieneLetra:
    print('La frase debe contener letras')
```

###### verifica si se encontró una letra en caso de que no la encontrara esta la imprime como que debe colocar letras al menos para poder operar.

```
else:
    fraseCifrada = frase.replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*")
    fraseCifrada = fraseCifrada.replace("A", "*").replace("E", "*").replace("I", "*").replace("O", "*").replace("U", "*")
```

###### esta la encargada de cifrar las vocales tanto mayúsculas como minúsculas por (*)  , el else es que si arriba no se cumplió la condición va a botar este resultado.

###### .replace = este cambia parte de una cadena por otra, en este caso cambia las vocales por (*) para colocarla como cifrado

```
  print(f"La frase cifrada es: {fraseCifrada}")
```

###### esta imprime el resultado de la fraseCifrada al usuario.

### 🔖Ejercicio 5: Contador de vocales

Se nos pide un programa que nos cuente cuantas vocales hay en la frase escrita por el usuario, imprimiendo el resultado.

##### CÓDIGO:

```
frase = input("Escribe una frase: ")
contieneLetra = False
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
```

##### 📄 EXPLICACIÓN:

```
frase = input("Escribe una frase: ")
```

###### frase = es la variable que estamos definiendo para darle uso en otros momentos, ella se encarga de guardar el resultado para ser utilizado después.

###### input = esta es una función de entrada encargada de transcribir lo que escribió el usuario

###### "Escribe una frase: " = este resultado es el impreso al usuario donde este va a escribir lo que se esta solicitando

```
contieneLetra = False
```

###### contieneLetra = False : contiene que la variable 'contineLetra ' sea falsa , con el fin si se escribe o dar enter no bote error

###### 

```
for caracter in frase:
```

###### for caracter in frase = crea un bucle que recorre de manera individual por cada letra, guardada en 'frase'.

```
if caracter.isalpha()
```

###### verifica si es un carácter del alfabeto y lo devuelve como verdadero

```
contieneLetra = True
break 
```

###### lo que hace que si al menos contiene una letra esta lo toma como falso para que automáticamente se pueda seguir operando y no bote como un error y se cierra el bucle

```
else:
    a = frase.count("a") + frase.count("A")
    e = frase.count("e") + frase.count("E")
    i = frase.count("i") + frase.count("I")
    o = frase.count("o") + frase.count("O")
    u = frase.count("u") + frase.count("U")
```

###### se cuenta cuantas veces aparece las vocales en mayusculas y en minusculas con el fin de evitar errores

###### .count = este sirve para cuantas veces aparece una subcadena o caracter dentro de una cadena osea dentro de las frases cuando parecen las vocales.

```
 total_vocales = a + e + i + o + u
```

###### se suman todas las vocales para saber el total de todas

```
print(f"La frase tiene {total_vocales} vocales.")
```

###### print = este imprime el resultado final al usuario

###### f"La frase tiene {total_vocales} vocales." =   'f' su nombre técnico es f-string osea cadena formateada es aquella que permite colocar o llamar a una variable dentro el resultado del texto con { }. El resultado que imprime es: "La frase tiene {total_vocales} vocales.",  el da el resultado de 'total_vocales' y nos muestra lasuma de las vocales en la frase

### 🔖Ejercicio 6: Formateando Cadenas

Escribe un programa que tome un número de teléfono ingresado por el usuario (10 dígitos) y lo formatee como `(XXX) XXX-XXXX`.

##### CODIGO:

```
telefono = input("Escribe un número de teléfono de 10 dígitos: ")
if len(telefono) == 10 and telefono.isdigit():
    telefono_formateado = f"({telefono[:3]}) {telefono[3:6]}-{telefono[6:]}"
    print(f"El número formateado es: {telefono_formateado}")
else:
    print("El número debe tener exactamente 10 dígitos(sin letras ni simbolos)")
```

##### 📄 EXPLICACIÓN:

```
telefono = input("Escribe un número de teléfono de 10 dígitos: ")
```

###### le pide al usuario que escriba 10 numeros, y lo almacena en la variable telefono

```
if len(telefono) == 10 and telefono.isdigit():
```

###### comprueba si la cantidad de caracteres ingresados es 10 si escribe algo mas ya cuenta como algo ya falso, el '.isdigit()' llega a verificar que todos sean numeros

```
telefono_formateado = f"({telefono[:3]}) {telefono[3:6]}-{telefono[6:]}"
```

###### esta cadena es alcenada en la variable telefono_formateado, su principal funcion es que f-string toma los numeros como los 3 primeros digitos, depues los 3 siguientes son prefijos y los ultimos 4 como el numero ya final

```
 print(f"El número formateado es: {telefono_formateado}")
```

###### nos muestra el resultado del if, mas lo guardado en la variable telefono_formateado.

```
else:
    print("El número debe tener exactamente 10 dígitos(sin letras ni simbolos)")
```

###### si ninguna de las condiciones del 'if'  se cumple este imprimira el resultado colacado en 'else' , donde dice que debe tener numeros hasta 10 digitos , y nada de ltras o algo mas. 

### 🔖Ejercicio 7: Detentando palidromios

se nos pide un programa que determine si una palabra ingresada por el usuario es un palíndromo, y mostar su resultado

##### CODIGO:

```
palabra = input("Escribe una palabra: ").lower()
invertida = palabra[::-1]

if palabra == invertida:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
```

##### 📄 EXPLICACIÓN:

```
palabra = input("Escribe una palabra: ").lower()
```

###### Este  la variable palabra revise lo suministrado por el usuario, y es covertido a minusculas

```
invertida = palabra[::-1]
```

###### usa slicing con paso negativo, osea esto significa que invierte la cadena

```
if palabra == invertida:
    print("La palabra es un palíndromo.")
```

###### si se cumple y se invierte la cadena sin problemas toma a 'if' y nos bota que es un palindromo

```
else:
    print("La palabra no es un palíndromo.")
```

###### si no se cumple lo propuesto en la variable invertida, este nos va a decir que no es un palindromo
