car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

car["year"] = 2018

print(x)
years = "Введите свой возраст"
message = ""
while message != 'quit':
    message = int(input(years))
    if message < 3:
        print("Для вас билет бесплатный")
    elif message <= 12:
        print("Для  тебя это стоит 10$")
    elif message > 12:
        print("Твоя стоимость 15$")