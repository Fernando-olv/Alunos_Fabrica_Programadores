peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))
imc = peso / (altura* altura)

if imc <= 18.5:
    print ("Abaixo do peso, está ok.")

elif imc <= 24.0:
    print("Peso normal, está tudo ok.")

elif imc <= 29.9:
    print("Sobrepeso, porém cuidado com a saúde.")

elif imc <= 34.9:
    print("Obeso.")

elif imc <= 39.9:
    print("Imenso")

else: 
    print("Stretched")