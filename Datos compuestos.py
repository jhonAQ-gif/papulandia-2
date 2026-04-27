#creando una lista (se pueden modificar)
lista = ["Lucas Dalto", "Soy Dalto", True,1.85, "Soy Dalto"]


#creando una tupla (no pueden modificar) tupla = ("Lucas Dalto", "Soy Dalto", True, 1.85, "Soy Dalto")
tupla = ("Lucas Dalto", "Soy Dalto", True,1.85, "Soy Dalto")


#esto es vàlido 
lista[3] = "Maquinola"
#para llamar a lista: print(lista[3])

#esto no:
#tupla[3] = "Maquinola"


#creando un conjunto (set) (no se accede a elementos por indice, no almacena datos duplicados) 
conjunto = {"Lucas Dalto", "Soy Dalto", True,1.85, "Soy Dalto"}
#print(conjunto[3]) -> no puede acceder al elemento
