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
print("МЕТОД ПРОСТЫХ ИТЕРАЦИЙ")
x = [0.0, 0.0, 0.0, 0.0]
iter = 0
while True:
    iter += 1
    x_new = [0.0, 0.0, 0.0, 0.0]
    for i in range(n):
        s = 0.0
        for j in range(n):
            if j != i:  
                s = s + a[i][j] * x[j]
        x_new[i] = (b[i] - s) / a[i][i]
    maxx = 0.0
    for i in range(n):
        error = abs(x_new[i] - x[i])
        if error > maxx:
            maxx = error
    print(f"Итерация {iter} = {maxx:.12f}")
    if maxx < e:
        print(f"Точность достигнута на итерации {iter}")
        break
    for i in range(n):
        x[i] = x_new[i]
print(f"\nРЕШЕНИЕ СИСТЕМЫ:")
print(f"x1 = {x[0]:.12f}")
print(f"x2 = {x[1]:.12f}")
print(f"x3 = {x[2]:.12f}")
print(f"x4 = {x[3]:.12f}")
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