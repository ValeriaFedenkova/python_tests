
# sandwich_orders = ['Бокадильо', 'Арепа', 'Крок-мадам', 'Донер-кебаб', 'Кацу-сандо']  

# finished_sandwiches = []
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     print('Я сдела тебе сендвич ' + sandwich)
#     finished_sandwiches.append(sandwich)
# print("Вот список сендвичей, которые я согу сделать:")
# for san in finished_sandwiches:
#     print(san)

# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
# # Проверяем каждого пользователя, пока остаются непроверенные
# # пользователи. Каждый пользователь, прошедший проверку,
# # перемещается в список проверенных.
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print("Verifying user: " + current_user.title())
#     confirmed_users.append(current_user)
# # Вывод всех проверенных пользователей.
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())
# sandwich_orders = ['pastrami','Бокадильо', 'Арепа', 'Крок-мадам', 'pastrami', 'Донер-кебаб','pastrami', 'Кацу-сандо']
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print ('pastrami закончился, но есть:' )
# print (sandwich_order)

# response = {}
# vacation_active = True
# while vacation_active:
#     name = input('Как Вас зовут?')
#     question = input('Где вы проведете отпуск?' + name)
#     response[name] = question
# print('Результаты опроса') 
# for name, question in response.items():
#     print(name + "поедет в отпуск на" + question)
# response = {}
# vacation_active == True
# while vacation_active:
#     name = input('Как Вас зовут?')
#     question = input('Где вы проведете отпуск?' + name)
#     response[name] = question
#     repeat = input('Хотите ли вы продолжить опрос?(да/нет)')
# if repeat == 'нет':
#     vacation_active = False 
# print('Результаты опроса') 
# for name, question in response.items():
#     print(name + "поедет в отпуск на" + question)
# def greet_user(username):
# #"""Выводит простое приветствие."""
#     print("Hello, " + username.title() + "!")
# greet_user('jesse')
# def display_message(information_message):
#     print("Это информация по главе: " + information_message)
# display_message("Иногда в литературе термины «аргумент» и «параметр» используются как синонимы") 
# def favorite_book(title):
#     print("One of my favorite books is " + title )
# favorite_book('Alice in Wonderland')   
# def make_shirt(text, size = "L"):
#     print("эта футболка размера " + size + " с надписью: " + text)
# make_shirt(text = "I love Python")   
# def build_person(first_name, last_name):
# #"""Возвращает словарь с информацией о человеке."""
#     person = {'first': first_name, 'last': last_name}
#     return person
# musician = build_person('jimi', 'hendrix')
# print(musician)
# # def get_formatted_name(first_name, last_name):
# # #"""Возвращает аккуратно отформатированное полное имя."""
# #     #full_name = first_name + ' ' + last_name
# #     #return full_name.title()
# # # Бесконечный цикл!
# # #while True:
# #     #print("\nPlease tell me your name:")
# # #f_name = input("First name: ")
# # l_name = input("Last name: ")
# # formatted_name = get_formatted_name(f_name, l_name)
# # print("\nHello, " + formatted_name + "!")

# def city_country(city, country):
#     full_name = city + " " + country
#     return full_name.title()
# list_city_country = city_country("москва", "россия")
# print(list_city_country)
# list_city_country1 = city_country("Токио", "япония")
# list_city_country2 = city_country("Минск", "Беларусь")
# print(list_city_country1)
# print(list_city_country2)

# def make_album(song, albom, treck = " "):
#     information = {"name_song": song, "name_albom": albom}
#     if treck:
#         information['treck'] = treck
#     return information
# musician = make_album('Foals', 'Luna', treck = 1 )
# print(musician)
# def make_album(song, albom, treck = " "):
#     information = {"name_song": song, "name_albom": albom}
#     if treck:
#         information['treck'] = treck
#     return information
# musician = make_album('Foals', 'Luna', treck = 1 )
# print(musician)

# def make_album(song, albom):
#     general_name = song + ' ' + albom  
#     return general_name
# while True:
#     print('\nВведите название любимой группы:')
#     print('Введите название любимого альбома:')
#     a_song = input('название группы')
#     if a_song == 'стоп':
#         break
#     a_albom = input('название альбома')
#     if a_albom == 'стоп':
#          break
            
#     general = make_album(a_song, a_albom)
#     print('У тебя хороший вкус, если ты слушаешь' + general)
#     name = []
#     def first_name(name):
# def show_magicians(names):
#     for name in names:
#         msg = "Hello, " + name.title()
#         print(msg)
# name_magicifns=['Альберт', 'Варфоломей', 'Фредерик', 'Патрик']
# show_magicians(name_magicifns)
 
def make_great(ame_magicifns, mag_new):
    while ame_magicifns:
        mag_newes = ame_magicifns.pop()
        print(mag_newes)
        mag_new.append(mag_newes)
def show_magicians(mag_new):
    for name in mag_new:
        print(name)
ame_magicifns=['Альберт', 'Варфоломей', 'Фредерик', 'Патрик'] 
mag_new = []
#     for n in names:
#         nanes_mag = "Great" + n
#         print(nanes_mag)

# ame_magicifns=['Альберт', 'Варфоломей', 'Фредерик', 'Патрик'] #список имен фокусников 
# mag_new = []
# make_great(name_magicifns[:], mag_new)

#####################################################################################

# def show_magicians(names):
#     for name in names:
#         msg = "Hello, " + name + "!"
#         print(msg)
# name_magicifns = ['Альберт', 'Варфоломей', 'Фредерик', 'Патрик'] 
# show_magicians(name_magicifns)
#####################################################################################
#Передача списка
# def greet_users(names):
#     for name in names:
#         msg = "Hello, " + name.title() + "!"
#         print(msg)
# usernames = ['hannah', 'ty', 'margot']   #Мы определяем список пользователей usernames, который затем передается greet_
# users() в вызове функции:
# greet_users(usernames)

#Изменение списка в функции
#Список моделей, которые необходимо напечатать
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Цикл последовательно печатает каждую модель до конца списка.
# После печати каждая модель перемещается в список completed_models.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Печать модели на 3D-принтере.
    print("Printing model: " + current_design)
    completed_models.append(current_design)
# Вывод всех готовых моделей.    
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
    

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
#параметры треугольника
def triangle(a, b, с):
    if a + b > c and b + c > a and a + c > b:
        return "Тругольник существует"
triangle(1, 2, 1)