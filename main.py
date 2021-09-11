import numpy as np
import matplotlib.pyplot as plt
import math
from itertools import permutations

no_of_points = 8

x_value = np.random.randint(1, 100, no_of_points)
y_value = np.random.randint(1, 100, no_of_points)

x_per = list(permutations(x_value))
y_per = list(permutations(y_value))
distance_sum= []

for x in range(math.factorial(no_of_points)):
    dist = []
    for y in range(no_of_points-1):
        d1 = np.sqrt((y_per[x][y]-y_per[x][y+1])**2 + (x_per[x][y]-x_per[x][y+1])**2)
        dist.append(d1)
    distance_sum.append(sum(dist))

print('The maximum distance = ', max(distance_sum))
print('The minimum distance = ', min(distance_sum))

max_pos = distance_sum.index(max(distance_sum))
min_pos = distance_sum.index(min(distance_sum))

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(x_per[max_pos], y_per[max_pos], color='red', linestyle='dashed', linewidth = 2,
         marker='o', markerfacecolor='blue', markersize=10)
ax2.plot(x_per[min_pos], y_per[min_pos], color='green', linestyle='dashed', linewidth = 2,
         marker='o', markerfacecolor='blue', markersize=10)
plt.show



