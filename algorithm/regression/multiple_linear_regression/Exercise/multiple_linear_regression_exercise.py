import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
# from word2number import w2n

data = pd.read_csv("hiring.csv")

data.experience = data.experience.fillna("zero")


#data.experience = data.experience.apply(w2n.word_to_num)

data["test_score(out of 10)"].fillna(data["test_score(out of 10)"].mean(), inplace=True)

print(data)

reg = LinearRegression()
reg.fit(data[['experience', 'test_score(out of 10)', 'interview_score(out of 10)']], data['salary($)'])

print(reg.predict([[2, 9, 6]]))
print(reg.predict([[12,10,10]]))


