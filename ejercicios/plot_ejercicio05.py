import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("salida_ejercicio05.txt")

plt.figure()
plt.subplot(2,2,1)
plt.plot(data[:,0], data[:,1])

plt.subplot(2,2,2)
plt.plot(data[:,0], data[:,2])

plt.subplot(2,2,3)
plt.plot(data[:,0], data[:,3])

plt.subplot(2,2,4)
plt.plot(data[:,0], data[:,4])

plt.savefig("plot_ejercicio05.png")
