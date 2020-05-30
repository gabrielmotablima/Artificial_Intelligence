# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# Some parameters
qtt_filters = [32, 16]
filter_dim = (3,3)

# Initialising the CNN
classifier = Sequential()

# Convolutional Operation
classifier.add(
  Conv2D(qtt_filters[0],
         filter_dim,
         input_shape = (64, 64, 3),
         activation = 'relu'))

# Pooling Operation
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Convolution and Pooling in sequence
classifier.add(Conv2D(qtt_filters[1],
                      filter_dim,
                      activation = 'relu'))

classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Flattening Operation
classifier.add(Flatten())

# Fully-Connected Layer
classifier.add(Dense(units = 100,
                     activation = 'relu'))

classifier.add(Dense(units = 1,
                     activation = 'sigmoid'))

# Compiling the CNN
classifier.compile(optimizer = 'adam',
                   loss = 'binary_crossentropy',
                   metrics = ['accuracy'])
