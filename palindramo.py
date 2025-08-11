def PalabraPalindramo(cadena):
     if  not isinstance(cadena,str):
          return "ingrese cadena valida "
     
     x=len(cadena)
     print("longitud de la cadena",x)
     print("palabra ingresada:",cadena)
     band=True
     if x%2==0 :# % operador del resto
          n=0
          j=1
          while n<=x/2 and band==True:
               if cadena[n]==cadena[-j]:
                    band=True
                    print(cadena[n])
               else:
                    band=False
                    
               n=n+1
               j=j+1

     else:
          n=0
          j=1
          while n<(x/2)+1 and band==True:
               if cadena[n]==cadena[-j]:
                    band=True
               else:
                    band=False
               n=n+1
               j=j+1
               
     if band==True:
          return True
     else:
          return False
          
print("la palabra  ingresada  es un palindramo.. ? : ",PalabraPalindramo('anana'))

