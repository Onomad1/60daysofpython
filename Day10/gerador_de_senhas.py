import random
import string

print(string.digits)

def gerador_de_senhas(tamanho):
        comprimento = tamanho
        caracteres = string.ascii_letters + string.digits + string.pontuation
        senha = ''
        
        while len(senha) < comprimento:
            senha += random.choice(caracteres)
            