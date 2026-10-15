import numpy as np
import matplotlib.pyplot as plt

def distance_formula(x1, x2, y1, y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

x1, x2 = 2, 6
y1, y2 = 1, 8

distance = distance_formula(x1, x2, y1, y2)
print(f"Distance between points ({x1}, {y1}) and ({x2}, {y2}) is {distance}")

plt.plot([x1, x2], [y1, y2], 'o-')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Distance between two points')
plt.grid(True)
plt.show()
