peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print("Classificação:", classificacao)