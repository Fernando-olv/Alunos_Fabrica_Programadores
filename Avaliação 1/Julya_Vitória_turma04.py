nome = input("Digite o nome: ")
peso = float(input("Qual o seu peso? (kg): "))
altura = float(input("Qual a sua altura? (m): "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

# Determina a categoria do IMC
if imc < 18.5:
    categoria = "Abaixo do peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Sobrepeso"
elif imc < 35:
    categoria = "Obesidade grau 1"
elif imc < 40:
    categoria = "Obesidade grau 2"
else:
    categoria = "Obesidade grau 3"

print(categoria)

# Salva os dados no arquivo txt
with open("imc.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"Nome: {nome} | Peso: {peso} kg | Altura: {altura} m | IMC: {imc:.2f} | Categoria: {categoria}\n")
