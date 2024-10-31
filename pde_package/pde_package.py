from pde import CartesianGrid, ScalarField, PDE, MemoryStorage, plot_kymograph
import numpy as np
import matplotlib.pyplot as plt

# Define constants
tau_c = 0.02   # characteristic time <= 20ms
exponential_factor = 11.29    # sigma0/epsilon0 * e^{2*kappa*z}  Assuming ground conductivity = 1E-14
kappa = 1/(2*30)   # 1/2K = scale height

# Define the PDE with the corrected syntax for the z-derivative
eq = PDE({"PI": f"1/{tau_c} * laplace(PI) - {exponential_factor}*exp(2*{kappa}*y) * (laplace(PI) + 2 * {kappa} * d_dy(PI))"})

# Set up the grid
grid = CartesianGrid([[0, 100], [0, 30]], shape=[64, 64])  # define the spatial domain and resolution

# PInitialize the field with zeros
initial_field = ScalarField(grid, np.zeros(grid.shape))  # initialize PI with zero

# Prepare storage for results
storage = MemoryStorage()

# Solve the PDE
result = eq.solve(initial_field, t_range=1.0, dt=0.01)

# Plot the xy-plane data
plt.imshow(result.data.T, extent=[0, 100, 0, 30], origin='lower', cmap='viridis')
plt.colorbar(label='PI')
plt.xlabel('x')
plt.ylabel('y')
plt.title('PI in 2D')
plt.show()