import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

dataset = load_iris()

# print(dataset)

# print(dataset.feature_names)
# print(dataset.target_names)

dataset_df = pd.DataFrame(dataset.data, columns=dataset.feature_names)

# print(dataset_df.head())
dataset_df['target'] = dataset.target

# print(dataset_df.head())

df0 = dataset_df[:50]
df1 = dataset_df[50:100]
df2 = dataset_df[100:]

'''
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.scatter(df0['petal length (cm)'], df0['petal width (cm)'], color='green', marker='+', label="setosa")
plt.scatter(df1['petal length (cm)'], df1['petal width (cm)'], color='blue', marker='.', label="versicolor")
plt.scatter(df2['petal length (cm)'], df2['petal width (cm)'], color='pink', marker='o', label="virginica")
plt.legend()
plt.show()


plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.scatter(df0['sepal length (cm)'], df0['sepal width (cm)'], color='green', marker='+', label="setosa")
plt.scatter(df1['sepal length (cm)'], df1['sepal width (cm)'], color='blue', marker='.', label="versicolor")
plt.scatter(df2['sepal length (cm)'], df2['sepal width (cm)'], color='pink', marker='o', label="virginica")
plt.legend()
plt.show()
'''

x = dataset_df.drop(["target"], axis='columns')
y = dataset_df.target

# print(x)
# print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)

# simple model
# model = KNeighborsClassifier()
model = SVC()

model.fit(x_train, y_train)

print(model.score(x_test, y_test))

print(model.predict([[4.8,3.0,1.5,0.3]]))


'''
# reguralization model

model = SVC(C=10)

model.fit(x_train, y_train)

print(model.score(x_test,y_test))
'''


'''
# Gamma model

model = SVC(gamma=10)

model.fit(x_train, y_train)

print(model.score(x_test,y_test))
'''

'''
# kernal model
# kernal keywords = rbf, linear, poly, sigmoid

model = SVC(kernel='rbf')

model.fit(x_train, y_train)

print(model.score(x_test,y_test))
'''




