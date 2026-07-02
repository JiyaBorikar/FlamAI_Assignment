# Flam AI Research & Development Assignment

**Name:** Jiya Borikar  
**College:** Amrita Vishwa Vidyapeetham  
**Course:** B.Tech CSE (AI)

## Objective

The goal of this assignment is to estimate the unknown parameters (θ, M and X) of the given parametric curve using the provided dataset of x and y coordinates.

---

## Project Structure

```
FlamAI_Assignment
│
├── data
│   ├── xy_data.csv
│   └── ordered_xy.csv
│
├── src
│   ├── explore.py
│   ├── plot.py
│   ├── order.py
│   ├── model.py
│   ├── solve.py
│   └── result.py
│
├── results
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Steps Followed

1. Loaded and explored the dataset.
2. Plotted the given points to understand the curve.
3. Observed that the points were not in the correct order.
4. Reconstructed the curve by ordering the nearest points.
5. Implemented the given parametric equation in Python.
6. Used numerical optimization to estimate the unknown values.
7. Compared the generated curve with the given curve.

---

## Libraries Used

- Python
- NumPy
- Pandas
- Matplotlib
- SciPy

---

## Estimated Parameters

Theta : 30.0437°

M : 0.029991

X : 55.0155

Final Error : 0.302291

---

## Desmos Equation

```text
(t*cos(30.0437)-e^(0.029991*abs(t))*sin(0.3*t)*sin(30.0437)+55.0155,
42+t*sin(30.0437)+e^(0.029991*abs(t))*sin(0.3*t)*cos(30.0437))
```

---

## Output

The final generated curve closely matches the given dataset after reconstructing the point order and optimizing the unknown parameters.