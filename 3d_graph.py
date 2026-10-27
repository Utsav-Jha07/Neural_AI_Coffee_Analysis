import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# ax=plt.axes(projection='3d')


# #ploting points
# # x_data=np.random.randint(0,100 , (500,))
# # y_data=np.random.randint(0,100 , (500,))
# # z_data=np.random.randint(0,100 , (500,))
# # ax.scatter(x_data , y_data , z_data , alpha=0.6)
# # plt.show()


# x_data=np.arange(0,50,0.1)
# y_data=np.arange(0,50,0.1)
# z_data=x_data*y_data
# ax.plot3D(x_data , y_data , z_data)
# ax.set_title("funny Function")
# ax.set_xlabel("My X Values (cm)")
# ax.set_ylabel("My Y Values (cm)")
# ax.set_zlabel("My X Values (cm)")
# plt.show()

#surface area 
ax=plt.axes(projection='3d')
x_data=np.arange(-5,5,0.1)
y_data=np.arange(-5,5,0.1)

X,Y=np.meshgrid(x_data , y_data)
Z=np.sin(X) * np.cos(Y)

ax.plot_surface(X , Y , Z , cmap='plasma')
ax.view_init(azim=0 ,elev=90 )
plt.show()
