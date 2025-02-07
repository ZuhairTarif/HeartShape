import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(theta)**3
y = 13 * np.cos(theta) - 5 * np.cos(2 * theta) - 2 * np.cos(3 * theta) - np.cos(4 * theta)

plt.figure(figsize=(6, 6))
plt.plot(x, y, color="red")
plt.axis('off')  # Hide axes
plt.gca().set_aspect('equal', adjustable='box')

plt.savefig("images/love_drawing.png", dpi=300, bbox_inches='tight', pad_inches=0)

plt.show()
