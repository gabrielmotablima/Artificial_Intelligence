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
    - I'll draw a simple explanation:
        
        The K-Nearest Neighbors Algorithm classify a new sample based on the already registered samples. For example:
        
        i.
        ![Data1](Illustrations/Data1.png)
        
        ii.
        ![Data2](Illustrations/Data2.png)
        
        iii.
        ![Data3](Illustrations/Data3.png)
        
        iv.
        ![Zoom](Illustrations/Zoom.png)
        
        v.
        ![Zoom2](Illustrations/Zoom2.png)
