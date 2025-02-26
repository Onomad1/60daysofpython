def contador_personaliado():
    try:
        limite = int(input("Digite um valor máximo: "))
        #a função range cria uma lista de números a partir do zero.
        #
        limite = limite + 1
        for i in range(limite):
            print(i)
            if i == limite:
                print("Limite atingido")
                break
    except ValueError:
        print('por favor digite algo válido')
        
contador_personaliado()