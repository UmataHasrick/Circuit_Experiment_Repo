import matplotlib.pyplot as plt
import numpy as np

h = np.pi/50

upperbound = 1.62
lowerbound = -2.50


plt.figure(figsize=(8,5), dpi=80)
ax = plt.subplot(111)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))


a = np.linspace(0, 3 * np.pi, 150)
a1 = np.linspace(0, 11*h,11)
a2 = np.linspace(11*h, 39*h, 28)
a3 = np.linspace(39*h, 111*h, 72)
a4 = np.linspace(111*h, 139*h, 28)
a5 = np.linspace(139*h, 150*h, 11)

b1 = 2.5*np.sin(a1)
b2 = 0*np.sin(a2) + 1.62
b3 = 2.5*np.sin(a3)
b4 = 0*np.sin(a2) + 1.62
b5 = 2.5*np.sin(a5)

c = np.hstack((b1,b2,b3,b4,b5))

plt.plot(a, c, label = r'$U_o$')

plt.legend(loc='upper right')


plt.plot([0,3*np.pi],[upperbound, upperbound], color ='red', linewidth=1, linestyle="--")
plt.plot([0,3*np.pi],[lowerbound, lowerbound], color ='red', linewidth=1, linestyle="--")

plt.scatter([0,],[upperbound,], 50, color ='red')

plt.annotate(str(upperbound)+'V',
         xy=(0,upperbound),xytext = (-1,upperbound))
plt.scatter([0,],[lowerbound,], 50, color ='red')

plt.annotate(str(lowerbound)+'V',
         xy=(0,lowerbound), xytext = (-1,lowerbound))

plt.savefig("U5.png")


