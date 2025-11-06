x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8]
y = [1.0000, 1.0990, 1.0780, 1.1708, 1.2937, 1.4427, 1.6144, 1.8061, 2.0161, 2.2429]
y_new = []
delta = []
for i in range(len(y) - 1):
    y_new.append(y[i+1]-y[i])
for i in range(len(y_new) - 1):
    delta.append(y_new[i+1]-1)
print("x")
for num in x:
    print(f"{num:.4f}", end=" ")
print()  
print("y")
for num in y:
    print(f"{num:.4f}", end=" ")
print()
print("delta y")
for num in y_new:
    print(f"{num:.4f}", end=" ")
print()
print("delta y2")
for num in delta:
    print(f"{num:.4f}", end=" ")
print()