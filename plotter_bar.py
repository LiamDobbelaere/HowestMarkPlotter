import matplotlib.pyplot as plt
import numpy as np
import pandas

test = "ZylannMicroHM"

g = pandas.read_csv('./results/Godot_' + test + '.csv', sep=',', header=None)
gx, gy = g[0].values, g[1].values

u = pandas.read_csv('./results/Unity_' + test + '.csv', sep=',', header=None)
ux, uy = u[0].values, u[1].values

plt.bar(gx, gy, label='Godot', color="#458dc0")
plt.bar(ux, uy, label='Unity', color="#000000")

plt.xticks(gx, rotation='vertical')
plt.ylabel('ms')
plt.title(test)
plt.legend()
plt.show()
