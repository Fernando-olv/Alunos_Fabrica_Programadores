peso = int(input("qual é o seu peso:\n"))
altura = float (input("qual á sua altura\n"))

calculo = peso / (altura * altura)

if calculo >= 40:
        print(f"c tá gigante man ☠️  {calculo:.2f}")
elif calculo > 39:
        print(f"você ta ficando grande dms😥{calculo:.2f}")
elif calculo > 34.9:
        print(f"grande🤨 {calculo:.2f}")
elif calculo > 29.9:
        print(f"sobrepeso🤠 {calculo:.2f}")
elif calculo > 24.9:
        print(f"peso normal👍🏽 {calculo:.2f}")
elif calculo > 18.5:
        print(f"abaixo do peso 🦟 {calculo:.2f}")

peso_ideal = 24 * altura * altura
print(f"tudo ok👍🏽 ")

