def eh_palidromo(texto):
    if texto == texto[::-1]:
        print("oi")

texto = input("Digite uma palavra: ")
texto = str(texto).replace(" ","").lower()
print(texto[::-1])

