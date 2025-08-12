vector=[['17693604', 'kiko', True, True, 'ooperacion apendicitis', True, 'diabetes', True, 'metformina', True], [True, '', True, True, '4', True, '2', True, 'riesgo'], [True, True, True, True, True, True, True, True, True]]

print(len(vector))

baux=[]
for  i in range(0,len(vector)):
     aux=(vector[i])
     for j in range(0,len(aux)):
          baux.append(aux[j])

print("datos del afiliado",baux)
     
           
