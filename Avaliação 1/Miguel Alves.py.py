# CALCULADORA DE IMC COM CATEGORIZAÇÃO
# ENTREGA ATÉ 06/06/2025
# FAZER UM FORK E UM PULL REQUEST PARA ENTREGAR

print("insira sua altura")
altura = input()
print("insira seu peso")
peso = input()

altura = float(altura)
peso = float(peso)

resultado = altura * altura
imc = peso/resultado

if imc < 18.5:
    print("abaixo do peso")

elif imc < 24.9:
    print("peso normal")

elif imc < 29.9:
    print("sobrepeso")

elif imc < 34.9:
    print("obesidade I")

elif imc < 39.9:
    print("obesidade II")

else: 
    print("obesidade III")

