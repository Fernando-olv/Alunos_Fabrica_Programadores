peso = float(input("qual é seu peso?; (Kg)"))
altura= float(input("Qual é sua altura?"))

imc = peso/ (altura**2) 

print(f"seu imc é: {imc:.2f}")

if imc < 18.5:
    print ("abaixo do preço")
elif imc < 24.9:
    print ("peso normal")
elif imc < 29.9:
    print ("sobrepeso")
elif imc < 34.9:
    print ("obesidade grau 1")
elif imc < 39.9:
    print ("obesidade grau 2")

else:
    print("obesidade grau 3")