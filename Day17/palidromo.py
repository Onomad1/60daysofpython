def eh_palidromo(texto):  
   texto = str(texto).replace(" ","").lower()
   
   if texto == texto[::-1]:
       return f"{texto} é um palidromo"
   return f"{texto} não é um paloidromo"

print(eh_palidromo(input("Digite uma palavra: ")))