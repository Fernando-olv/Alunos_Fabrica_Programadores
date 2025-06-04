# CALCULADORA DE IMC COM CATEGORIZAÇÃO
# ENTREGA ATÉ 06/06/2025                            nome:Emanuelly Gomes de Souza
# FAZER UM FORK E UM PULL REQUEST PARA ENTREGAR     turma:anacleto turma |

input("digite o seu nome: ")
peso = float (input("digite seu peso: " ))
altura = float (input ("digite sua altura: "))

imc = peso /(altura * altura)
if imc <= 18.5:
    print ("abaixo do peso")
elif imc <= 24.9:
    print ("peso normal ")
elif imc <= 29.9:
    print ("sobrepeso")
elif imc <= 34.9:
    print ("obesidade grau |")
elif imc <= 39.9:
    print ("obesidade grau ||")
else:
    print ("obesidadegrau |||")

print("""
▄───▄
█▀█▀█
█▄█▄█
─███──▄▄
─████▐█─█
─████───█
─▀▀▀▀▀▀▀
▄───▄
█▀█▀█
█▄█▄█
─███──▄▄
─████▐█─█
─████───█
─▀▀▀▀▀▀▀
█▀█▀█
█▄█▄█
─███──▄▄
─████▐█─█
─████───█
─▀▀▀▀▀▀▀\n""")
