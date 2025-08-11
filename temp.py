# Usar una lista por comprensión para crear la matriz

#filas = int(input("Introduce número de filas: "))
#columnas = int(input("Introduce número de columnas: "))
filas=2
columnas=2

#matriz = [[float(input(f"Fila {i+1}, Columna {j+1}: ")) for j in range(columnas)] for i in range(filas)]

matriz = [[int(input(f"dia{i+1}, mes{j+1}: ")) for j in range(columnas)] for i in range(filas)]

may=0

print(matriz)

for fila in matriz:
     for elemento in fila:
          if  elemento> may :
               print(elemento)

     
print("[", "   ".join(f"{elemento}" for elemento in fila), "]")




for fila in matriz:
    print("[", "   ".join(f"{elemento}" for elemento in fila), "]")


print(may)
