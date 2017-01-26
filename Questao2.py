Numero = int(input("Digite um número:"))
Fatorial = 1

for a in range (1, Numero):
    Fatorial = Fatorial * Numero
    Numero = Numero - 1
print(Fatorial)
