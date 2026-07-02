import numpy as np
import pandas as pd
from scipy.optimize import minimize

from model import draw_curve

# Read ordered data
data = pd.read_csv("data/ordered_xy.csv")

# Create t values
t = np.linspace(6, 60, len(data))

# Error function
def find_error(values):
    theta, m, shift = values

    x, y = draw_curve(t, theta, m, shift)

    error_x = np.mean(np.abs(x - data["x"]))
    error_y = np.mean(np.abs(y - data["y"]))

    return error_x + error_y


# Starting values
start = [25, 0.02, 50]

# Limits given in assignment
bounds = [
    (0, 50),        # theta
    (-0.05, 0.05),  # M
    (0, 100)        # X
]

result = minimize(
    find_error,
    start,
    bounds=bounds,
    method="L-BFGS-B"
)

theta, m, shift = result.x

print("\nBest Parameters")
print("-" * 25)
print(f"Theta : {theta:.4f}")
print(f"M     : {m:.6f}")
print(f"Shift : {shift:.4f}")
print(f"Error : {result.fun:.6f}")