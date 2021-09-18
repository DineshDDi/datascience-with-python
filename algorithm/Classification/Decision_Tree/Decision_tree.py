import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("salaries.csv")

x = data.drop('salary_more_then_100k', axis='columns')
y = data['salary_more_then_100k']

# print(x)
# print(y)

x_company = LabelEncoder()
x_job = LabelEncoder()
x_degree = LabelEncoder()

x['company_n'] = x_company.fit_transform(x['company'])
x['job_n'] = x_job.fit_transform(x['job'])
x['degree_n'] = x_degree.fit_transform(x['degree'])

# print(x)

x1 = x.drop(['company', 'job', 'degree'], axis='columns')

# print(x1)

model = DecisionTreeClassifier()
model1 = RandomForestClassifier()

model.fit(x1, y)
model1.fit(x1, y)


# print(model.score(x1,y))
# print(model1.score(x1,y))


print(model.predict([[2,1,0]]))
print(model1.predict([[2,1,0]]))

