# Usar una lista por comprensión para crear la matriz

#filas = int(input("Introduce número de filas: "))
#columnas = int(input("Introduce número de columnas: "))
filas=2
columnas=3


#matriz = [[float(input(f"Fila {i+1}, Columna {j+1}: ")) for j in range(columnas)] for i in range(filas)]

matriz = [[float(input(f"dia{i+1}, mes{j+1}: ")) for j in range(columnas)] for i in range(filas)]

may=[0]

for fila in matriz:
     for elemento in fila:
          if  elemento> may :
               may=matriz[]

     
print("[", "   ".join(f"{elemento}" for elemento in fila), "]")




for fila in matriz:
    print("[", "   ".join(f"{elemento}" for elemento in fila), "]")


print(may)
