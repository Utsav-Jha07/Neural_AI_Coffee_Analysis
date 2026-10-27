import random
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-1,1,100)
y=np.sin(x)
z=np.cos(x)
plt.plot(x,y, color='purple')
plt.plot(x,z, color='green')
plt.show()