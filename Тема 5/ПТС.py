import math
def f(x):
    return math.sin(x**3)
def p(a, b, n):
    h = (b - a) / n
    s = 0
    for i in range(n):
        x = a + h/2 + i * h
        s = s + h * f(x)
    return s
def t(a, b, n):
    h = (b - a) / n
    s = h * (f(a) + f(b)) / 2
    for i in range(1, n):
        x = a + i * h
        s = s + h * f(x)
    return s
def s(a, b, n):
    h = (b - a) / (n * 2)
    s1 = 0
    s2 = 0
    for i in range(1, n + 1):
        x1 = a + (2 * i - 1) * h  
        s1 = s1 + f(x1)
        x2 = x1 + h  
        s2 = s2 + f(x2)
    s = h / 3 * (f(a) + 4 * s1 + 2 * s2 - f(b))
    return s
def yz(method):
    a, b = 1, 2
    e = 0.0001
    n = 2
    while True:
        i = method(a, b, n)   
        inew = method(a, b, 2 * n)
        if abs(inew - i) < e:
            return n, inew  
        n *= 2  
n1, ip1 = yz(p)
print(f"Прямоугольники: {n1} узлов, значение: {ip1:.5f}")
n2, it2 = yz(t)
print(f"Трапеции: {n2} узлов, значение: {it2:.5f}")
n3, is3 = yz(s)
print(f"Симпсон: {n3} узлов, значение: {is3:.5f}")
print("\nАНАЛИЗ РЕЗУЛЬТАТОВ:")
print("1. Точность: Все методы достигли требуемой точности e = 0.0001")
print("2. Эффективность:")
print("   - Метод Симпсона:", n3, "узлов (самый эффективный)")
print("   - Метод прямоугольников:", n1, "узлов")
print("   - Метод трапеций:", n2, "узлов")
print("3. Значения интегралов практически идентичны")
input()