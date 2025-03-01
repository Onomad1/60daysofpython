def busca_linear(lista, numero_procurado):



  for i, numero in enumerate(lista):
      
      if numero == numero_procurado:
          return i
  return -1

lista = [1,2,3,4,5,6,7,9]
numero_procurado = 9

buscando_o_numero = busca_linear(lista, numero_procurado)
print(buscando_o_numero)