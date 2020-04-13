# K-Nearest Neighbors Algorithm

Docummentaton: https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
![KNN](Illustrations/KNN.png)



1. If you are looking for the K-NN method only, here it is:
    - Check the docummentation for the parametrization of "KNeighborsClassifier()".
    - <x_train>, <y_train> and <whatever_you_want> are data arrays that you have already pre-processed.
    ```py
    from sklearn.neighbors import KNeighborsClassifier
    classifier = KNeighborsClassifier() 
    classifier.fit( <x_train> , <y_train> )
    prediction = classifier.predict( <whatever_you_want> )
    ```



2. If you want to know more about the algorithm, including data processing (pre-processing, visualization and tuning):
    - Can you look the code into file "K-NN.py"
    - Can you look the explanations in:
      - http://saedsayad.com/k_nearest_neighbors.htm
      - https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761
      - https://towardsdatascience.com/introduction-to-k-nearest-neighbors-3b534bb11d26
      - https://towardsdatascience.com/knn-k-nearest-neighbors-1-a4707b24bd1d
      - https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
