peso = float(input("Qual é o seu peso?: (kg)"))
altura = float(input("Qual é a sua altura?: (cm)"))

imc = peso/(altura**2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5: 
    print("Abaixo do Peso")
elif imc < 25:
    print("Peso Normal")
elif imc <30: 
    print("Peso Normal")
elif imc < 35:
    print("Obesidade grau 1")
elif imc < 40:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")