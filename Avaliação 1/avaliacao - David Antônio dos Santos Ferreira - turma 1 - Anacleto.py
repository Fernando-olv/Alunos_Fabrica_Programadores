# CALCULADORA DE IMC COM CATEGORIZAÇÃO
# ENTREGA ATÉ 06/06/2025                                                David Antônio Dos Santos Ferreira           Anacleto            Turma 1
# FAZER UM FORK E UM PULL REQUEST PARA ENTREGAR

nome = input("Digite seu nome: ")
peso = input("Digite seu peso: ")
altura = input("Digite sua altura: ")

try:
    peso = float(peso)
    altura = float(altura)
    imc = peso / (altura * altura)
    
except ValueError:
    print("Erro de valor.")
    exit()
except TypeError:
    print("Use apenas números! ")
    exit()
except Exception:
    print("Erros de conta. ")
    exit()

if imc <= 18.5:
    print("Nome do pasciente: ", nome, "\n","Situação: Abaixo do peso. ")

elif imc <= 24.9:
    print("Nome do pasciente: ", nome, "\n", "Situação: Peso normal. ")

elif imc <= 29.9:
    print("Nome do pasciente: ", nome, "\n", "Situação: Sobre peso. ")

elif imc <= 34.9:
    print("Nome do pasciente: ", nome, "\n", "Situação: Obsidade Grau I. ")

elif imc <= 39.9:
    print("Nome do pasciente: ", nome, "\n", "Situação: Obsidade Grau II. ")

else:
    print("Nome do pasciente: ", nome, "\n", "Situação: Obsidade Grau III. ")