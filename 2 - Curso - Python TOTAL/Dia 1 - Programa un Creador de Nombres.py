# -------------------------------------------------------
# Dia 1
# -------------------------------------------------------

print('Hola Mundo')
print("Hola mundo te digo 'Hola'")
print(100)  # Los numeros no necesitan comillas
print('100 + 50 = ' + str(100 + 50))
print('-------------------------------')

# Strings: Cadenas de texto
# -------------------------------
# Operaciones con strings:
# 1. Concatenar
print('Hola' + ' ' + 'Sofia')
# 2. Mostar caracteres especiales
print('Hola \'Sofia\'') # La barra invertida le dice a Python que el siguiente caracter no lo tome como texto, tomalo como caracter especial
# 3. Crear saltos de linea
print("Esta es uni linea\nY esta es otra linea")
# 4. Tabular: Agregar 4 caracteres antes del siguiente output
print('\tEsta es la tercera linea')
# 5. Escribir los caacteres especiales en una cadena the texto
print('This isn\'t a number')
print('Este signo \\ es una barra invertida')
print('--------------------------------------')

# Ejercicio:
print('A\tB\t\tC\nD\tE\t\tF\nG\tH\t\tI')
print('Barra Normal: /\nBarra Invertida: \\')
print('--------------------------------------')

# Input:
# Funcion que nos permite pedirle al usuario que escriba algo y luego poder mostrar esa informacion o almacenarla
# ------------------------------------------------------------------------------------------
print(input('Dime tu nombre: '))
print(input('Dime tu apellido: '))
print('Tu nombre es ' + input('Dime tu nombre: '))
    # Python corre el codigo de adentro hacia afuera, por lo tanto:
        # Primero correra el input y preguntara por el nombre
        # Luego correra el print e imprimira el texto + el nombre ingresado
print('Tu nombre es ' + input('Dime tu nombre: ') + ' ' + input('Dime tu apellido: '))
print('--------------------------------------')

# Proyecto:
# -----------------------
print('La cerveza se llama\n\"' + input('¿Cual es tu dip o salsa favorita? ') + ' ' + input('¿Cual es tu nacionalidad? ') + '\"')



