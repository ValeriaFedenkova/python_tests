#import this
name = 'валерия феденкова'
#print (name.upper())
#print (name.lower())
#print (name.title())
famous_person = "  валерия феденкова "
message = "да это я пою"
#print ( "'" + message + "'" +  "\n"  + " " + famous_person.lstrip().title())
#print(16/2)
#print(2*4)
#print(6+2)
#print(26-18)
number = "4"
#print("Мое любимое число" + " " + str(number))
freinds = ["Полина", "Галина", "Оксана", "Александр", "Дмитрий"]
#print(freinds[0], freinds[1], freinds[2], freinds[3], freinds[4] )
#print("Привет мой друг", freinds[0] )
#print("Привет мой друг", freinds[1] )
#print("Привет мой друг", freinds[2] )
#print("Привет мой друг", freinds[3] )
#print("Привет мой друг", freinds[4] )

guests = ["Chester Bennington", "Ada Laveles", "Альберт Энштейн"]
#print("Приглашаю Вас на ужин", guests[2] )
##print("Не сможет прийти", guests[0] )
cancellation = guests.pop(0)
#print(guests)
no_guests = "Ada Laveles"
guests.remove(no_guests)
#print("\n этот гость " + no_guests.title() + " не сможет прийти")
guests.insert(0, "Сергей Владимирович")
guests.append("Антон Александрович")
guests.insert(3, "Екатерина Ивановна")
#print(guests)
#print("Приглашаю Вас на ужин", guests[0] )
#print("Приглашаю Вас на ужин", guests[1] )
#print("Приглашаю Вас на ужин", guests[2] )
#print("Приглашаю Вас на ужин", guests[3] )
#countries = ["япония", "нидерланды", "китай", "италия", "франция" ]
#print(countries)                                                    #1 исходный список
#print(sorted(countries))                                            #2 список в алфавитном порядке
#print(countries)                                                    #3 исходный список
#print(sorted(countries, reverse=True))                              #4 список в обратном алфавитном порядке
#print(countries)                                                    #5 исходный список
#countries.reverse()                                                 
#print(countries)                                                    #6 список обратный алфавитному порядку                                             
#countries.reverse()
#print(countries)                                                    #7 список обратный обратному списку алфавитного порядка
#countries.sort()
#print(countries)                                                    #8 список в алфавитном порядке исходному списку(изменениям не подлежит)
#countries.sort(reverse=True)                                               
#print(countries)                                                    #9 список в обратном алфавитном порядке исходному списку(изменениям не подлежит)
#print(len(countries))
#pizzas = ["американка", "четыре сыра", "пепперони", "карбанара"]
#for pizza in pizzas:
    #print("I like " + pizza)
#print("I really love pizza!")
#nimals = ["собака", "кошка", "тигр", "волк"]
#for animal in animals:
	#print(animal.title())
	#print("Одно из лучших животных " + animal)
#print("Все животные очень классные!")
#for k in range(1,21):
	#print(k)

#i = list(range(1,1000001))
#print(min(i))
#print(max(i))
#for x in range(3,30,3):
	#print(x) 
#cube = [value**3 for value in range(1,11)]	
#print(cube)

my_foods = ['piz', 'falafel', 'carrot cake', 'ice cream', 'cannoli' ]
print("The first three items in the list are::")
print(my_foods[:3])
print("Three items from the middle of the list are:::")
print(my_foods[1:4])
print("The last three items in the list are::")
print(my_foods[-3:])
my_pizza = ["американка", "четыре сыра", "пепперони", "карбанара"]
friend_pizzas = my_pizza[:]
my_pizza.append("мясная")
friend_pizzas.append("гаваяская")
print("My favorite pizzas are:")
for pi in my_pizza:
    print(pi)
print("My friend’s favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)
age = 10
age > 10 or age == 10
names = ["admin", "михаил", "николай", "варвара", "кристина"]
for name in names:
	if name == "admin":
		print ("Hello admin, would you like to see a status report?")
	else:
		print("Hello Eric, thank you for logging in again")
namest = []
if namest:
    for n in namest:
        print("gaergfEFSED")
else:
	print("We need to find some users!")

current_users = ["дэвид", "Андрей", "павел", "анатолий", "валерия"]
new_users = ["лидия", "андрей", "сергей", "ирина", "валерия"]
for new_user in new_users:
	if new_user.lower() in [i.lower() for i in current_users]:
	
		print("Выбирите другое имя " + new_user + " занято!")
	else:
		print("имя доступно " + new_user)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]		
for i in numbers:
	if i == 1:
		print(str(i) + "st")
	elif i == 2:
		print(str(i) + "nd")
	elif i == 3:
		print(str(i) + "rd")
	else:
		print(str(i) + "th")
#prompt = "\nTell me something, and I will repeat it back to you:"
#prompt += "\nEnter 'quit' to end the program. "
#message = ""
#while message != 'quit':
#message = input(prompt)

	#if message != 'quit':
#print(message)		
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
	city = input(prompt)
	if city == 'quit':
		break
else:
	print("I'd love to go to " + city.title() + "!")