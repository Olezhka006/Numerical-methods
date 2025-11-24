import math
def f(x, y):
    return 1 + 0.3 * y * math.sin(x) - 1.7 * y**2
def rk4(x, y, b, h):
    n = int((b - x) / h)
    print(f"x = {x:.6f}, y = {y:.8f}")
    for i in range(1, n + 1):
        r1 = h * f(x, y)
        r2 = h * f(x + h/2, y + r1/2)
        r3 = h * f(x + h/2, y + r2/2)
        r4 = h * f(x + h, y + r3)
        y = y + (r1 + 2*r2 + 2*r3 + r4) / 6
        x = x + h
        print(f"x = {x:.6f}, y = {y:.8f}")
    return x, y
print("Метод Рунге-Кутты 4-го порядка")
print("=" * 60)
x0 = 0.0
y0 = 0.0
b = 1.0
h = 0.1
epsilon = 0.000001
print(f"x0 = {x0}, \ny0 = {y0}, \nb = {b}, \nh = {h}, \neps = {epsilon}, \nf(x, y) = 1 + 0.3 * y * sin(x) - 1.7 * y^2")
print("=" * 60)
z = 0 #для пред значения
print("Проход с h =", h)
x, y = rk4(x0, y0, b, h)
z = y
while True:
    h /= 2
    print(f"\nПроход с h1 = {h}")
    x, y = rk4(x0, y0, b, h)
    p = (1/30) * abs(z - y)
    z = y
    if p < epsilon:
        print("\n" + "=" * 60)
        print("Точность достигнута!!!!!")
        print(f"Финальный результат: y = {y:.8f}")
        break
input()