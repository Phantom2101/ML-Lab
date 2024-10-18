import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv('C:\\Users\\HP\\Desktop\\python pgms\\Python codes\\Lab work\\ML LAB\\Salary_Data.csv')
X =data.iloc[:, :-1].values
Y =data.iloc[: , -1].values


from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, Y_train)

y_pred = model.predict(X_train)

plt.scatter(X_train, Y_train, color = 'red')
plt.plot(X_train, model.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

plt.scatter(X_test, Y_test, color = 'red')
plt.plot(X_test, model.predict(X_test), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()