import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data/xy_data.csv")

points = data[["x", "y"]].to_numpy()

used = np.zeros(len(points), dtype=bool)

# Start from leftmost point
index = np.argmin(points[:, 0])

new_points = []

for i in range(len(points)):
    new_points.append(points[index])
    used[index] = True

    dist = np.linalg.norm(points - points[index], axis=1)
    dist[used] = np.inf

    index = np.argmin(dist)

new_points = np.array(new_points)

new_data = pd.DataFrame(new_points, columns=["x", "y"])
new_data.to_csv("data/ordered_xy.csv", index=False)

plt.figure(figsize=(7, 7))

plt.plot(new_points[:, 0], new_points[:, 1])
plt.scatter(new_points[:, 0], new_points[:, 1], s=2)

plt.title("Ordered Curve")
plt.xlabel("X")
plt.ylabel("Y")

plt.grid(True)
plt.axis("equal")

plt.show()

print("Ordered data saved")