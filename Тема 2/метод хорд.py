import math
def f(x):
    return 8 * math.cos(x) - x - 6
def d2f(x):
    return -8 * math.cos(x)
while True:
    print("Добро пожаловать в метод хорд!!!")
    a = float(input("A = "))
    b = float(input("B = "))
    eps = float(input("Точность = "))
    i = 1
    if f(a) * d2f(a) > 0:
        x0 = b
        c = a
        print(f"c = a = {a}")
        print(f"x0 = b = {b}")
    else:
        x0 = a
        c = b
        print(f"c = b = {b}")
        print(f"x0 = a = {a}")
    fc = f(c)
    fx0 = f(x0)
    count = 2
    x1 = (c * fx0 - x0 * fc) / (fx0 - fc)
    if abs(x1 - x0) > eps: 
        while abs(x1 - x0) > eps:
            i += 1
            x0 = x1
            fx0 = f(x0)
            count += 1
            x1 = (c * fx0 - x0 * fc) / (fx0 - fc)
        x = x1
    else:
        x = x1 
    if eps == 0.1:
        print(f'x = {x:.1f}')
    elif eps == 0.01:
        print(f'x = {x:.2f}')
    elif eps == 0.001:
        print(f'x = {x:.3f}')
    elif eps == 0.0001:
        print(f'x = {x:.4f}')
    elif eps == 0.00001:
        print(f'x = {x:.5f}')
    elif eps == 0.000001:
        print(f'x = {x:.6f}')   
    print(f'i = {i}, кол-во вычислений = {count}')
    repeat = input("Хотите выполнить метод снова? (да/нет): ").strip().lower()
    if repeat != 'да':
        break
    else:
        print()