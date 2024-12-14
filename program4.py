import math

# Запрашиваем коэффициенты у пользователя
a = float(input("Введите коэффициент a (a ≠ 0): "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))
if a == 0:
    print("Коэффициент a не должен быть равен 0.")
else:
    D = b**2 - 4*a*c
    print(f"Дискриминант D = {D}")
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(f"Уравнение имеет два корня: x1 = {x1}, x2 = {x2}")
    elif D == 0:
        x = -b / (2 * a)
        print(f"Уравнение имеет один корень: x = {x}")
    else:
        print("Нет корней")