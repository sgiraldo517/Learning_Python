# -------------------------------------------------------
# Dia 2
# -------------------------------------------------------

# TIPOS DE DATOS
    # 1. String (str): texto. En python, cualquier cadena de caracteres que este encerrada en " "
    # 2. integer (int): cualquier numero positivo o negavito que NO este entre " ". Se puede hacer operaciones con ellos.
    # 3. floating (float): decimales que no se encuentren entre comillas. Tambien se puede hacer operaciones con ellos.
    # 4. listas (list): coleccion ordenada de objetos. Se escriben entre corchetes y pueden contener objetos de todo tipo []
        # Caracteristica importante: el orden es importante y cada elemento tiene un lugar numerado o INDICE que inicia en 0 hasat el ultimo elemento.
    # 5. diccionarios (dict): pares de palabras agrupados (clave y valor)
        # No estan ordenados con indice.
    # 6. tuples (tuple): similares a las listas. Es una agrupacion ordenada de objetos pero su orden es inmutable.
    # 7. sets (set): conjunto ordenado de elementos unicos ({})
    # 8. booleanos (bool): True, False

# VARIABLES
    # Espacio de memoria al que se le pone un nombre y queda reservado para que se pueda poner en ella el valor deseado

# -------------------------------------------------------

nombre = 'Juan'
print(nombre)

nombre = 'Laura' # Para cambiar el valor de la variable solo es necesario declararla de nuevo con su nuevo valor
print(nombre)

edad = 30
edad2 = 15
print(edad + edad2) # se pueden hacer operaciones matematicas con las variables tipo integer

# nombre = input("dime tu nombre")
print("Tu nombre es " + nombre)

nombre1 = 'hola'
nombre2 = 'python'
frase = nombre1 + nombre2 # Se pueden concatenar variables de tipo string
print(frase)

print("--------------------")

# -------------------------------------------------------

# INTEGERS Y FLOATS

mi_numero = 1
print(mi_numero)
print(type(mi_numero)) # la funcion Type permite saber que tipo de dato es una variable

mi_numero = 1 + 3
print(mi_numero + mi_numero)

mi_numero = 5.8
print(mi_numero)
mi_numero = mi_numero + mi_numero
print(mi_numero)
print(type(mi_numero))

mi_numero = 5 + 5.8
print(mi_numero)
print(type(mi_numero)) # la suma de int + float dara siempre un resultado de tipo float

num1 = 7.5
num2 = 2.5
print(type(num1 + num2))  # Resultado de la operacion es de tipo float

edad = input("Dime tu edad: ")
print("Tu edad es " + edad)
print(type(edad))
print(edad + edad) # Concatenacion de str

# nueva_edad = 1 + edad
# print("vas a cumplir " + nueva_edad) # Error: + no puede funcionar entre int y strings
    # Nota: todo lo que el usuario ingrese mediante un input sera tomado como String

print("--------------------")

# -------------------------------------------------------

# CASTING: coversiones entre Tipos de Datos
    # Implicita: Python convierte el tipo de datos en otro tipo de datos automaticamente
    # Explicita: Python necesita que el usuario haga algo para convertir un tipo de dato en otro

# Ejemplo casting explicito
mi_valor = 1
otro_valor = str(mi_valor)
print(otro_valor)

num1 = 7.5
print(type(int(num1)))

num1 = 20
print(type(num1)) # Resultado = int
num2 = 30.9
print(type(num2)) # Resultado = floar

num1 = num1 + num2
print(type(num1)) # Resultado = float / Casting implicito. Python cambio el tipo de dato a float sin inervencion del usurio
print(num1)

num1 = int(num1) # la funcion int cambia el tipo de datos a integer. Elimina los decimales
                    # Nota: la funcion no redondea! solo quita los decimales
print(num1)
print(type(num1))

edad = input("Dime tu edad: ")
print("Tu edad es " + edad)
edad = int(edad)
nueva_edad = 1 + edad
print("vas a cumplir " + str(nueva_edad))




