print('Insira sua altura:')
altura = input()
print('insira seu peso:')
peso = input()

altura = float(altura)
peso = float(peso)

resultado = altura * altura
imc = peso / resultado

if imc >= 40:
    situacao = 'Obesidade Grau III (mórbida)' 
elif imc > 34.9:
    situacao = 'Obesidade Grau II'
elif imc > 29.9:
   situacao = 'Obesidade Grau I'
elif imc > 24.9:
    situacao  = 'Sobrepeso'
elif imc > 18.5:
    situacao = 'Peso normal'
else:
    print = 'Abaixo do peso'

with open("imc.txt", "a", encoding="utf-8") as media_arquivo:
    media_arquivo.write(f"{altura} com imc {imc:.1f} está: {situacao}\n")
