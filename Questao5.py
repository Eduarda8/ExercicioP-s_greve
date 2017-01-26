Cigarro = int(input("Quantos cigarros você fuma por dia ?:"))
Anos =int(input("Há quantos anos você fuma ?:"))
Min = 0
for a in range (1, Cigarro + 1):
    Min = Min + 10
VidaPerdida = (Anos *365) * Min

print("Por fumar todo esse tempo, você perdeu", VidaPerdida,"minutos de sua vida. Cuidado o cigarro mata!!")
