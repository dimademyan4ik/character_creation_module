from math import sqrt

message = "Добро пожаловать в самую лучшую программу для вычисления \
квадратного корня из заданного числа"
print(message)


def calculatesquareroot(number):
    """Вычисляет квадратный корень"""
    if number <= 0:
        return
    root = sqrt(number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. \
Это будет: {root}')



print(message)
calculatesquareroot(25.5)
