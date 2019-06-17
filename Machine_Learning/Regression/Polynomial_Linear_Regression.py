###################################################################################################
################################## Polynomial Linear Regression ###################################
###################################################################################################
##################################### Run on Jupyter Notebook #####################################
###################################################################################################

# Importing the Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
# For .csv data in the same code's folder, otherwise you will have to specify the file address.
# The dataset have to be in format: | ID COLUMN | FEATURE COLUMNS | LABEL COLUMN |
dataset = pd.read_csv('YOUR_DATA.csv')
print(dataset)

# Visualizing the Independent and Dependent Variables
# Just set YOUR_DATA.csv in read_csv pandas function, INDEPENDENT_VARIABLES_COLUMNS in iloc,
# DEPENDENT_VARIABLE_COLUMN iloc() and see what happens
X = dataset.iloc[:, [INDEPENDENT_VARIABLES_COLUMNS]].values
y = dataset.iloc[:, DEPENDENT_VARIABLE_COLUMN].values

# Fitting Linear Regression Model of the Dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Fitting Polynomial Linear Regression of the Dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

# Visualising the Linear Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('Linear Regression')
plt.xlabel('DEPENDENT_VARIABLES_COLUMNS (X_VARIABLES)')
plt.ylabel('INDEPENDENT_VARIABLES_COLUMNS (Y_VARIABLES)')
plt.show()

# Visualising the Polynomial Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('DEPENDENT_VARIABLES_COLUMNS (X_VARIABLES)')
plt.ylabel('INDEPENDENT_VARIABLES_COLUMNS (Y_VARIABLES)')
plt.show()

# Visualising the Polynomial Regression results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color = 'red' )
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('DEPENDENT_VARIABLES_COLUMNS (X_VARIABLES)')
plt.ylabel('INDEPENDENT_VARIABLES_COLUMNS (Y_VARIABLES)')
plt.show()

# Predicting a new result with Linear Regression
lin_reg.predict(4)

# Predicting a new result with Polynomial Linear Regression
lin_reg_2.predict(poly_reg.fit_transform(4))
