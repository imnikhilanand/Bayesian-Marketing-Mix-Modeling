# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 09:47:15 2022

@author: Nikhil
"""

# importing the libraries
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# importing the dataset
data = pd.read_csv("advertising_data.csv")
data['sales'] = data['sales']*100

# Lets plot the spend over time 
sns.lineplot(x='Week', y='TV', data=data, color='blue')
sns.lineplot(x='Week', y='sales', data=data, color='red')
sns.lineplot(x='Week', y='radio', data=data, color='green')
sns.lineplot(x='Week', y='newspaper', data=data, color='cyan')

# lets plot the sales vs tv commercial
sns.scatterplot(x='TV', y='sales', data=data, color='blue')

# lets plot the sales vs tv commercial
sns.scatterplot(x='radio', y='sales', data=data, color='blue')

# lets plot the sales vs tv commercial
sns.scatterplot(x='newspaper', y='sales', data=data, color='blue')


# modeling OLS
x = data[['TV', 'sales', 'radio', 'newspaper']]
x = sm.add_constant(x)
y = data['sales']

# modeling the data
result = sm.OLS(y, x).fit()

# printing the summary of the model
print(result.summary())

''' 
From the above model we can observe that increase in newspaper spending will lower the sales.
Similarly, for the radio we can see that the coefficient is 0, which means that the spending in newspaper advertisment will not result in any increase in sale.
Since, these coefficients does not go along with our assumptions, we have to use Bayesian Model to find the coefficient. 
'''

