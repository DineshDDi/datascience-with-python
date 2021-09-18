"""
# multidimential array
import numpy as np

a = np.array([(1, 2, 3, 4), (5, 6, 7, 8)])

print(a)
"""


"""
# fast and lessmemory compare with list
import numpy as np
import time
import sys

a = range(1000)
print(sys.getsizeof(1)*len(a))

d = np.arange(1000)
print(d.size*d.itemsize)

size = 1000000

l1 = range(size)
l2 = range(size)

a1 = np.arange(size)
a2 = np.arange(size)

start = time.time()

result = [(x,y) for x,y in zip(l1,l2)]

print((time.time()-start)*1000)

start = time.time()

result = a1+a2

print((time.time()-start)*1000)
"""


'''
# find the dimential,datatpye,shape,size,itemsize
import numpy as np

a = np.array([(1,2,3),(4,5,6),(7,8,9),(10,11,12)])

print(a.ndim)
print(a.dtype)
print(a.itemsize)
print(a.size)
print(a.shape)
print(a)
a = a.reshape(3,4)
print(a)

# slicing
print(a[0,2])

# 0 is first element I mean first tuple or first row
# 2 is inside the first element index value I mean (1,2,3) is first element, 1 is 0 index in first element

print(a[0:,2]

# all elements 2nd index was print
print(a[0:2,3])
# 0 to 2nd elements 3rd index was print
'''


'''
# range in numpy array
import numpy as np

a = np.linspace(1,3,5)

print(a)
'''


'''
# max,min and sum in numpy
import numpy as np

a = np.array([(1,2,3),(4,5,6)])

print(a.sum(axis=1))
print(a.max())
print(a.min())
'''


'''
# 3D dimensional array
import numpy as np
a = np.array([[[1,2,3,4],[1,2,3,4]],[[6,7,8,9],[5,6,7,8]]])
print(a.ndim)
'''


'''
#sqrt,standard deviation

import numpy as np

a = np.array([1,2,3,4,5])
print(np.sqrt(a))
print(np.std(a))
'''


'''
# addition,multiple,subtraction,divition

import numpy as np

a = np.array([(1,2,3),(4,5,6)])
b = np.array([(1,2,3),(4,5,6)])
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# vertical,herizondal in array 
print(np.hstack(a))
print(np.vstack(b))
'''


"""
# numpy special functions
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0,3*np.pi,0.1)

# y = np.sin(x)
y = np.cos(x)
# y = np.tan(x)

plt.plot(x,y)

plt.show()
"""


'''
# log,exponantial
import numpy as np

a = np.array([1,2,3])
print(np.log(a))
print(np.exp(a))
'''

