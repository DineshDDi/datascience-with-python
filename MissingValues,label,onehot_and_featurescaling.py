import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing._encoders import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


data = pd.read_csv("Data_preprocessing for ML.csv")

# find null value location
# print(data.isnull())
# print(data.isnull().sum())

# set depended(y) variable and independed(x) variable
x = data.iloc[:, 0:3].values
y = data.iloc[:, 3:4].values

# missing value filling
im = SimpleImputer(missing_values=np.nan, strategy="mean")

# fit the value to the table
im = im.fit(x[:,1:3])
x[:,1:3] = im.transform(x[:,1:3])
# print(x)


# change string datas to int values (x)
label_x = LabelEncoder()
x[:,0] = label_x.fit_transform(x[:,0])
# print(x)


columntrans = ColumnTransformer([('encoder',OneHotEncoder(),[0])],remainder="passthrough")
x = np.array(columntrans.fit_transform(x),dtype=np.str)
# print(x)


# remove dome variable trap
x = x[:,1:]
# print(x)


# change string datas to int values (y)
label_y = LabelEncoder()
y = label_y.fit_transform(y)

# 1D to 2D
# y = y[np.newaxis, :]

# print(y)


# sprit 4 types of datas as train & test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= .20, random_state=0)
# print(x_train)
# print(x_test)
# print(y_train)
# print(y_test)


# feature Scaling

sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.fit_transform(x_test)

# print(x_train)
# print(x_test)


# plt.plot(x_train,y_train, label="Mytrainset")
# plt.plot(x_test,y_test, label="mytestset")
# plt.show()

