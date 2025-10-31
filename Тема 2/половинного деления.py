import math
def f(x):
    return 8 * math.cos(x) - x - 6
while True:
    print("Добро пожаловать в метод половинного деления!!!")
    a = float(input('А = '))
    b = float(input('Б = '))
    eps = float(input('Точность = '))  
    i = 0
    count = 0
    if abs(b - a) > eps: 
        while abs(b - a) > eps:
            i += 1
            c = (a + b) / 2
            fa = f(a)
            fc = f(c)
            count += 2 
            if fa * fc < 0:
                b = c
            else:
                a = c
        x = (a + b) / 2 
    else:
        x = (a + b) / 2  
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
    else:
        print(f'x = {x:.6f}')     
    print(f'Число итераций = {i}, количество вычислений = {count}')
    repeat = input("Хотите выполнить метод снова? (да/нет): ").strip().lower()
    if repeat != 'да':
        break
    else:
        print()