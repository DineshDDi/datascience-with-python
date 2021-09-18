import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.metrics import mean_squared_error

dataset = pd.read_csv("bank_train.csv")
dataset_test = pd.read_csv("bank_test.csv")

#print(dataset.shape)
#print(dataset.info)
# print(dataset.dtypes)
#print(dataset.isnull().sum())

dataset.dropna(inplace=True)
dataset_test.dropna(inplace=True)

dataset_test_dr = dataset_test

x = dataset.iloc[:, :16].values
y = dataset.iloc[:, 16].values

x_test = dataset_test.iloc[:, :16].values
y_test = dataset_test.iloc[:, 16].values

#print(x.shape)

"""
# Correlation
age_cor = x['age']
correction = age_cor.corr(x['balance'])
print(correction)
"""


label_x = LabelEncoder()
x[:, 1] = label_x.fit_transform(x[:, 1])
x[:, 2] = label_x.fit_transform(x[:, 2])
x[:, 3] = label_x.fit_transform(x[:, 3])
x[:, 4] = label_x.fit_transform(x[:, 4])
x[:, 6] = label_x.fit_transform(x[:, 6])
x[:, 7] = label_x.fit_transform(x[:, 7])
x[:, 8] = label_x.fit_transform(x[:, 8])
x[:, 10] = label_x.fit_transform(x[:, 10])
x[:, 15] = label_x.fit_transform(x[:, 15])
#print(x)


label_y = LabelEncoder()

y = label_y.fit_transform(y)
#print(y)

#print(dataset.shape)

#print(dataset.iloc[:, 0].value_counts())

# print(243/597*100)


#sns.countplot(dataset['marital'], hue=dataset['deposit'])
sns.scatterplot(dataset['age'], dataset['balance'])

plt.show()

label_xtest = LabelEncoder()
x_test[:, 1] = label_xtest.fit_transform(x_test[:, 1])
x_test[:, 2] = label_xtest.fit_transform(x_test[:, 2])
x_test[:, 3] = label_xtest.fit_transform(x_test[:, 3])
x_test[:, 4] = label_xtest.fit_transform(x_test[:, 4])
x_test[:, 6] = label_xtest.fit_transform(x_test[:, 6])
x_test[:, 7] = label_xtest.fit_transform(x_test[:, 7])
x_test[:, 8] = label_xtest.fit_transform(x_test[:, 8])
x_test[:, 10] = label_xtest.fit_transform(x_test[:, 10])
x_test[:, 15] = label_xtest.fit_transform(x_test[:, 15])
#print(x_test)

label_ytest = LabelEncoder()
y_test = label_ytest.fit_transform(y_test)

#print(y_test)

"""
print(x.shape)
print(y.shape)
print(x_test.shape)
print(y_test.shape)
"""


#model = KNeighborsClassifier(n_neighbors=7)
model = LogisticRegression(random_state=0)

model.fit(x, y)

print(model.score(x_test, y_test))

prediction = model.predict(x_test)

dataset_test_dr['prediction'] = prediction

dataset_test_dr.to_csv("evng_logic_predictions.csv")

cm1 = confusion_matrix(y_test, prediction)

total1=sum(sum(cm1))
accuracy1=(cm1[0,0]+cm1[1,1])/total1
print ('Accuracy : ', accuracy1)

sensitivity1 = cm1[0,0]/(cm1[0,0]+cm1[0,1])
print('Sensitivity : ', sensitivity1*100)

specificity1 = cm1[1,1]/(cm1[1,0]+cm1[1,1])
print('Specificity : ', specificity1*100)

print(f1_score(y_test, prediction, average=None))

print(mean_squared_error(y_test, prediction))


