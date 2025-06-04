# CALCULADORA DE IMC COM CATEGORIZAÇÃO
# ENTREGA ATÉ 06/06/2025
# FAZER UM FORK E UM PULL REQUEST PARA ENTREGAR
nome = input("digite seu nome: ")

peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))


imc = peso / (altura * altura)

if imc <= 18.5:
    situação = "abaixo do peso"

elif imc <= 24.9:
    situação = "peso normal"

elif imc <= 29.9:
    situação = "sobre peso"

elif imc <= 34.9:
    situação = "obesidade grau I"

elif imc <= 39.9:
    situação = "obesidade grau II"

else:
    situação = "obesidade grau 3(morbida)"


print(situação)