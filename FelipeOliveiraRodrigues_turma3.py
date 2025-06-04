nome = input("qual seu vulgo o indigente??\n")
idade = int(input("idade do corno??\n"))
peso= float(input("qual seu peso????\n"))
altura = float(input("qual sua altura???\n"))
imc = peso / (altura * altura)
while True:
    if imc <= 18.5:
        print("chassi de grilo")
        print(imc)
    elif imc <= 24.9:
       print("gente normal")
    elif imc <= 29.9:
        print("sore peso")
    elif imc <= 34.9:
        print("imenso")
    elif imc <= 39.9:
        print("slk")
    else:
        print("pqp mlk kkkkk")
