import matplotlib.pyplot as plt
import numpy as np

y = np.linspace(0, 30000, 10000)
k = np.linspace(0, 1/60000, 1000)
K, Y = np.meshgrid(k, y)
scalar =  1e-14 * np.exp((2*K) * Y)
print(scalar)

plt.figure(figsize=(10, 5))
contour = plt.contourf(K, Y, scalar, levels=50, cmap='viridis')  # levels를 50으로 설정하여 색상 세분화
plt.colorbar(contour, label="cond")
plt.xlabel("kappa")
plt.ylabel("Y")
plt.show()

y = np.linspace(0, 30000, 10000)
h = np.linspace(1000, 10000, 1000)
H, Y = np.meshgrid(h, y)
scalar =  1e-14 * np.exp(Y/H/30)

plt.figure(figsize=(10, 5))
contour = plt.contourf(H, Y, scalar, levels=50, cmap='viridis')  # levels를 50으로 설정하여 색상 세분화
plt.colorbar(contour, label="cond")
plt.xlabel("scale height")
plt.ylabel("Y")
plt.show()
