## Start training a binary classifier
import re
import numpy as np
import cv2
import os,sys
import glob
from matplotlib import pyplot as plt
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Input, MaxPooling2D, Activation, BatchNormalization, Concatenate, Dropout, Add
from tensorflow.keras.applications.vgg16 import VGG16


#start with round1
path_train = '/home/marmia/snic2020-6-41/Mariam/Mariam_Thesis/Results_Pipelines_Images/Binary_Classifier_data/Objects_split/round1/Train'
path_val = '/home/marmia/snic2020-6-41/Mariam/Mariam_Thesis/Results_Pipelines_Images/Binary_Classifier_data/Objects_split/round1/Validation'

####fix train images

train_images = []
train_labels = []
count=0
train_list = glob.glob(path_train+'/*')
for im in train_list:
    #get the labels
    label = re.split('[_.]',im)[12]
    train_labels.append(label)
    #read the image in RGB because vgg16 only takes rgbs
    im = cv2.imread(im)
    im =  cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    train_images.append(im)

    
#convert lists to arrays
train_labels = tf.keras.utils.to_categorical(np.array(train_labels),num_classes = 2, dtype ="int8")
train_images = np.array(train_images)


####fix validation images

val_images = []
val_labels = []

val_list = glob.glob(path_val+'/*')
for im in val_list:
    #get the labels
    label = re.split('[_.]',im)[12]
    val_labels.append(label)
    #read the image in RGB because vgg16 only takes rgbs
    im = cv2.imread(im)
    im =  cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    val_images.append(im)
    
#convert lists to arrays
val_labels = tf.keras.utils.to_categorical(np.array(val_labels),num_classes = 2, dtype ="int8")
val_images = np.array(val_images) 

#rename to x-train,x-test,y-train,y-test
x_train,y_train,x_val,y_val = train_images,train_labels,val_images,val_labels

###check the images
# for i in x_train:
#     plt.imshow(i)
#     plt.show()

#make sure hey are RGB
#y = x_train[0]
# y[:,:,0] = 0 
# plt.imshow(y)

#if dtype was float, we need to divide by 255.0 not 255
#print(y.dtype)

#Normalize images pixels between 0 and 1
x_train,x_val = x_train/255, x_val/255


#predefine image shape
#predefine image shape
Image_size = (224,224,3)

#loading the model
#include_top = false will remove the last layer because i have 2 categories only, not 1000 as imagenet
vgg = VGG16(input_shape = Image_size , weights = 'imagenet', include_top = False)
#vgg.summary()
        
#to prevent training existing weights
for layer in vgg.layers:
        layer.trainable = False

#build the model
x = vgg.input
y = vgg.output # a vector with a size of 2 for each image (2 probabilities)
y = Flatten(name = 'flatten')(y)
#normaliza the input to the neural network to speed up training
y = BatchNormalization()(y)
y = Dense(1024, activation='relu', name = 'FC1')(y)
y = Dropout(0.5)(y)
y = Dense(64, activation='relu', name = 'FC2')(y)
y = Dropout(0.2)(y)
y = Dense(2, activation = 'softmax', name = 'prediction')(y)
model = Model(inputs = x, outputs = y)
#model.summary()
#plot_model(model, to_file='/home/marmia/snic2020-6-41/Mariam/Mariam_Thesis/Notebooks_Master/train1/model1.png')

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#save results to a csv
csv_logger = tf.keras.callbacks.CSVLogger('train_log.csv', append=True, separator=',')
checkpoint = tf.keras.callbacks.ModelCheckpoint(filepath='model.{epoch:02d}-{val_accuracy:.2f}.h5', monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')
#stop the training when there's no improvement in the accuracy anymore 
#set patience which is the number of epochs after which no improvment in training is observed
callback = tf.keras.callbacks.EarlyStopping(monitor='val_accuracy', mode = 'max',patience=7)
#train the model #each batch includes 32 batches by default
hist = model.fit(x_train, y_train,epochs=50, validation_data=(x_val, y_val), callbacks = [csv_logger,checkpoint,callback],verbose=1)
print("Done!")
model.save_weights('Final_VGG16.h5') 

#plot the results
#Plot loss and accuracy
plt.figure()
plt.plot(hist.history["loss"], label = "train_loss")
plt.plot(hist.history["val_loss"], label = "val_loss")
plt.plot(hist.history["accuracy"], label = "acc")
plt.plot(hist.history["val_accuracy"], label = "val_acc")
plt.title("Training loss and Accuracy on VGG16")
plt.xlabel("Number of epochs")
plt.ylabel("Loss/Accuracy")
plt.legend(loc = "best")
plt.savefig('train10_50epochs.png')

#history for accuracy
fig = plt.figure()
plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train_acc', 'val_acc'],loc='upper left')
plt.show()
fig.savefig('accuracy_curve.png')

# summarize history for loss
fig = plt.figure()
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train_loss', 'val_loss'],loc='upper left')
plt.show()
fig.savefig('loss_curve.png')

