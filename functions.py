from math import sqrt

def plos_square(a, b):
    plos = a * b
    print(f"Площадь прямоугольника равна {plos}")

def plos_round(r):
    plosr = 3.14 * r ** 2
    print(f"Площадь круга равна {plosr}")  

def plos_triangle(a, b, c):
    import math
    p = (a + b + c) / 2
    plost = sqrt((a - p) * (b - p) * (c - p))
    print(f"Площадь треугольника равна {plost}")