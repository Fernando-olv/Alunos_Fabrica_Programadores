nome = input("Qual é o seu nome \n")

meta = int(input("Qual a sua meta\n"))

peso = int(input("Qual o seu peso\n"))
altura = float(input("Qual a sua altura\n"))

calculo = peso/ (altura * altura)

if calculo <= 18.5:
    print("Abaixo do peso")
elif  calculo <= 24.9:
    print("Peso Normal")
elif  calculo <= 29.9:
    print("Sobre Peso")
elif  calculo <= 34.9:
    print("Obesidade Level 1")
elif calculo <= 39.9:
    print("Obesidade Level 2")
elif  calculo <= 40:
    print("Obesidade Level 3")
else: 
    print("Oloco meu, ta fazendo PVP com a Thais carla")

print(f"Este é seu IMC {calculo:.2f}" )

peso_ideal = 24 * altura * altura

resto = meta - peso
peso_ideal2 = peso - peso_ideal
print(f"Relaxa só falta isso {resto}")
print(f"Falta {peso_ideal2:.2f} chegar no peso normal")
