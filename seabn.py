# 1.visualizing statistical relationships
# 2.plotting with categorical data
# 3.visualizing the distribution of a dataset


# sample function
import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


"""
# simple relplot
a = sns.load_dataset("flights")
b = sns.relplot(x='passengers', y='month', data=a)
plt.show()
"""


'''
# year view relplot
a = sns.load_dataset("flights")
b = sns.relplot(x='passengers', y='month', hue='year', data=a)
plt.show()
'''


'''
b = sns.load_dataset("tips")
#print(b)
# line graph
#sns.relplot(x='time',y='tip', data=b, kind="line")

# categorical data
#sns.catplot(x='day',y='total_bill',data=b)

#plt.show()

# kind views categorical data
sns.catplot(x='day',y='total_bill',kind='violin',data=b) # kind='boxen' is another kind

plt.show()
'''


'''
s = np.random.normal(loc=10, size=100, scale=2)
sns.distplot(s)
plt.show()
'''


