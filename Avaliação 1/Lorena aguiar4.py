peso= float(input("Qual o seu peso?:"))
altura= float(input("Qual a sua altura?:"))

imc = peso/(altura**2)

print (f"seu IMC é: {imc:.2f}")

if imc < 18.5: 
    print("abaixo do peso") 
elif imc < 24.9: 
    print("peso normal")
elif imc < 29.9:
    print("sobrepeso")
elif imc < 34.9:
    print ("obesidade grau II")
elif imc < 39.9:
    print ("obsidade grau II")

else:
    print ("obesidade grau III")