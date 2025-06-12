altura = float ( input ("digite o sua altura ") )
peso = float ( input ("digite seu peso") )

imc =  peso / (altura * altura )

if imc >= 40.0:
    print ("obesidade grau III")
elif imc >= 39.9:
    print ("obesidade grau II")
elif imc >= 34.9:
    print ("obesidade grau I")
elif imc >= 29.9:
    print ("sobrepeso")
elif imc >= 24.9:
    print ("peso normal")
else: 
    print ("baixo do peso")