import numpy as np
import pandas as pd
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


data_df = load_digits()

# print(data_df)

# print(data_df.feature_names)
# print(data_df.target_names)
# print(dir(data_df))
# print(data_df.target)

dataset = pd.DataFrame(data_df.data, data_df.target)
# print(dataset.head())

dataset['targets'] = data_df.target
# print(dataset.head(20))

x_train, x_test, y_train, y_test = train_test_split(dataset.drop("targets", axis='columns'), dataset['targets'],
                                                    test_size=0.30, random_state=0)

model = SVC(kernel='linear')
model.fit(x_train, y_train)
print(model.score(x_test, y_test))


model = SVC(kernel='rbf')
model.fit(x_train, y_train)
print(model.score(x_test, y_test))




