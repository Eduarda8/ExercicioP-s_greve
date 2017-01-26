Qtd_Pizza = int(input("Quantas pizzas o senhor irá pedir ?:"))
Preço = float(input("Digite o preço da pizza que está no cardápio:"))
SemImposto = Qtd_Pizza * Preço
#A taxa de imposto é de 8%
Imposto = SemImposto * (8.0/100)
ComImposto = SemImposto + Imposto

print("O valo total cobrado da(s) pizza(s) é de:",ComImposto)
