import pandas as pd
#from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import keras
from sklearn.model_selection import train_test_split
from keras.layers import Conv2D, MaxPool2D, AveragePooling2D, Input, BatchNormalization, MaxPooling2D, Activation, Flatten, Dense, Dropout
from keras.models import Model
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import classification_report
#from imblearn.over_sampling import RandomOverSampler
from keras.preprocessing import image
import scipy
import os
import cv2


def emotion_recognition(input_shape):
    X_input = Input(input_shape)

    X = Conv2D(32, kernel_size=(3, 3), strides=(1, 1), padding='valid')(X_input)
    X = BatchNormalization(axis=3)(X)
    X = Activation('relu')(X)

    X = Conv2D(64, (3, 3), strides=(1, 1), padding='same')(X)
    X = BatchNormalization(axis=3)(X)
    X = Activation('relu')(X)

    X = MaxPooling2D((2, 2))(X)

    X = Conv2D(64, (3, 3), strides=(1, 1), padding='valid')(X)
    X = BatchNormalization(axis=3)(X)
    X = Activation('relu')(X)

    X = Conv2D(128, (3, 3), strides=(1, 1), padding='same')(X)
    X = BatchNormalization(axis=3)(X)
    X = Activation('relu')(X)

    X = MaxPooling2D((2, 2))(X)

    X = Conv2D(128, (3, 3), strides=(1, 1), padding='valid')(X)
    X = BatchNormalization(axis=3)(X)
    X = Activation('relu')(X)

    X = MaxPooling2D((2, 2))(X)
    X = Flatten()(X)
    X = Dense(200, activation='relu')(X)
    X = Dropout(0.6)(X)
    X = Dense(7, activation='softmax')(X)

    model = Model(inputs=X_input, outputs=X)

    return model

model = emotion_recognition((48,48,1))

label_dict = {0 : 'Angry', 1 : 'Disgust', 2 : 'Fear', 3 : 'Happy', 4 : 'Sad', 5 : 'Surprise', 6 : 'Neutral'}