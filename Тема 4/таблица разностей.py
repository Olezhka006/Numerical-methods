x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8]
y = [1.0000, 1.0990, 1.0780, 1.1708, 1.2937, 1.4427, 1.6144, 1.8061, 2.0161, 2.2429]
delta_y = []
for i in range(len(x)-1):
    delta_y.append(y[i+1] - y[i])
delta2_y = []
for i in range(len(x)-2):
    delta2_y.append(delta_y[i+1] - delta_y[i])
print("x     y       Δy      Δ²y")
print("-" * 30)
for i in range(len(x)):
    line = f"{x[i]:.1f}  {y[i]:.4f}"
    if i < len(delta_y):
        line += f"  {delta_y[i]:.4f}"
    else:
        line += "        "
    if i < len(delta2_y):
        line += f"  {delta2_y[i]:.4f}"
    print(line)
input()