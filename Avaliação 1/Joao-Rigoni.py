peso = float(input("Qual o seu peso(Kg): "))
altura = float (input("Qual a sua altura(Cm): "))

imc = peso /(altura ** 2)

print(f"Seu imc é: {imc: .2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobre peso")
elif imc < 35:
    print("Obesidade Grau 1")
elif imc < 40:
    print("Obesidade Grau 2")
else:
    print("Obesidade Grau 3 (morbida)")
    