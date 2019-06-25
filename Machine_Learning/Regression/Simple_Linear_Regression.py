###################################################################################################
#################################### Simple Linear Regression #####################################
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
# Just set YOUR_DATA.csv in read_csv pandas function, INDEPENDENT_VARIABLES_COLUMNS in iloc(),
# DEPENDENT_VARIABLE_COLUMN in iloc() and see what happens
X = dataset.iloc[:, [INDEPENDENT_VARIABLES_COLUMNS]].values
y = dataset.iloc[:, DEPENDENT_VARIABLE_COLUMN].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Fitting Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Try printing y_pred, y_test and observe the results
print(y_pred)
print(y_test)

# Visualizing the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.scatter(X_test, y_pred, color = 'green')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title("Y_VARIABLE (DEPENDENT VARIABLE) vs X_VARIABLE (TRAINING SET, INDEPENDENT VARIABLE)")
plt.xlabel("X_VARIABLE")
plt.ylabel("Y_VARIABLE")
plt.show()
