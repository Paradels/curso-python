###
# 05 - Entrada de usuario (input()) - Verson simplificada
#LA funcioon input()( permite obtener usuario a traves de las consola)
###

nombre = input("Hola, ¿Como te llamas?\n") #\n es un salto de linea
print(f"Hola {nombre}, Encantado de conocerte!")

age = input("cuantos años tienes?\n")

print(f"Dentro de 20 años tendras {int(age) + 20 } años") #input() devuelve siempre un string, por lo que es necesario convertirlo a int para hacer operaciones matematicas

print("Obtener múltiples valores a la vez")
city, country = input("Introduce tu ciudad y pais: ").split()
print(f"Vives en {city}, {country}.")