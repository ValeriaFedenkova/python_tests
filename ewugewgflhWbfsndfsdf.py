def triangle_type(a, b, c):
    if type(a) is not int and type(b) is not int and  type(c) is not int:  
        raise TypeError  #пошел в жопу тогда
    else: 
        print("норм")
def triangle(a, b, c):
    if a + b > c and a + c > b and c + b > a:
        print ("Треугольник существует")
    else:
        print ("Треугольник не существует")
def triangle_terms(a, b, c):
    if a == b == c:
        print ("Треугольник равносторонний")
    elif a == b or a == c or c == b:
        print ("Треугольник равнобедренный")      
    elif c**2 == a**2 + b**2  or a**2 == c**2 + b**2 or b**2 == c**2 + a**2:
        print ("Треугольник прямоугольный")
triangle_type(2, 2, 2)
triangle(2, 2, 2)
triangle_terms(2, 2, 2)