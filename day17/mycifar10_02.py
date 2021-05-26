import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets, layers, models
import cv2
 
cifar10 = datasets.cifar10 
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()
 
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
 
train_images = train_images.reshape((50000, 32, 32, 3))
test_images = test_images.reshape((10000, 32, 32, 3))
 
for i,img in enumerate(train_images):
    cv2.imwrite('cifar_train/'+str(train_labels[1][0])+ '_'+ str(i)+'.jpg', train_images[i])
    if i > 100:
        break

for i,img in enumerate(test_images):
    cv2.imwrite('cifar_train/'+str(test_labels[1][0])+ '_'+ str(i)+'.jpg', test_images[i])
    if i > 100:
        break