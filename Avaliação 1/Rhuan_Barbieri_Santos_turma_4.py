nome=input("informe seu nome: ")
peso=int(input("informe seu peso: "))
altura=float(input("informe sua altura: "))

imc=peso/(altura*altura)

print(imc)

if imc <= 18.5:
    print("abaixo do peso! ")
elif imc <= 24.9:
    print("peso normal! ")
elif imc <=29.9:
    print("sobre peso! ")
elif imc <=34.9:
    print("Obesidade Grau I! ")
elif imc <=39.9:
    print("Obesidade Grau II! ")
elif imc <=40.0:
    print("Obesidade Grau III! ")
else:
    print("muito acima!! ")