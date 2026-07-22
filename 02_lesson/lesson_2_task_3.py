import math

def square(side):
    #Вычисляет площадь квадрата.
    #Если сторона не является целым числом, площадь округляется вверх.
    area = side * side

    if side != int(side):
        area = math.ceil(area)
    return area

# Пример вызова функции с разными сторонами

side1 = 6
side2 = 2.0
side3 = 4.2

print(f"Сторона {side1}: площадь = {square(side1)}")
print(f"Сторона {side2}: площадь = {square(side2)}")
print(f"Сторона {side3}: площадь = {square(side3)}")