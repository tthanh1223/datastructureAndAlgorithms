import numpy as np
import random


def random_gauss(mean, std):
    """Generates a Gaussian-distributed random number."""
    return random.gauss(mean, std)


def rectify(value):
    """Ensures that the value stays within the range [0, 1]."""
    return max(0, min(value, 1))


def mid_disp_2d(R, x, y, w, h, c1, c2, c3, c4, std, roughness):
    """
    2D midpoint displacement algorithm for fractal terrain generation.

    Parameters:
        R (2D array): The grid storing height values.
        x, y (int): Coordinates of the top-left corner of the rectangle.
        w, h (int): Width and height of the current rectangle.
        c1, c2, c3, c4 (float): Corner values of the current rectangle.
        std (float): Standard deviation for random displacement.
        roughness (float): Factor to control roughness (0 < roughness < 1).
    """
    newW = w // 2
    newH = h // 2

    if w > 1 or h > 1:
        disp = random_gauss(0.0, std) * roughness

        # Calculate the edges and midpoint
        mid = ((c1 + c2 + c3 + c4) / 4) + disp
        e1 = (c1 + c2) / 2
        e2 = (c2 + c3) / 2
        e3 = (c3 + c4) / 2
        e4 = (c4 + c1) / 2

        # Ensure values are within the range [0, 1]
        mid = rectify(mid)
        e1 = rectify(e1)
        e2 = rectify(e2)
        e3 = rectify(e3)
        e4 = rectify(e4)

        # Recursively displace the sub-rectangles
        mid_disp_2d(R, x, y, newW, newH, c1, e1, mid, e4, std / 2, roughness)
        mid_disp_2d(R, x + newW, y, w - newW, newH, e1, c2, e2, mid, std / 2, roughness)
        mid_disp_2d(R, x + newW, y + newH, w - newW, h - newH, mid, e2, c3, e3, std / 2, roughness)
        mid_disp_2d(R, x, y + newH, newW, h - newH, e4, mid, e3, c4, std / 2, roughness)
    else:
        # Base case: assign a value to the grid
        p = (c1 + c2 + c3 + c4) / 4
        R[x, y] = p * 255
        if w == 2:
            R[x + 1, y] = p * 255
        if h == 2:
            R[x, y + 1] = p * 255
        if w == 2 and h == 2:
            R[x + 1, y + 1] = p * 255


# Initialize parameters and grid
size = 257  # Size must be 2^n + 1 for proper recursion (e.g., 257 = 2^8 + 1)
R = np.zeros((size, size))
initial_std = 0.5
roughness = 0.5

# Set initial corner values and start the algorithm
c1, c2, c3, c4 = random.random(), random.random(), random.random(), random.random()
mid_disp_2d(R, 0, 0, size - 1, size - 1, c1, c2, c3, c4, initial_std, roughness)

# Display the generated terrain
import matplotlib.pyplot as plt

plt.imshow(R, cmap='gray')
plt.colorbar()
plt.title('Fractal Terrain')
plt.show()
