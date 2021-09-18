import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

data = pd.read_csv("homeprices.csv")

# print(data)

x = data.iloc[:,0:3]
y = data.iloc[:,3:]
# print(x)
# print(y)

data.bedrooms = data.bedrooms.fillna(data.bedrooms.median())
# print(data)

reg = LinearRegression()
reg.fit(data.drop('price',axis='columns'),data.price)

print(reg.predict([[3000, 3, 40]]))

