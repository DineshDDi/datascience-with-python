import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


dataset = pd.read_csv("Exploratory_data_analysis.csv")

# shape of the data
# print(dataset.shape)
# print(dataset.shape[0])
# print(dataset.shape[1])


# how to describe data. describe is find min, max, mean, std, percentile of the dataset
# print(dataset.describe())


# how to display total values change the display setting
# print(pd.options.display.max_rows)
# print(pd.options.display.max_columns)

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# print(dataset.describe())

# see the top and bottum of the dataset
# print(dataset.head(10))
# print(dataset.tail(10))


# find the datatypes of datasets
# print(dataset.info())
# print(dataset.dtypes)


# identify data unique
# print(dataset.nunique())


# how to identify value counts hint: you identify one column use below
# print(dataset.iloc[:,4].value_counts())


# how to identify value counts in plots hint: using seaborn
sns.countplot(x="State", data=dataset)
plt.show()

# how to identify value counts hint: you identify muliple columns use below

'''
for i in range(0, dataset.shape[1]):
    print("________",dataset.columns[i],"__________")
    print(dataset.iloc[:,i].value_counts())
    print("__________________________________")
'''


# find null values
# print(dataset.isnull().sum())

# sns.heatmap(dataset.isnull(),cbar=True)
# plt.show()


# finding mean, mode and fill the null values
# print(dataset.mean())
# print(dataset.mode())

# fill single column null value
# dataset["R&D Spend"].fillna((dataset["R&D Spend"].mean()), inplace=True)
# print(dataset["R&D Spend"])

# fill all column null value
dataset.fillna(dataset.mean(), inplace=True)
# print(dataset.isnull().sum())

print(dataset)



