import math
def f(x):
    return 8 * math.cos(x) - x - 6
def phi(x):
    return 8 * math.cos(x) - 6
while True:
    print("Добро пожаловать в метод простой итерации")   
    ainterval = float(input('A = '))
    binterval = float(input('B = '))
    eps = float(input('Точность = '))
    q = float(input('Q = ')) 
    a_param = eps * (1 - q) / q
    if abs(phi(ainterval) - ainterval) < abs(phi(binterval) - binterval):
        x0 = ainterval
    else:
        x0 = binterval
    print(f"x0 = {x0}")
    x = x0
    y = phi(x)   
    count = 1  
    i = 1      
    while abs(x - y) > a_param:
        i+= 1
        x = y
        y = phi(x)
        count += 1
    x = y  
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
    print(f'Количество итераций = {i}, Количество вычислений = {count}') 
    repeat = input("Хотите выполнить метод снова? (да/нет): ").strip().lower()
    if repeat != 'да':
        break
    else:
        print()