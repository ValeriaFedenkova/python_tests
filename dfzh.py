	

# def trangle_exception(a, b, c):
# 	a = input()
# 	b = input()
# 	c = input()
#     raise TypeError("Число должно быть целым.")
#         print ("Число должно быть целым.")
#     if  a < 0 and b < 0 and c < 0:
#         raise ValueError("Число должно быть неотрицательным.")
#         print ("Число должно быть неотрицательным.")
#         def triangle_type(a, b ,c):
#     if (a, b, c(type, int)):
#         return 'a, b, с'
#     else:
#        raise TypeError("Число должно быть целым.")
#        print ("Число должно быть целым.")
def triangle(a, b, с):
    if a + b >= c and a + c >= b and b + c >= a:
        print('Треугольник существует') 
    else: 
        print('Треугольник не существует')   
def triangle_terms(a, b ,c): 
    if a == b == c:
        print('Треугольник равносторонний')
    elif a == b or a == c or c == b:
        print ('Треугольник равнобедренный')
    elif c**2 == a ** 2 + b ** 2 or a ** 2 == c ** 2 + b**2 or b**2 == a**2 + c**2:
        print ('Треугольник прямоугольный')