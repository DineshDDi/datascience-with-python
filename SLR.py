import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv("Simple_linear_regression.csv")

x = dataset.iloc[:,0:1].values
y = dataset.iloc[:,1].values

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=.30, random_state=0)

# create model
regress = LinearRegression()
regress.fit(x_train, y_train)

# predict
y_pred = regress.predict(x_test)

# print(y_pred)

# print(y_test)

plt.title("predict")
plt.xlabel("experience")
plt.ylabel("salary")
plt.scatter(x_test, y_test, color="red")
plt.plot(x_test, y_pred, color="blue")
plt.show()


plt.title("comparison predict")
plt.xlabel("experience")
plt.ylabel("salary")
plt.scatter(x_test, y_test, color="red")
plt.plot(x_train, regress.predict(x_train), color="blue")
plt.show()

