import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,5), dpi=80)
ax = plt.subplot(111)
plt.ylim((-3,3))

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))


a = np.linspace(-2.5, 1.62, 50)
plt.plot(a,a,label = r'$U_o$')        #生成一个正弦函数图

a = np.linspace(1.62, 2.5)
b = 0*a + 1.62
plt.plot(a,b, linewidth = 3)

plt.legend(loc='upper right')


plt.plot([0,1.62],[1.62,1.62], color ='red', linewidth=1, linestyle="--")
plt.plot([-2.5,0],[-2.5,-2.5], color ='red', linewidth=1, linestyle="--")

plt.plot([1.62,1.62],[0,1.62], color ='red', linewidth=1, linestyle="--")
plt.plot([-2.5,-2.5],[-2.5,0], color ='red', linewidth=1, linestyle="--")

plt.scatter([0,],[1.62,], 50, color ='red')

plt.annotate(r'1.62V',
         xy=(0,1.62),xytext = (-.3,1.62))
plt.scatter([0,],[-2.5,], 50, color ='red')

plt.annotate(r'-2.50V',
         xy=(0,-2.5), xytext = (0,-2.5))


plt.scatter([1.62,],[0,], 50, color ='red')

plt.annotate(r'1.62V',
         xy=(1.62,0),xytext = (1.62,-0.3))

plt.scatter([-2.5,],[0,], 50, color ='red')

plt.annotate(r'-2.50V',
         xy=(-2.5,0), xytext = (-2.5,0.3))

plt.savefig("U6.png")

