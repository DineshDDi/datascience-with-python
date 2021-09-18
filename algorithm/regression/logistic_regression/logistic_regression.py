import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import math

data = pd.read_csv("insurance_data.csv")

plt.scatter(data.age, data.bought_insurance, marker='*', color='red')
plt.show()

x_train, x_test, y_train, y_test = train_test_split(data[['age']],data.bought_insurance, test_size=0.2, random_state=0)

model = LogisticRegression()
model.fit(x_train, y_train)

y_predict = model.predict(x_test)

# print(model.predict_proba(x_test))

# print(y_predict)


plt.scatter(data.age, data.bought_insurance, marker='*', color='red')
plt.plot(x_test, model.predict(x_test), color="blue")
plt.show()


# print(model.predict([[43]]))
print(model.score(x_test, y_test))




