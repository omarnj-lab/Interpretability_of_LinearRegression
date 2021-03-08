# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 01:34:03 2021

@author: omar
"""
# Imports 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# get the data 
dataset = pd.read_csv('student_scores.csv')


#dataset.shape
#dataset.head()
#dataset.describe()

#dataset.plot(x='Hours', y='Scores', style='o')
#plt.title('Hours vs Percentage')
#plt.xlabel('Hours Studied')
#plt.ylabel('Percentage Score')
#plt.show()

# Prepare thr Data : 
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values


# Split DataSet: 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)



from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)


print(regressor.intercept_)
print(regressor.coef_)


y_pred = regressor.predict(X_test)

df = pd.DataFrame(y_pred)
df


from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))














