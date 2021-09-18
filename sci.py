from scipy import special
from scipy import integrate
#help(integrate.quad)


'''
#power of a and b (exponential functions)
a = special.exp10(2)
print(a)

b = special.exp2(3)
print(b)

#sin,cos degrees (trigonometric functions)
a = special.sindg(90)
print(a)

b = special.cosdg(90)
print(b)
'''


'''
#single integration
a = integrate.quad(lambda x: special.exp10(x),0,4)

print(a)

'''

'''
#double integration
a = lambda x,y : x*y**2
b = lambda x : 1
c = lambda x : -1
print(integrate.dblquad(a,0,5,b,c))
'''


'''
#fourier tranformation

from scipy.fftpack import fft,ifft
import numpy as np
x = np.array([1,2,3,4])
y = ifft(x)
print(y)
'''


'''
#linear algebra

from scipy import linalg
import numpy as np

a = np.array([[1,2],[3,4]])
b = linalg.inv(a)
print(b)
'''


'''
#interpolatation
from scipy import interpolate
from matplotlib import pyplot as plt
import numpy as np

x = np.arange(5,20)
y = np.exp(x/3.0)
f = interpolate.interp1d(x,y)
x1 = np.arange(6,12)
y1 = f(x1)
plt.plot(x,y,'p',x1,y1,"--")
plt.show()
'''



