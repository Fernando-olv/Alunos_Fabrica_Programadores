nome = input("Digite o nome do usuario: ")
try:
        peso = float(input("Digite o peso do usuario: "))
        altura = float(input("Dige a altura do usuario: "))

        imc = peso /(altura * altura)

        if imc <= 18.5:
                print("Abaixo do peso")
        elif imc <= 24.9:
                print("Peso normal")
        elif imc <= 29.9:
                print("Sobrepeso")
        elif imc <= 34.9:
                print("Obesidade Grau 1")
        elif imc <= 39.9:
                print("Obesidade Grau 2")
except Exception as e:
        print("Ocorreu um erro.\nDetalhes do erro:",e)