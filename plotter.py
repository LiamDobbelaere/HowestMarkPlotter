import matplotlib.pyplot as plt
import numpy as np

test = "PolyMark3D"

gx, gy = np.loadtxt('results/Godot_' + test + '.csv', delimiter=',', unpack=True)
ux, uy = np.loadtxt('results/Unity_' + test + '.csv', delimiter=',', unpack=True)

plt.plot(gx, gy, linewidth=1, alpha=0.8, label='Godot', color="#458dc0")
plt.plot(ux, uy, linewidth=1, alpha=0.8, label='Unity', color="#000000")

plt.xlabel('Count')
plt.ylabel('FPS')
plt.title(test)
plt.legend()
plt.show()
