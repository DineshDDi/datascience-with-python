import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt

data = pd.read_csv("homeprices.csv")

x = data.iloc[:, :1].values
y = data.iloc[:, 1:].values

# print(x)
# refer who data in this plot
'''
plt.title("Linear Regression")
plt.xlabel("area")
plt.ylabel("price")
plt.scatter(x, y, color='red', label="price")
plt.legend()
plt.show()
'''

reg = LinearRegression()
reg.fit(x, y)

print(reg.predict([[2800]]))

print(reg.coef_)

print(reg.intercept_)

# area = pd.read_csv("areas.csv")

# p = reg.predict(area)
# print(p)

# area['price'] = p

# print(area)
# area.to_csv("SLR_answer.csv")


'''
plt.title("Linear Regression")
plt.xlabel("area")
plt.ylabel("price")
plt.scatter(x, y, color='red', label="price")
plt.plot(area, reg.predict(area), color='blue')
plt.legend()
plt.show()
'''




