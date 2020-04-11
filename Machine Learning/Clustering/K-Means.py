###################################################################################################
############################################# K-Means #############################################
###################################################################################################
##################################### Run on Jupyter Notebook #####################################
###################################################################################################

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset, you can just substitute YOUR_DATE for your file's name,
# choose the interval of independent and dependent variables in your CSV file
# And finally run the code, change it on X_Y_VARIABLES.
# This dataset suppose that X and Y variables are neighbors columns
dataset = pd.read_csv('YOUR_DATE.csv')
X = dataset.iloc[:, [X_Y_VARIABLES]].values
dataset.head()

# Using the Elbow Method to find the optimal number os clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
	kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
	kmeans.fit(X)
	wcss.append(kmeans.inertia_)
plt.plot(range(1,11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Apllying k-means to the dataset
# By the Elbow Method you'll suppose a clusters number to carry out
# change it on N_CLUSTERS
kmeans = KMeans(n_clusters = N_CLUSTERS, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
y_kmeans = kmeans.fit_predict(X)

# Visualising the clusters
plt.scatter(X[y_kmeans==0, 0],X[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_kmeans==1, 0],X[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_kmeans==2, 0],X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_kmeans==3, 0],X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(X[y_kmeans==4, 0],X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
# ... How many clusters you need
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of data')
plt.xlabel('X_VARIABLES')
plt.ylabel('Y_VARIABLES')
plt.legend()
plt.show()
