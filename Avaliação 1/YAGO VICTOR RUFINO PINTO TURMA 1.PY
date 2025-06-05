

print("digite sua altura")
altura = input()
print("digite seu peso")
peso = input()

altura =float(altura)
peso =float(peso)
resultado = altura * altura
imc = peso / resultado

if imc < 18.5:
    print ("abaixo do peso")
elif imc < 24.9:
    print("peso normal")
elif imc < 29.9:
    print ("sobrepeso")
elif imc < 34.9:
    print("obsidade grau 1")
elif imc < 39.9:
    print("obsidade grau 2")
else:
    print("obsidade grau 3")
