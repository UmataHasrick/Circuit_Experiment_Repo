import matplotlib.pyplot as plt
import numpy as np



upperbound = 2.5
lowerbound = -2.5


plt.figure(figsize=(8,5), dpi=80)
ax = plt.subplot(111)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))


a = np.linspace(0, 3 * np.pi, 150)
a1 = np.linspace(np.pi, 2*np.pi, 50)
a2 = np.linspace(2*np.pi, 3*np.pi, 50)
a3 = np.linspace(0, np.pi, 50)

b1 = 2.5*np.sin(a2)
b2 = -2.5*np.sin(a1)

c1 = np.hstack((b1,b2))
c = np.hstack((c1,b1))

plt.plot(a, c, label = r'$U_o$')

plt.legend(loc='upper right')


plt.plot([0,3*np.pi],[upperbound, upperbound], color ='red', linewidth=1, linestyle="--")


plt.scatter([0,],[upperbound,], 50, color ='red')

plt.annotate(str(upperbound)+'V',
         xy=(0,upperbound),xytext = (-1,upperbound))


plt.savefig("U7.png")


