import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("SLR_practice_height_weight.csv")

# print(data.isnull().sum())

x = data.iloc[:,0:1].values
y = data.iloc[:,1:2].values

# print(x)
# print(y)

im = SimpleImputer(missing_values=np.nan, strategy="mean")

im = im.fit(x[:,0:1])

x[:,0:1] = im.transform(x[:,0:1])

# print(data.isnull().sum())

x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.30, random_state=0)

linear = LinearRegression()
linear.fit(x_train, y_train)

y_predict = linear.predict(x_test)

plt.title("predict")
plt.xlabel("height")
plt.ylabel("weight")
plt.scatter(x_train, y_train, color="red")
plt.plot(x_test, y_predict, color="blue")
plt.show()


plt.title("comparison predict")
plt.xlabel("height")
plt.ylabel("weight")
plt.scatter(x_test, y_test, color="red")
plt.plot(x_train, linear.predict(x_train), color="blue")
plt.show()



