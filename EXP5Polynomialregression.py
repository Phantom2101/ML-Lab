# Polynomial Regression with Lasso and Ridge Regularization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, Lasso, Ridge

# Creating synthetic dataset
np.random.seed(0)
X = 2 - 3 * np.random.rand(100)
y = X**2 + np.random.randn(100) * 0.5

# Reshaping X for sklearn
X = X[:, np.newaxis]

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Transforming data for polynomial regression
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X_train)

# Fitting Linear Regression to the Polynomial Features
lin_reg = LinearRegression()
lin_reg.fit(X_poly, y_train)
# Predicting on the test set
X_test_poly = poly.transform(X_test)
y_pred = lin_reg.predict(X_test_poly)
# Lasso Regression
lasso_reg = Lasso(alpha=1.0)  # You can adjust the alpha parameter for regularization strength
lasso_reg.fit(X_poly, y_train)
y_pred_lasso = lasso_reg.predict(X_test_poly)
# Ridge Regression
ridge_reg = Ridge(alpha=1.0)  # You can adjust the alpha parameter for regularization strength
ridge_reg.fit(X_poly, y_train)
y_pred_ridge = ridge_reg.predict(X_test_poly)
# Visualizing the results
plt.scatter(X, y, color='blue', label='Data')
plt.scatter(X_test, y_test, color='green', label='Test Data', marker='x')
plt.plot(X_test, y_pred, color='red', label='Linear Regression')
plt.plot(X_test, y_pred_lasso, color='orange', label='Lasso Regression')
plt.plot(X_test, y_pred_ridge, color='purple', label='Ridge Regression')
plt.title('Polynomial Regression with Lasso and Ridge')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
