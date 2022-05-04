import random
from matplotlib import pyplot as plt
import numpy as np

x = [1,2,3,4,5]

# plt.plot(x)
# plt.show()
# plt.plot(x, np.cos(x))
# plt.show()
# plt.plot(x, np.sin(x))
# plt.show()
# plt.plot(x, np.tan(x))
# plt.show()


# left = [1, 2, 3, 4, 5]
# height = [10, 24, 36, 40, 5]
# tick_label = ['one', 'two', 'three', 'four', 'five']
# plt.bar(left, height, tick_label = tick_label,
#         width = 0.8, color = ['red', 'green'])
# plt.show()


# ages = [2,5,70,40,30,45,50,45,43,40,44,
#         60,7,13,57,18,90,77,32,21,20,40]
# range = (0, 100)
# bins = 10 
# plt.hist(ages, bins, range, color = 'green',
#         histtype = 'bar', rwidth = 0.8)
# plt.show()

# x = []
# y = []
# for i in range(1, 1024):
#     x.append(random.randint(0, 20))
#     y.append(random.randint(0, 20))

# plt.scatter(x, y, label= "stars", color= "green",
#             marker= "*", s=30)
# plt.show()


# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(500)
#     left(210)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

# u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
# x = np.cos(u)*np.sin(v)
# y = np.sin(u)*np.sin(v)
# z = np.cos(v)
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_wireframe(x, y, z)

# plt.show()

# activities = ['eat', 'sleep', 'work', 'play']
# slices = [3, 7, 8, 6]
# colors = ['r', 'y', 'g', 'b']
# plt.pie(slices, labels = activities, colors=colors,
#         startangle=90, shadow = True, explode = (0, 0, 0.1, 0),
#         radius = 1.2, autopct = '%1.1f%%')
# plt.legend()
# plt.show()