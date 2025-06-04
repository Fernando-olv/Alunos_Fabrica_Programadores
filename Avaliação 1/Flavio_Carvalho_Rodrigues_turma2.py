try:
    nome = input("Digite o seu nome:")
    altura = float(input("Digite sua altura:"))
    peso = float(input("Digite o seu peso:"))
except ValueError:
    print("Digite seu peso e altura apenas em formato de numeros")
except ZeroDivisionError:
    print("Impossivel que sua altura ou peso sejam 0")
    

imc = peso / altura ** 2
imc = round(imc, 2)

if imc >= 40.0:
    print(f"{nome} seu IMC e de:{imc} você esta com Obesidade grau III(mórbida)")
    estado = "Obesidade grau III(mórbida)"

elif imc <= 18.5:
    print(f"{nome} seu IMC e de:{imc} você esta Abaixo do peso")
    estado = "Abaixo do peso"

elif imc <= 24.9:
    print(f"{nome} seu IMC e de:{imc} você esta com o Peso normal")
    estado = "Peso normal"

elif imc <= 29.9:
    print(f"{nome} seu IMC e de:{imc} você esta com sobrepeso")
    estado = "Sobrepeso"

elif imc <= 34.9:
    print(f"{nome} seu IMC e de:{imc} você esta com Obesidade grau I")
    estado = "Obesidade gra I"


elif imc <= 39.9:
    print(f"{nome} seu IMC e de:{imc} voce esta com Obesidade grau II")
    estado = "Obesidade grau II"








with open("Estado_saude.txt", "a", encoding="utf8") as arquivo:
    altura = str(altura)
    peso = str(peso)
    arquivo.write(f"Nome:{nome}|Altura:{altura}|Peso:{peso}|IMC:{imc}|Estado:{estado}\n")