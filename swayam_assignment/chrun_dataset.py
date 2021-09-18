import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

churn = pd.read_csv("churn.csv")

print(churn['SeniorCitizen'].describe())
churn['SeniorCitizen'].fillna(churn['SeniorCitizen'].mean(), inplace = True)

print(churn['SeniorCitizen'].isna().sum())

"""
sns.countplot(x=churn['InternetService'])

plt.show()
"""
# sns.boxplot(x=churn['InternetService'],y=churn['MonthlyCharges'])

# plt.show()

"""
churn['Dependents'] = churn['Dependents'].replace("1@#", np.nan)

# print(churn.shape)
"""

"""
s =  churn['customerID'].str.len()

print(s.value_counts())
"""
"""
# find fiber optic customers count
cust_det_extr = churn[churn.InternetService == 'Fiber optic']

print(len(cust_det_extr))

cust_det_extr = churn.loc[churn.InternetService == 'Fiber optic']

print(len(cust_det_extr))

cust_det_extr = churn.loc[churn.InternetService.isin(['Fiber optic'])]

print(len(cust_det_extr))
"""
