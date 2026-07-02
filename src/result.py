import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from model import curve

# Read data
data = pd.read_csv("data/ordered_xy.csv")

# Final values
theta = 30.0437
m = 0.029991
shift = 55.0155

# t values
t = np.linspace(6, 60, len(data))

# Generate curve
x, y = curve(t, theta, m, shift)

plt.figure(figsize=(7, 7))

plt.plot(data["x"], data["y"], label="Given Curve")
plt.plot(x, y, "--", label="Generated Curve")

plt.title("Curve Comparison")
plt.xlabel("X")
plt.ylabel("Y")

plt.legend()
plt.grid(True)
plt.axis("equal")

plt.savefig("results/comparison.png")

plt.show()