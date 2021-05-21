# loading some libs
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# array: you cannot change the element in an array
# list: []
# dictonary: {}

# how much time does student spend on reading one book
# minutes
cost_time = (26,33,65,28,34,55,25,44,50,36,26,37,43,62,35,38,45,32,28,34)


def draw_pic(x1, y1, x2, y2):
    # draw your audio waves
    # setting size for your picture
    fig = plt.figure(figsize=(10, 10))

    # total 2*1 = 2 sub picture
    # pic1 is the first one
    # pic2 is the second one
    pic1 = fig.add_subplot(2, 1, 1)
    pic2 = fig.add_subplot(2, 1, 2)

    # pic1
    pic1.scatter(x1, y1, color='red')
    pic1.set_xlabel('xpic1')
    pic1.set_ylabel('ypic1')

    # pic2
    pic2.scatter(x2, y2, color='g', linestyle='--')
    plt.show()
    plt.close()

def gaussian(sigma, x, u):
	y = np.exp(-(x - u) ** 2 / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
	return y

# caculate Mean
arg = 0.0
for i in range(len(cost_time)):
    arg += cost_time[i]
arg = arg/len(cost_time)

# caculate standard Deviation
sigma = 0.0
for i in range(len(cost_time)):
    sigma += np.sqrt((cost_time[i] - arg) ** 2)
sigma = sigma / len(cost_time)


x = []
y = []
for i in range(len(cost_time)):
    x.append(cost_time[i])
    y.append(gaussian(sigma,cost_time[i],arg))



##############do the standard gaussian


std_x = []
std_y = []
for i in range(len(cost_time)):
    std_x.append( (cost_time[i] - arg)/sigma)

std_y = stats.norm.pdf(std_x)


draw_pic(x,y,std_x,std_y)




