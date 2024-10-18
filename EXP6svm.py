# Support Vector Machine for Regression

# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR

# Creating synthetic dataset
np.random.seed(0)
X = np.sort(5 * np.random.rand(80, 1), axis=0)
y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])  # Add noise

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Fitting the Support Vector Regression model
svr = SVR(kernel='rbf')  # Using Radial Basis Function kernel
svr.fit(X_train, y_train)

# Predicting on the test set
y_pred = svr.predict(X_test)

# Visualizing the results
plt.scatter(X_train, y_train, color='blue', label='Training Data')
plt.scatter(X_test, y_test, color='green', label='Test Data', marker='x')
plt.scatter(X_test, y_pred, color='red', label='SVM Predictions')
plt.title('Support Vector Machine Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
