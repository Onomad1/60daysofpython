num = int(input("Digite um número para verificar se ele é primo: "))

primo = True

if num <= 1:
    primo = False
    
    
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        primo == False
        break
    
if primo:
    print(f"{num} é um número primo")
    
else:
        print(f"{num} não é um número primo")