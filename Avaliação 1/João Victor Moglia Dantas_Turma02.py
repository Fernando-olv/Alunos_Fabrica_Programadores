nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / altura ** 2

if imc <= 18.5:
    print("Abaixo do peso")
elif imc <= 24.9:
    print("peso normal")
elif imc <= 29.9:
    print("Sobrepeso")
elif imc <= 34.9:
    print("Obesidade grau 1")
elif imc <= 39.9:
    print("Obesidade grau 2")
elif imc >= 40.0:
    print("Obesidade grau 3 (mórbida)")
else:
    "Sinistro"