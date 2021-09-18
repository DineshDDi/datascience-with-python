import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


data = pd.read_csv("canada_per_capita_income.csv")

x = data.iloc[:,:1].values
y = data.iloc[:,1:].values

# print(x)
# print(y)

'''
plt.title("Linear Regressiion")
plt.xlabel("year")
plt.ylabel("income")
plt.scatter(x, y, color='red', label="income")
plt.legend()
plt.show()
'''

reg = LinearRegression()
reg.fit(x, y)

print(reg.predict([[2020]]))

print(reg.coef_)
print(reg.intercept_)



