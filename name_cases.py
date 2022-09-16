#family = "семья"
#print(" family == 'семья' I predict True")
#print(family == "семья")
#print(" family == 'друзья' I predict False")
#print(family == "друзья")
#print(" family != друзья I predict True")
#print(family != "друзья")
#print("family >= семья I predict True")
##age = "12"
#if age <= 4:
    #print ("Вход бесплатный")
#elif age >= 4 and age <= 18:
        #print("Вход 5$")
#else: 
    #print("Вход 10$")

alien_color = "green"
if alien_color == "green":
    print("Пришелец зеленого цвета!")
alien_color = "green"
if alien_color == "red":
    print("\nПришелец зеленого цвета?") 

color = "red"
if color == "green":
	print("\nИгрок заработал 5 очков!")
elif color == "yellow":
        print("\nИгрок заработал 10 очков!")
elif color == "red":
    print("\nИгрок заработал 15 очков!")
else:
    print("\nИгрок заработал 10 очков!")

human_life = 2
if human_life < 2:
	print("младенец")
elif 2>= human_life < 4:
  print("малыш")
elif human_life > 13 and human_life <= 20:
  print("ребенок")  
elif 13>= human_life < 20:
  print("подросток")  
elif 65> human_life >=20:
  print("взрослый")  
elif human_life >=65:
  print("пожилой человек")  
fruits = ["яблоко", "банан", "виноград", "персик"]  
if "яблоко" in fruits:
	print("Добавление яблока")
if "персик" in fruits:
	print("Добавление персик")
if "апельсин" in fruits:
	print("Добавление апельсин")	

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Пришелец перемещается вправо.
# Вычисляем величину смещения на основании текущей скорости.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
# Пришелец двигается быстро.
    x_increment = 3
# Новая позиция равна сумме старой позиции и приращения.Работа со словарями 105
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
human = {'first_name': 'Сергей', 'last_name': 'Феденков', 'age': 58, 'city': 'Печора'}
print(human['first_name'])
print(human.values())
print(human['last_name'])
print(human['age'])
print(human['city'])
human_number = {'Валерия': 4, 'Лука': 9999, 'Никита': 58, 'Варвара': 26}
for human in human_number:
    print("это любимое число у "  + human + " " + str(human_number[human]))
    termin = {}
    termin['кортеж'] = 'неизменяемый список'
    termin['строка'] = 'последовательность символов'
    termin['вещественные числа'] = 'числа имеющие дробную часть'
    termin['список'] = 'набор элементов, следующих в определенном порядке'
#print(termin) 

termin_db = {
'кортеж': 'неизменяемый список',
'строка': 'последовательность символов',
'вещественные числа': 'числа имеющие дробную часть',
'список': 'набор элементов, следующих в определенном порядке',
 }
termin_db['словарь'] = 'структура данных, предназначенная для объединения взаимосвязной информации'
for termin_0, values in termin_db.items():
    print("данное определение " + termin_0.title()  + " означает " + ":" + values)
#termin_db['словарь'] = 'структура данных, предназначенная для объединения взаимосвязной информации'
#print(termin_db)
#print("данное определение " + termin_0.title()  + " означает " + ":" + values)
river_db = {
'USA': 'Misissipi',
'Brazil':'Amazon',
'Egypt': 'Nile', 
}
for country, river in river_db.items():
    print('The ' + river + ' runs through ' + country)
for country in river_db:
    print(country)    
for river in river_db.values():
    print(river)

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
the_survey = ['andrey', 'valeria', 'sarah' ]
for name in the_survey:
    if name in favorite_languages.keys():
        print('спасибо за пройденный опрос ' + name)
    else:
        print('Пройдите опрос ' + name)

dad = {'first_name': 'Сергей', 'last_name': 'Феденков', 'age': 58, 'city': 'Печора'}
mom = {'first_name': 'Екатерина', 'last_name': 'Пугач', 'age': 51, 'city': 'Печора'}
brother = {'first_name': 'Антон', 'last_name': 'Пугач', 'age': 31, 'city': 'Печора'}
people = [dad, mom, brother]
for informaton in people:
    print (informaton)
sherry = {'Собака': 'Валерия'}
sima = {'Кошка': 'Екатерина'}     
pux = {'Кот': 'Ирина'} 
pets = [sherry, sima, pux]
for informaton in pets:
    print (informaton)

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to " + city.title() + "!")

message = "Введите возраст" #задачв №7.5
message += "\nВведите 'выйти' чтобы завершить программу"
age = " "
active = True 
while active:
   age = input(message)
if age == 'выйти':
   active = False
elif age <=3:
    print("Билет бесплатный")
elif age >= 3 and age <=12:
    print("Билет стоит 12$")
elif age >=12:
    print ("Билет стоит 15$") 
