import matplotlib.pyplot as plt
import numpy as np

y = np.linspace(0, 30000, 10000)
x = np.linspace(1, 1000, 1000)
X, Y = np.meshgrid(x, y)
scalar =  1e-14 * np.exp(1/8500 * Y)
print(scalar)

plt.figure(figsize=(6, 5))
contour = plt.contourf(X, Y, scalar, levels=50, cmap='viridis')  # levels를 50으로 설정하여 색상 세분화
plt.colorbar(contour, label="cond")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
