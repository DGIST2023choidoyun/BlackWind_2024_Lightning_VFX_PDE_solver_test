from pde import CartesianGrid, ScalarField, PDE, MemoryStorage
import numpy as np
import matplotlib.pyplot as plt
import pyvista as pv

sigma_0 = 1e-14
epsilon_0 = 8.854 * 1e-12

H = 60000 # height of ionosphere

x_0, y_0, z_0 = 0, 0, 0
V_0 = 100
q_0 = -25 # same as a paper ref


tau_c = 0.02   # characteristic time <= 20ms
exponential_factor = sigma_0/epsilon_0    # sigma0/epsilon0 * e^{2*kappa*z}  Assuming ground conductivity = 1E-14
kappa = 1/(2*5000)   # 2K = scale height

eq = PDE({"PI": f"1/{tau_c} * laplace(PI) - 100 * (laplace(PI) + 2 * {kappa} * d_dz(PI))"})

grid = CartesianGrid([[-100, 100], [-100, 100], [0, 1000]], shape=[64, 64, 64])

initial_field = ScalarField.from_expression(grid, f"{V_0} * (1 - exp(-2 * {kappa} * z)) / (1 - exp(-2 * {kappa} * {H})) + ({q_0} * exp(-{kappa} * (z - {z_0})) / (4 * pi * {epsilon_0})) * ((exp(-{kappa} * sqrt((x - {x_0})**2 + (y - {y_0})**2 + (z - {z_0})**2)) / sqrt((x - {x_0})**2 + (y - {y_0})**2 + (z - {z_0})**2)) - (exp(-{kappa} * sqrt((x - {x_0})**2 + (y - {y_0})**2 + (z + {z_0})**2)) / sqrt((x - {x_0})**2 + (y - {y_0})**2 + (z + {z_0})**2)))")

storage = MemoryStorage()

result = eq.solve(initial_field, t_range=1.0, dt=0.01)


data = result.data  # 결과 스칼라 필드 데이터
x = np.linspace(-100, 100, grid.shape[0])
y = np.linspace(-100, 100, grid.shape[1])
z = np.linspace(0, 1000, grid.shape[2])

# 3D grid를 pyvista로 변환
grid_pv = pv.StructuredGrid(*np.meshgrid(x, y, z, indexing="ij"))
grid_pv["PI"] = data.flatten(order="F")  # pyvista는 Fortran 스타일로 정렬된 데이터가 필요함

# 3D 볼륨 플로팅
plotter = pv.Plotter()
plotter.add_volume(grid_pv, scalars="PI", opacity="sigmoid", cmap="viridis")
plotter.show()