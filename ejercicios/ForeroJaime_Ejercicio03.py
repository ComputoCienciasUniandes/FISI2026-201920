# Primer punto
#1. (10 puntos) Inicializar una cadena de caracteres (en mayúsculas 
# sin espacios) e imprimir en pantalla si se trata de un palíndromo o no.
print("Punto 1")
cadena = "ARTETRA"
n_total = len(cadena)
n_iguales = 0

for i in range(n_total):    
    if cadena[i] == cadena[-i-1]:
        n_iguales = n_iguales + 1
if n_iguales == n_total:
    print("La palabra ", cadena, " si es palindroma")
else:
    print("La palabra ", cadena, " no es palindroma")
print("")
# 2. (20 puntos ) Inicializar la siguiente cadena de caracteres DNA="ATGTCTCATTGAACCAGTCCCTA" 
# e imprimir el porcentaje de veces que se encuentra cada uno de los caracteres.
print("Punto 2")
DNA="ATGTCTCATTGAACCAGTCCCTA" 
letras_unicas = list(set(DNA))
n_total = len(DNA)

for letra in letras_unicas:
    p = 100*DNA.count(letra)/n_total
    print("La letra ", letra,"se encuentra el ", p, " por ciento de las veces")

# 3. (20 puntos) Inicializar la siguiente lista ListaGenes = 
# ["ACTCAGTATA", "TGTACAGATA", "TGTATCGCGA", "ATGTCTCTAT"] e imprimir 
# las secuencias de 3 letras se repiten más de una vez junto al número de veces que se repiten.

ListaGenes = ["ACTCAGTATA", "TGTACAGATA", "TGTATCGCGA", "ATGTCTCTAT"] 
trios_todos = []
print("")

#primero hago la lista de todos los trios posibles
print("Punto 3")
for gen in ListaGenes:
    n_bases = len(gen)
    for i in range(n_bases-2):
        trios_todos.append(gen[i]+gen[i+1]+gen[i+2])

trios_unicos = list(set(trios_todos))
for trio in trios_unicos:
    n_in = 0
    for t in trios_todos:
        if trio==t:
            n_in = n_in +1

    if n_in > 1:
        print("El trio ", trio, "se encuentra", n_in, "veces")
print("")


# 4. (10 puntos) Usando el resultado de readlines(), imprima en pantalla cuántas lineas hay en el archivo the_raven_poe.txt
print("Punto 4")
filename = "the_raven_poe.txt"
raven = open(filename, "r")
raven_lineas = raven.readlines()
raven.close()

n_lineas = len(raven_lineas)
print(filename, "tiene", n_lineas, "lineas")
print("")

# 5. (10 puntos) Usando el resultado de readlines(), imprima en pantalla cuántas palabras hay en el archivo the_raven_poe.txt 
print("Punto 5")
raven_palabras = []
for linea in raven_lineas:
    raven_palabras = raven_palabras + linea.split()

n_palabras = len(raven_palabras)
print(filename, "tiene", n_palabras, "palabras")
print("")

# 6. (10 puntos) Usando el resultado de readlines(), imprima en pantalla cuántas letras hay en el archivo the_raven_poe.txt

print("Punto 6")
n_letras = 0
for palabra in raven_palabras:
    n_letras += len(palabra)
print(filename, "tiene", n_letras, "letras")
print("")

# 7. (20 puntos) Usando el resultado de readlines(), imprima en pantalla las palabras diferentes que empiezan con "h" o con "H".

print("Punto 7")
h_palabras = []
for palabra in raven_palabras:
    palabra.lower()
    if "h"==palabra[0]:
        h_palabras.append(palabra)

h_palabras_unicas = list(set(h_palabras))
print("Las palabras que empiezan por h o H son:", h_palabras_unicas)
print("")
