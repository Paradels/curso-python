##
# 04 - Variables
# Las variables serven para guardar datos y reutilizarlos a lo largo del código.
###

my_name = "Luis Paradela"

print(my_name)

age = 27
print(age)  

age = age + 1
print(age)

# Tipado dinámico: el tipo de dato se determina en tiempo de ejecución (  tipado dinamico )
# que no tienes que declarar el tipo de dato de la variable
name = "Luis"
print(type(name))
name = 27
print(type(name))

# Tipado fuerte: no se pueden mezclar tipos de datos sin convertirlos explícitamente ( tipado fuerte )
# print (10 + "2")

#f-strings ( formatted strings ) (literal de cadena de formato)
print(f"Hola {my_name}, tienes {age } años.")

#Convenciones de variables
# - No usar palabras reservadas ( if, else, for, while, def, return)

mi_nombre_de_variable = "Luis" #snake_case

MiNombreDeVariable = "Luis" #PascalCase (No usar)

MI_CONSTANTE = 3.1416 #Mayusculas y guion bajo (constantes)( aunque no existen constantes en python )

