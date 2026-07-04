# Flam AI - Research & Development Assignment

**Name:** Jiya Borikar  
**Course:** B.Tech Computer Science and Engineering (Artificial Intelligence)  
**College:** Amrita Vishwa Vidyapeetham

---

## Objective

The objective of this assignment was to estimate the unknown parameters (θ, M and X) of the given parametric equation using the provided dataset.

---

## Approach

1. Explored the dataset and checked for missing values.
2. Plotted the given points to understand the curve.
3. Observed that directly optimizing the parameters resulted in a high error.
4. Reordered the points using a nearest-neighbor approach to reconstruct the curve.
5. Implemented the given parametric equation in Python.
6. Used numerical optimization to estimate the unknown parameters by minimizing the L1 distance.
7. Compared the generated curve with the reconstructed curve.

---

## Estimated Parameters

| Parameter | Value |
|-----------|--------:|
| θ | **30.0437°** (0.52436 radians) |
| M | **0.029991** |
| X | **55.0155** |

Final L1 Error:

```
0.302291
```

---

## Final Parametric Equation

```latex
\left(
t\cos(0.52436)-e^{0.029991|t|}\sin(0.3t)\sin(0.52436)+55.0155,\;
42+t\sin(0.52436)+e^{0.029991|t|}\sin(0.3t)\cos(0.52436)
\right)
```

Parameter Range

```
6 ≤ t ≤ 60
```

---

## Repository Structure

```
data/
    xy_data.csv

src/
    explore.py
    plot.py
    order.py
    model.py
    solve.py
    result.py

results/
    comparison.png
```

---

## Libraries Used

- NumPy
- Pandas
- Matplotlib
- SciPy

---

## Result

The estimated parameters generated a curve that closely matches the provided dataset with a final L1 error of **0.302291**.
