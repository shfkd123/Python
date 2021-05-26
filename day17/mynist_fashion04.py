import tensorflow as tf
import numpy as np
import cv2

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images_refine = train_images / 255.0
test_images_refine = test_images / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)

img = cv2.imread('baji.jpg', cv2.IMREAD_GRAYSCALE)
img_28 = cv2.resize(img, dsize=(28,28))
cv2.imshow('Image1', img_28)
cv2.imshow('Image2', test_images[0])
img_28_refine = img_28 / 255.0
img_28_refine = img_28_refine.reshape((1, 28, 28))

predictions = model.predict(test_images_refine)

print(np.argmax(predictions))

cv2.waitKey(0)
cv2.destroyAllWindows()
