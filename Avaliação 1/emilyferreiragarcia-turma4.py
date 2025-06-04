print ('qual sua altura')
altura = input ()
print ('qual seu peso')
peso = input ()

altura = float (altura)
peso = float (peso)


altura_final = altura * altura 
altura_final = float (altura_final)
imc = peso / altura_final 
print ('seu imc é', imc)
if imc <18.5:
    print('Abaixo do peso')
elif imc <24.9:
    print('Peso normal')
elif imc <29.9:
    print ("Sobrepeso")
elif imc <34.9:
    print ("Obesidade Grau 1")
elif imc <39.9:
    print ("Obesidade Grau 2")
else:
    print ('Obesidade Grau 3')