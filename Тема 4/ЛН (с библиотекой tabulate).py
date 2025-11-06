from tabulate import tabulate
def l1(points, x):
    x0, y0 = points[0]
    x1, y1 = points[1]
    L0 = (x - x1) / (x0 - x1)
    L1 = (x - x0) / (x1 - x0)
    return y0 * L0 + y1 * L1

def l2(points, x):
    x0, y0 = points[0]
    x1, y1 = points[1]
    x2, y2 = points[2]
    L0 = ((x - x1) * (x - x2)) / ((x0 - x1) * (x0 - x2))
    L1 = ((x - x0) * (x - x2)) / ((x1 - x0) * (x1 - x2))
    L2 = ((x - x0) * (x - x1)) / ((x2 - x0) * (x2 - x1))
    return y0 * L0 + y1 * L1 + y2 * L2

def n1(x, y, tt, st):
    h = x[1] - x[0]
    t = (tt - x[0]) / h
    if st == 1:
        delta_y0 = y[1] - y[0]
        return y[0] + t * delta_y0
    elif st == 2:
        delta_y0 = y[1] - y[0]
        delta_y1 = y[2] - y[1]
        delta2_y0 = delta_y1 - delta_y0
        result = y[0] + t * delta_y0 + (t * (t - 1) / 2) * delta2_y0
        return result

def n2(x, y, tt, st):
    h = x[1] - x[0]
    t = (tt - x[-1]) / h 
    if st == 1:
        delta_yn1 = y[-1] - y[-2]  
        return y[-1] + t * delta_yn1
    elif st == 2:
        delta_yn1 = y[-1] - y[-2] 
        delta_yn2 = y[-2] - y[-3]  
        delta2_yn2 = delta_yn1 - delta_yn2  
        result = y[-1] + t * delta_yn1 + (t * (t + 1) / 2) * delta2_yn2
        return result

print("ТЕМА 4. ИНТЕРПОЛИРОВАНИЕ И ЭКСТРАПОЛИРОВАНИЕ".center(50))
print("ФУНКЦИЙ. ПРАКТИЧЕСКОЕ ЗАНЯТИЕ.".center(50))
print("СОСТАВЛЕНИЕ ИНТЕРПОЛЯЦИОННЫХ ФОРМУЛ".center(50))
print("ЛАГРАНЖА, НЬЮТОНА.".center(50))
print("=" * 50)
n = 13
x1 = int((40 - 1.33 * n)) * 0.01
print(f"x1 = int(40 - 1.33 * n) * 0.01 = {x1:.4f}")  
x2 = int((80 + 1.57 * n)) * 0.01 
print(f"x2 = int(80 + 1.57 * n) * 0.01 = {x2:.4f}")   
x3 = int((180 - 1.15 * n)) * 0.01 
print(f"x3 = int(180 - 1.15 * n) * 0.01 = {x3:.4f}")
x = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8]
y = [1, 1.099, 1.0780, 1.1708, 1.2937, 1.4427, 1.6144, 1.8061, 2.0161, 2.2429]
print("\nТАБЛИЦА ЗНАЧЕНИЙ ФУНКЦИИ:")
table_data = [["x"] + x,["y"] + y]
print(tabulate(table_data, headers=[""] + [f"x{i}" for i in range(10)], tablefmt="grid", numalign="center", stralign="center"))

print()
print("=" * 50)
print("ЛАГРАНЖ".center(50))
print("=" * 50)
print("Формулы") 
print("L₁(x) = y₀ × (x - x₁)/(x₀ - x₁) + y₁ × (x - x₀)/(x₁ - x₀) - для 1 степени")
print("L₂(x) = y₀ × (x - x₁)(x - x₂)/((x₀ - x₁)(x₀ - x₂)) +")
print("        y₁ × (x - x₀)(x - x₂)/((x₁ - x₀)(x₁ - x₂)) +")
print("        y₂ × (x - x₀)(x - x₁)/((x₂ - x₀)(x₂ - x₁)) - для 2 степени")
print()

points_x1_1 = [[x[1], y[1]], [x[2], y[2]]]  
points_x1_2 = [[x[0], y[0]], [x[1], y[1]], [x[2], y[2]]]  
points_x2_1 = [[x[4], y[4]], [x[5], y[5]]]  
points_x2_2 = [[x[4], y[4]], [x[5], y[5]], [x[6], y[6]]] 
points_x3_1 = [[x[8], y[8]], [x[9], y[9]]]  
points_x3_2 = [[x[7], y[7]], [x[8], y[8]], [x[9], y[9]]] 

print(f"Лагранж 1 степени x1 = {l1(points_x1_1, x1):.4f}")
table_x1_1 = [
    ["x", points_x1_1[0][0], points_x1_1[1][0]],
    ["y", points_x1_1[0][1], points_x1_1[1][1]]
]
print(tabulate(table_x1_1, tablefmt="grid"))

print(f"\nЛагранж 2 степени x1 = {l2(points_x1_2, x1):.4f}")
table_x1_2 = [
    ["x", points_x1_2[0][0], points_x1_2[1][0], points_x1_2[2][0]],
    ["y", points_x1_2[0][1], points_x1_2[1][1], points_x1_2[2][1]]
]
print(tabulate(table_x1_2, tablefmt="grid"))

print(f"\nЛагранж 1 степени x2 = {l1(points_x2_1, x2):.4f}")
table_x2_1 = [
    ["x", points_x2_1[0][0], points_x2_1[1][0]],
    ["y", points_x2_1[0][1], points_x2_1[1][1]]
]
print(tabulate(table_x2_1, tablefmt="grid"))

print(f"\nЛагранж 2 степени x2 = {l2(points_x2_2, x2):.4f}")
table_x2_2 = [
    ["x", points_x2_2[0][0], points_x2_2[1][0], points_x2_2[2][0]],
    ["y", points_x2_2[0][1], points_x2_2[1][1], points_x2_2[2][1]]
]
print(tabulate(table_x2_2, tablefmt="grid"))


print(f"\nЛагранж 1 степени x3 = {l1(points_x3_1, x3):.4f}")
table_x3_1 = [
    ["x", points_x3_1[0][0], points_x3_1[1][0]],
    ["y", points_x3_1[0][1], points_x3_1[1][1]]
]
print(tabulate(table_x3_1, tablefmt="grid"))

print(f"\nЛагранж 2 степени x3 = {l2(points_x3_2, x3):.4f}")
table_x3_2 = [
    ["x", points_x3_2[0][0], points_x3_2[1][0], points_x3_2[2][0]],
    ["y", points_x3_2[0][1], points_x3_2[1][1], points_x3_2[2][1]]
]
print(tabulate(table_x3_2, tablefmt="grid"))
print()

print("=" * 50)
print("НЬЮТОН".center(50))
print("=" * 50)
table_data = [
    [0.0, 1.0000, 0.0990, -0.1200],
    [0.2, 1.0990, -0.0210, 0.1138],
    [0.4, 1.0780, 0.0928, 0.0301],
    [0.6, 1.1708, 0.1229, 0.0261],
    [0.8, 1.2937, 0.1490, 0.0227],
    [1.0, 1.4427, 0.1717, 0.0200],
    [1.2, 1.6144, 0.1917, 0.0183],
    [1.4, 1.8061, 0.2100, 0.0168],
    [1.6, 2.0161, 0.2268, ""],
    [1.8, 2.2429, "", ""]
]

print("Таблица разностей")
print(tabulate(table_data, headers=['x', 'y', 'Δy', 'Δ²y'], tablefmt="grid"))

print("Формулы")
print("Pₙ(x) = y₀ + t × Δy₀ + [t(t-1)/2!] × Δ²y₀ + ... + [t(t-1)...(t-n+1)/n!] × Δⁿy₀ - Первая интерполяционная")
print("Pₙ(x) = yₙ + t × Δyₙ₋₁ + [t(t+1)/2!] × Δ²yₙ₋₂ + ... + [t(t+1)...(t+n-1)/n!] × Δⁿy₀ - Вторая интерпполяционная")

x_x1 = [x[1], x[2]]  
y_x1 = [y[1], y[2]]  
print(f"\nНьютон 1 степени x1 = {n1(x_x1, y_x1, x1, 1):.4f}")
table_x1_1 = [
    [0.2, 1.0990, -0.0210],
    [0.4, 1.0780, ""]
]
print(tabulate(table_x1_1, headers=['x', 'y', 'Δy'], tablefmt="grid"))

x_x1_2 = [x[0], x[1], x[2]]  
y_x1_2 = [y[0], y[1], y[2]]  
print(f"\nНьютон 2 степени x1 = {n1(x_x1_2, y_x1_2, x1, 2):.4f}")
table_x1_2 = [
    [0.0, 1.0000, 0.0990, -0.1200],
    [0.2, 1.0990, -0.0210, ""],
    [0.4, 1.0780, "", ""]
]
print(tabulate(table_x1_2, headers=['x', 'y', 'Δy', 'Δ²y'], tablefmt="grid"))

x_x2 = [x[4], x[5]]  
y_x2 = [y[4], y[5]]  
print(f"\nНьютон 1 степени x2 = {n1(x_x2, y_x2, x2, 1):.4f}")
table_x2_1 = [
    [0.8, 1.2937, 0.1490],
    [1.0, 1.4427, ""]
]
print(tabulate(table_x2_1, headers=['x', 'y', 'Δy'], tablefmt="grid"))

x_x2_2 = [x[4], x[5], x[6]]  
y_x2_2 = [y[4], y[5], y[6]]  
print(f"\nНьютон 2 степени x2 = {n1(x_x2_2, y_x2_2, x2, 2):.4f}")
table_x2_2 = [
    [0.8, 1.2937, 0.1490, 0.0227],
    [1.0, 1.4427, 0.1717, ""],
    [1.2, 1.6144, "", ""]
]
print(tabulate(table_x2_2, headers=['x', 'y', 'Δy', 'Δ²y'], tablefmt="grid"))

x_x3 = [x[8], x[9]]  
y_x3 = [y[8], y[9]]  
print(f"\nНьютон 1 степени x3 = {n2(x_x3, y_x3, x3, 1):.4f}")
table_x3_1 = [
    [1.6, 2.0161, 0.2268],
    [1.8, 2.2429, ""]
]
print(tabulate(table_x3_1, headers=['x', 'y', 'Δy'], tablefmt="grid"))

x_x3_2 = [x[7], x[8], x[9]]  
y_x3_2 = [y[7], y[8], y[9]]  
print(f"\nНьютон 2 степени x3 = {n2(x_x3_2, y_x3_2, x3, 2):.4f}")
table_x3_2 = [
    [1.4, 1.8061, 0.2100, 0.0168],
    [1.6, 2.0161, 0.2268, ""],
    [1.8, 2.2429, "", ""]
]
print(tabulate(table_x3_2, headers=['x', 'y', 'Δy', 'Δ²y'], tablefmt="grid"))

print()
print("=" * 50)
print("ОБЩИЙ РЕЗУЛЬТАТ".center(50))
print("=" * 50)

data = [
    ["x1 = 0.2200", 
     l1(points_x1_1, x1),
     l2(points_x1_2, x1),
     n1(x_x1, y_x1, x1, 1),
     n1(x_x1_2, y_x1_2, x1, 2)],
    
    ["x2 = 1.0000",
     l1(points_x2_1, x2),
     l2(points_x2_2, x2),
     n1(x_x2, y_x2, x2, 1),
     n1(x_x2_2, y_x2_2, x2, 2)],
    
    ["x3 = 1.6500",
     l1(points_x3_1, x3),
     l2(points_x3_2, x3),
     n2(x_x3, y_x3, x3, 1),
     n2(x_x3_2, y_x3_2, x3, 2)]
]

print(tabulate(data, 
               headers=["Точка", "Лагранж 1ст", "Лагранж 2ст", "Ньютон 1ст", "Ньютон 2ст"],
               tablefmt="grid",
               floatfmt=".4f"))

input()