import math

N = 13
alpha_val = 2 / N
n = 4
e = 10 ** -11
a = [[5.8, 0.2, 1.3, 0.7 + alpha_val],[4, 6.3 + alpha_val, 0.9, 1],[2, 1.3, 5 + alpha_val, 0.5],[1 + alpha_val, 2.5, 3.3, 9]]
b = [1.9 + 4.8 * alpha_val,0.8 + 4 * alpha_val,9.5 + 4 * alpha_val,alpha_val**2 + alpha_val - 2.4]

print("Матрица A:")
for i in range(n):
    for j in range(n):
        print(f"{a[i][j]:.4f}", end=" ")
    print()

print("\nВектор B:")
for i in range(n):
    print(f"{b[i]:.4f}", end=" ")
print()

print(f"\nТочность: {e:.11f}")
print("МЕТОД ЗЕЙДЕЛЯ")


x = [0.0, 0.0, 0.0, 0.0]
iterations = 0

while True:
    iterations += 1
    x_old = [x[0], x[1], x[2], x[3]]
    
    for i in range(n):
        s = 0.0
        for j in range(n):
            if j != i:  
                s = s + a[i][j] * x[j]  
        x[i] = (b[i] - s) / a[i][i]  
    
    
    maxx = 0.0
    for i in range(n):
        error = abs(x[i] - x_old[i])
        if error > maxx:
            maxx = error
    
    print(f"Итерация {iterations} = {maxx:.12f}")
    
    if maxx < e:
        print(f"Точность достигнута на итерации {iterations}")
        break

print(f"\nРЕШЕНИЕ СИСТЕМЫ (найдено за {iterations} итераций):")
for i in range(n):
    print(f"x{i+1} = {x[i]:.12f}")

print("ПРОВЕРКА РЕШЕНИЯ")
for i in range(n):
    result = 0.0
    print(f"Уравнение {i+1}:")
    for j in range(n):
        product = a[i][j] * x[j]
        print(f"  {a[i][j]:.4f} * {x[j]:.6f} = {product:.6f}")
        result = result + product
    print(f"  Сумма: {result:.8f}")

input()