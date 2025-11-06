x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8]
y = [1.0000, 1.0990, 1.0780, 1.1708, 1.2937, 1.4427, 1.6144, 1.8061, 2.0161, 2.2429]
y_new = []
delta = []
for i in range(len(y) - 1):
    y_new.append(y[i+1] - y[i])
for i in range(len(y_new) - 1):
    delta.append(y_new[i+1] - y_new[i])
print("x       y       y_new   delta")
for i in range(len(x)):
    x_str = f"{x[i]:.4f}"
    y_str = f"{y[i]:.4f}"
    if i < len(y_new):
        y_new_str = f"{y_new[i]:.4f}"
    else:
        y_new_str = ""
    if i < len(delta):
        delta_str = f"{delta[i]:.4f}"
    else:
        delta_str = ""
    print(f"{x_str}  {y_str}  {y_new_str}  {delta_str}")
input()