def g(a, b):
    n=4
    matrix=[]
    for i in range(n):
        row = [a[i][0], a[i][1], a[i][2], a[i][3], b[i]]
        matrix = matrix + [row]
    for i in range(n):
        if matrix[i][i]==0:
            for j in range(i+1, n):
                if matrix[j][i]!=0:
                    matrix[i],matrix[j]=matrix[j],matrix[i]
                    break
        for j in range(i + 1, n):
            coeff = matrix[j][i]/matrix[i][i]
            for k in range(i,n+1):
                matrix[j][k]=matrix[j][k]-coeff*matrix[i][k]

    print("МАТРИЦА (ТРАПЕЦЕВИДНАЯ):")
    for i in range(n):
        for j in range(n):
          print(round(matrix[i][j], 4), end=" ")
        print("|", round(matrix[i][n], 4))
    print()

    x=[0]*n
    for i in range(n - 1, -1, -1):
        x[i]=matrix[i][n]/matrix[i][i]
        for j in range(i-1,-1,-1):
            matrix[j][n]=matrix[j][n]-matrix[j][i]*x[i]
    return x

def check(a, x, b):
    for i in range(len(a)):
        result = 0
        print(f"Уравнение {i+1}:")
        for j in range(len(x)):
            product = a[i][j] * x[j]
            print(f"{a[i][j]} * {x[j]:.3f} = {product:.3f}")
            result = result + product
        print(f"Сумма: {result:.3f}")
        print()

alpha = 2 / 13
a = [[5.8, 0.2, 1.3, 0.7 + alpha],[4, 6.3 + alpha, 0.9, 1],[2, 1.3, 5 + alpha, 0.5],[1 + alpha, 2.5, 3.3, 9]]
b = [1.9 + 4.8 * alpha,0.8 + 4 * alpha,9.5 + 4 * alpha,alpha**2 + alpha - 2.4]
print("A:")
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print()
print("Б:", b)
print()
x = g(a, b)
print("РЕШЕНИЕ СИСТЕМЫ:")
print(f"x1 = {x[0]:.3f}")
print(f"x2 = {x[1]:.3f}")
print(f"x3 = {x[2]:.3f}")
print(f"x4 = {x[3]:.3f}")
print()
print("ПРОВЕРКА:")
check(a, x, b)
input()