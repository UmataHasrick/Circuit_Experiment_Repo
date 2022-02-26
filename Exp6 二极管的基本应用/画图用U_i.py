import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,5), dpi=80)
ax = plt.subplot(111)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))


a = np.linspace(0, 3 * np.pi, 50)
b = 2.5 * np.sin(a)
plt.plot(a,b,label = r'$U_i$')        #生成一个正弦函数图

plt.legend(loc='upper right')


plt.plot([0,3*np.pi],[2.5,2.5], color ='red', linewidth=1, linestyle="--")
plt.plot([0,3*np.pi],[-2.5,-2.5], color ='red', linewidth=1, linestyle="--")

plt.scatter([0,],[2.5,], 50, color ='red')

plt.annotate(r'2.50V',
         xy=(0,2.5),xytext = (-1,2.5))
plt.scatter([0,],[-2.5,], 50, color ='red')

plt.annotate(r'-2.50V',
         xy=(0,-2.5), xytext = (-1,-2.5))

plt.savefig("Ui.png")


