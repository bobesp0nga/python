# Soy un comentario
print("hola  mundo")
"""
nada me la pela
"""
# variables
texto = "Repaso de python"
nombre = "Ivan"
altura = "1,82"
year = 2023

print(f"{texto} - {nombre} {str(year)}")
print(texto + " - " + nombre +" - " + altura + " - " + str(year) )
# Entrada
#sitioweb = input("¿Cual es tu pagina web?: ")
#print("El sitio web del ususario es: " + sitioweb)
#  Conidicones
altura = int(input("¿Cual es tu altura?: "))
if altura >= 180:
    print("Eres una persona alta!!")
else:
    print("Eres bajito!!")