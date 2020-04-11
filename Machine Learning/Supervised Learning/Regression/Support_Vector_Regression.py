###################################################################################################
#################################### Support Vector Regression ####################################
###################################################################################################
##################################### Run on Jupyter Notebook #####################################
###################################################################################################

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('<YOUR_DATA>.csv')
X = dataset.iloc[:, <INDEPENDENT_VARIABLES_COLUMNS>].values
y = dataset.iloc[:, <DEPENDENT_VARIABLES_COLUMN>].values

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

# Fitting SVR to the dataset
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X, y)

# Predicting a new result
y_pred = regressor.predict(6.5)
y_pred = sc_y.inverse_transform(y_pred)

# Visualising the SVR results
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Support Vector Regression')
plt.xlabel('DEPENDENT_VARIABLES_COLUMNS (X_VARIABLES)')
plt.ylabel('INDEPENDENT_VARIABLES_COLUMNS (Y_VARIABLES)')
plt.show()

# Visualising the SVR results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.01) # choice of 0.01 instead of 0.1 step because the data is feature scaled
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Support Vector Regression - Smoother Curve')
plt.xlabel('DEPENDENT_VARIABLES_COLUMNS (X_VARIABLES)')
plt.ylabel('INDEPENDENT_VARIABLES_COLUMNS (Y_VARIABLES)')
plt.show()
