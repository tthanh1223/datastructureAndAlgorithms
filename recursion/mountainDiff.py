import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random


def random_disp(scale):
    """Generates a random displacement based on the scale."""
    return random.uniform(-scale, scale)


def midpoint_displacement_3d(size, roughness, scale):
    """
    Generates a 3D height map for mountains using midpoint displacement.

    Parameters:
        size (int): The size of the grid (size x size).
        roughness (float): Roughness factor for the mountain (higher = rougher).
        scale (float): Initial scale of the random displacement.

    Returns:
        np.ndarray: A 2D array representing the height map of the mountains.
    """
    # Create an empty height map
    height_map = np.zeros((size, size))

    # Set the corners
    height_map[0, 0] = random_disp(scale)
    height_map[0, size - 1] = random_disp(scale)
    height_map[size - 1, 0] = random_disp(scale)
    height_map[size - 1, size - 1] = random_disp(scale)

    step_size = size - 1

    while step_size > 1:
        half_step = step_size // 2

        # Diamond step
        for y in range(0, size - 1, step_size):
            for x in range(0, size - 1, step_size):
                avg = (height_map[y][x] +
                       height_map[y + step_size][x] +
                       height_map[y][x + step_size] +
                       height_map[y + step_size][x + step_size]) / 4.0
                height_map[y + half_step][x + half_step] = avg + random_disp(scale)

        # Square step
        for y in range(0, size, half_step):
            for x in range((y + half_step) % step_size, size, step_size):
                avg = 0
                count = 0
                if x - half_step >= 0:
                    avg += height_map[y][x - half_step]
                    count += 1
                if x + half_step < size:
                    avg += height_map[y][x + half_step]
                    count += 1
                if y - half_step >= 0:
                    avg += height_map[y - half_step][x]
                    count += 1
                if y + half_step < size:
                    avg += height_map[y + half_step][x]
                    count += 1
                height_map[y][x] = (avg / count) + random_disp(scale)

        # Reduce the scale for next iteration
        scale *= roughness
        step_size //= 2

    return height_map


# Parameters
size = 513  # Size of the height map (must be 2^n + 1)
roughness = 0.5  # Roughness factor (lower values = smoother)
scale = 100  # Initial displacement scale

# Generate the height map
height_map = midpoint_displacement_3d(size, roughness, scale)

# Create a meshgrid for plotting
x = np.linspace(0, size - 1, size)
y = np.linspace(0, size - 1, size)
x, y = np.meshgrid(x, y)

# Plotting the 3D mountain
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, height_map, cmap='terrain', edgecolor='none')
ax.set_title('3D Mountain Landscape Using Midpoint Displacement')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Height')
plt.show()
