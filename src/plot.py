import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/xy_data.csv")

plt.figure(figsize=(7, 7))
plt.scatter(data["x"], data["y"], s=8)

plt.title("Curve")
plt.xlabel("X")
plt.ylabel("Y")

plt.grid(True)
plt.axis("equal")
plt.savefig("results/curve.png")
plt.show()