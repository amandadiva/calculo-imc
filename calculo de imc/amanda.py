peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

IMC = peso / (altura ** 2)

print("Seu IMC é:", round(IMC, 2))

if IMC > 25:
    print("Acima do peso")
else:
    print("Peso normal")