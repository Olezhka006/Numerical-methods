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
    # Сохраняем старые значения для сравнения
    x_old = [x[0], x[1], x[2], x[3]]
    
    print(f"\n--- Итерация {iterations} ---")
    
    # Вычисляем x1 
    s = a[0][1]*x[1] + a[0][2]*x[2] + a[0][3]*x[3]
    print(f"x1 = ({b[0]:.4f} - ({a[0][1]:.4f}*{x[1]:.6f} + {a[0][2]:.4f}*{x[2]:.6f} + {a[0][3]:.4f}*{x[3]:.6f})) / {a[0][0]:.4f}")
    print(f"x1 = ({b[0]:.4f} - {s:.6f}) / {a[0][0]:.4f}")
    x[0] = (b[0] - s) / a[0][0]
    print(f"x1 = {x[0]:.6f}")
    
    # Вычисляем x2 
    s = a[1][0]*x[0] + a[1][2]*x[2] + a[1][3]*x[3]
    print(f"x2 = ({b[1]:.4f} - ({a[1][0]:.4f}*{x[0]:.6f} + {a[1][2]:.4f}*{x[2]:.6f} + {a[1][3]:.4f}*{x[3]:.6f})) / {a[1][1]:.4f}")
    print(f"x2 = ({b[1]:.4f} - {s:.6f}) / {a[1][1]:.4f}")
    x[1] = (b[1] - s) / a[1][1]
    print(f"x2 = {x[1]:.6f}")
    
    # Вычисляем x3 
    s = a[2][0]*x[0] + a[2][1]*x[1] + a[2][3]*x[3]
    print(f"x3 = ({b[2]:.4f} - ({a[2][0]:.4f}*{x[0]:.6f} + {a[2][1]:.4f}*{x[1]:.6f} + {a[2][3]:.4f}*{x[3]:.6f})) / {a[2][2]:.4f}")
    print(f"x3 = ({b[2]:.4f} - {s:.6f}) / {a[2][2]:.4f}")
    x[2] = (b[2] - s) / a[2][2]
    print(f"x3 = {x[2]:.6f}")
    
    # Вычисляем x4 
    s = a[3][0]*x[0] + a[3][1]*x[1] + a[3][2]*x[2]
    print(f"x4 = ({b[3]:.4f} - ({a[3][0]:.4f}*{x[0]:.6f} + {a[3][1]:.4f}*{x[1]:.6f} + {a[3][2]:.4f}*{x[2]:.6f})) / {a[3][3]:.4f}")
    print(f"x4 = ({b[3]:.4f} - {s:.6f}) / {a[3][3]:.4f}")
    x[3] = (b[3] - s) / a[3][3]
    print(f"x4 = {x[3]:.6f}")
    maxx = 0.0
    for i in range(n):
        error = abs(x[i] - x_old[i])
        if error > maxx:
            maxx = error
    if maxx < e:
        print(f"Точность достигнута на итерации {iterations}")
        break

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