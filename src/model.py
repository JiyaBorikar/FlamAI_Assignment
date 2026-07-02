import numpy as np

def curve(t, theta, m, shift):

    theta = np.radians(theta)

    x = (
        t * np.cos(theta)
        - np.exp(m * np.abs(t)) * np.sin(0.3 * t) * np.sin(theta)
        + shift
    )

    y = (
        42
        + t * np.sin(theta)
        + np.exp(m * np.abs(t)) * np.sin(0.3 * t) * np.cos(theta)
    )

    return x, y