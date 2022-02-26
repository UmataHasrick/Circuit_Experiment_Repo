import matplotlib.pyplot as plt
import numpy as np

h = np.pi/50

upperbound = 1.275
lowerbound = 1.225


plt.figure(figsize=(8,5), dpi=80)
plt.ylim(-2,2)
ax = plt.subplot(111)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))


a = np.linspace(0, 3 * np.pi, 150)
a1 = np.linspace(0, 20*h,20)
a2 = np.linspace(20*h, 25*h, 5)
a3 = np.linspace(25*h, 120*h, 95)
a4 = np.linspace(120*h, 125*h, 5)
a5 = np.linspace(25*h, 120*h, 25)

b1 = 1.235526-0.0083765*a1
b2 = 1.275*np.sin(a2)
b3 = 1.275-0.0083765*a3+0.0083765
b4 = 1.275-0.0083765*a5+0.0083765

c = np.hstack((b1,b2,b3,b2,b4))

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

plt.savefig("U3.png")


