peso = float (input("Me diga seu peso"))
altura = float (input("Me diga a sua altura"))

imc = peso /(altura*altura)

if imc >=30.0:
    print("Cuidado com a saúde!")
elif imc <18.5:
    print ("Abaixo do peso")
elif imc < 24.9:
    print("Peso normal")
elif imc < 29.9:
    print("Sobrepeso")
elif imc < 34.9:
    print ("Obesidade Grau 1")
elif imc < 39.9:
    print ("Obesidade Grau 2")
else:
    print ("Obesidade Grau 3(Mórbida)")