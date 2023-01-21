entrada = "falso"

while not entrada.isnumeric():
    entrada = input("Digite um número: ")
    
entrada = int(entrada)

if entrada < 10:
    print("O número é menor que 10")

if (entrada % 2) == 0:
    print("O número é par")

if entrada >= 8 and entrada <= 16:
    print("O número está entre 8 e 16")

if entrada == 51 or entrada == 81:
    print("O número é 51 ou 80")      

