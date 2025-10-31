import math
def f(x):
    return 8 * math.cos(x) - x - 6
def df(x):
    return -8 * math.sin(x) - 1
while True:
    print("Добро пожаловать в метод касательных!!!")
    a = float(input('А = '))
    b = float(input('Б = '))
    eps = float(input('Точность = '))
    i = 1
    count = 0
    fa = f(a)
    fb = f(b)
    d2fa = -8 * math.cos(a)  
    d2fb = -8 * math.cos(b)  
    if fa * d2fa > 0:
        x0 = a
    elif fb * d2fb > 0:
        x0 = b
    print(f"x0 = {x0}")
    fx = f(x0)
    dfx = df(x0)
    count += 2
    x_new = x0 - fx / dfx
    if abs(x_new - x0) > eps: 
        while abs(x_new - x0) > eps:  
            i += 1
            x0 = x_new
            fx = f(x0)
            dfx = df(x0)
            count += 2    
            x_new = x0 - fx / dfx
        x = x_new
    else:
        x = x_new  
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
    print(f'i = {i}, количество вычислений = {count}')
    repeat = input("Хотите выполнить метод снова? (да/нет): ").strip().lower()
    if repeat != 'да':
        break
    else:
        print()