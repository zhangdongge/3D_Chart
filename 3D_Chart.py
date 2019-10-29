
1 、函数=21.5 + X * np.sin(4 * np.pi * X) + Y * np.sin(20 * np.pi * Y)
from matplotlib import pyplot as plt
import numpy as np
# mpl_toolkits.mplot3d是Matplotlib里面专门用来画三维图的工具包；
# 使用from mpl_toolkits.mplot3d import *或者import mpl_toolkits.mplot3d as p3d
from mpl_toolkits.mplot3d import Axes3D

# 创建Axes3D对象:ax
fig = plt.figure()
ax = Axes3D(fig)

# 调用函数在ax上画图
X,Y = np.mgrid[-3:12.1:20j,4.1:5.8:20j]  # 返回多维结构，常见的如2D图形，3D图形。
Z = 21.5 + X * np.sin(4 * np.pi * X) + Y * np.sin(20 * np.pi * Y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
# rstride:行之间的跨度  cstride:列之间的跨度
# rcount:设置间隔个数，默认50个，ccount:列的间隔个数  不能与上面两个参数同时出现
# cmap是颜色映射表
plt.show()

# 2
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as p3d

fig = plt.figure()
ax = p3d.Axes3D(fig)

z = np.linspace(0, 15, 1000)
x = np.sin(z)
y = np.cos(z)
ax.plot(x, y, z, 'green')
plt.show()


# 3 3D 散点图
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3

k, b = np.mgrid[1:3:3j, 4:6:3j]
f_kb = 3 * k ** 2 + 2 * b + 1

k.shape = -1, 1
b.shape = -1, 1
f_kb.shape = -1, 1  # 统统转成9行1列

fig = p.figure()
ax = p3.Axes3D(fig)
ax.scatter(k, b, f_kb, c='r')
ax.set_xlabel('k')
ax.set_ylabel('b')
ax.set_zlabel('ErrorArray')
p.show()

# 4、3D曲面图
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3

# 注意：mgrid中第三个参数越大，说明某一区间被分割得越细，相应的曲面越精准。
k, b = np.mgrid[1:3:100j, 4:6:100j]
f_kb = 3 * k ** 2 + 2 * b + 1

ax = plt.subplot(111, projection='3d') # 创建一个三维的绘图工程
ax.plot_surface(k, b, f_kb, rstride=1, cstride=1)
ax.set_xlabel('k')
ax.set_ylabel('b')
ax.set_zlabel('ErrorArray')
p.show()
