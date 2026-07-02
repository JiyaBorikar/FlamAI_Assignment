import numpy as np
import pandas as pd
from scipy.optimize import minimize

from model import curve

# Read ordered data
data = pd.read_csv("data/ordered_xy.csv")

# t values
t = np.linspace(6, 60, len(data))


def error(values):
    theta, m, shift = values

    x, y = curve(t, theta, m, shift)

    x_error = np.mean(np.abs(x - data["x"]))
    y_error = np.mean(np.abs(y - data["y"]))

    return x_error + y_error


# Starting values
guess = [25, 0.02, 50]

# Limits
limits = [
    (0, 50),
    (-0.05, 0.05),
    (0, 100)
]

result = minimize(
    error,
    guess,
    bounds=limits,
    method="L-BFGS-B"
)

theta, m, shift = result.x

print("\nFinal Values:")
print(f"Theta : {theta:.4f}")
print(f"M     : {m:.6f}")
print(f"X     : {shift:.4f}")
print(f"Error : {result.fun:.6f}")