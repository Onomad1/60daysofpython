entrada = input("Digite o número: ")

try:
    numero = int(entrada)
    if numero % 2 == 0:
      print("Este número é par")
    else:
      print("Este numero é impar")
except ValueError:
    print("Voc~e não passou um inteiro")