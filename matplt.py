"""
from matplotlib import pyplot as plt

plt.plot([1,2,3],[4,6,1])

plt.show()
"""


"""
from matplotlib import pyplot as plt

x = [1,2,3]
y = [4,5,1]

plt.plot(x,y)
plt.title("title of the graph")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()
"""


"""
from matplotlib import pyplot as plt
from matplotlib import style

style.use("ggplot")

x = [1,2,3]
y = [4,5,1]

x1 = [2,3,4]
y1 = [3,6,2]

plt.plot(x,y,'g',label='line one',linewidth=5)
plt.plot(x1,y1,'c',label='line two',linewidth=5)

plt.title("title of the graph")
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.legend()
plt.grid(True,color='k')
plt.show()
"""


"""
#bar plot
import matplotlib.pyplot as plt

plt.bar([.25, 1.25, 2.25, 3.25, 4.25], [11, 20, 14, 19, 15], label="CSK", color='yellow', width=.5)
plt.bar([.75, 1.75, 2.75, 3.75, 4.75], [15, 10, 11, 12, 15], label="MI", width=.5)
plt.xlabel('Overs')
plt.ylabel('Runs')
plt.title('Statistic Board')
x = [.25, .75, 2.25, 3.75, 4.25, 4.75]
y = [13, 17, 16, 14, 17, 17]
plt.scatter(x,y, label="Wickets", color='black', marker=".", s=1300)
plt.legend()
plt.show()
"""


"""
#histograms
from matplotlib import pyplot as plt

population_ages = [25,34,62,73,22,87,92,43,51,15,12,33,48,82,30,46,35]

btn = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(population_ages,btn,histtype='bar',rwidth=0.8,label='population')

plt.title("age views population")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()
"""


"""
# Scatter Plot
from matplotlib import pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y,label='Skitcat',color='b',s=25,marker='o')

plt.xlabel('x')
plt.ylabel('y')
plt.title("Scatter Plot")
plt.legend()
plt.show()
"""


'''
# Stackplot or area plot
from matplotlib import pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating = [2,3,2,3,2]
working = [7,8,7,2,2]
playing =  [8,5,7,8,13]

plt.plot([],[],color='m',label='Sleeping',linewidth=5)
plt.plot([],[],color='c',label='Eating',linewidth=5)
plt.plot([],[],color='r',label='Working',linewidth=5)
plt.plot([],[],color='k',label='Playing',linewidth=5)

plt.stackplot(days,sleeping,eating,working,playing)
colors=['m','c','r','k']

plt.xlabel('days')
plt.ylabel('y')
plt.title('Stackplot')
plt.legend()
plt.show()
'''


'''
# pie chart
import matplotlib.pyplot as plt

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols=['c','m','r','b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%')

plt.title('Pie plot')
plt.show()
'''


'''
# multiple plots
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.arange(0.0,5.0,0.1)
t2 = np.arange(0.0,5.0,0.02)

plt.subplot(211)
plt.plot(t1,f(t1),'bo',t2,f(t2))

plt.subplot(212)
plt.plot(t2,np.cos(2*np.pi*t2))
plt.show()
'''


'''
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

img = mpimg.imread('pythondevelop1.png')
print(img)

imgplot = plt.imshow(img)

lum_img = img[:, :, 0]

plt.imshow(lum_img)

plt.imshow(lum_img, cmap="hot")

imgplot = plt.imshow(lum_img)
imgplot.set_cmap('nipy_spectral')

imgplot = plt.imshow(lum_img)
plt.colorbar()

plt.hist(lum_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')

imgplot = plt.imshow(lum_img, clim=(0.0, 0.7))

fig = plt.figure()
ax = fig.add_subplot(1, 2, 1)
imgplot = plt.imshow(lum_img)
ax.set_title('Before')
plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')
ax = fig.add_subplot(1, 2, 2)
imgplot = plt.imshow(lum_img)
imgplot.set_clim(0.0, 0.7)
ax.set_title('After')
plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')

img = Image.open('pythondevelop1.png')
img.thumbnail((64, 64), Image.ANTIALIAS)  # resizes image in-place
imgplot = plt.imshow(img)

imgplot = plt.imshow(img, interpolation="nearest")


imgplot = plt.imshow(img, interpolation="bicubic")

plt.show()
'''



