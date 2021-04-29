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
import efficientnet.tfkeras as efc


count = 0
#start with round1
path_train = '/pfs/proj/nobackup/fs/projnb10/aits_storage/Mariam/All_augmented_images_train_val/round1/aug_train'
path_val = '/pfs/proj/nobackup/fs/projnb10/aits_storage/Mariam/All_augmented_images_train_val/round1/aug_val'

####fix train images

train_images = []
train_labels = []
count=0
train_list = glob.glob(path_train+'/*')
for im in train_list:
    #get the labels
    label = im.split('_')[-1].replace('.png','')
    train_labels.append(label)
    im = cv2.imread(im)
    im =  cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    train_images.append(im)


# #convert lists to arrays
train_labels = tf.keras.utils.to_categorical(np.array(train_labels), num_classes = 2, dtype = 'int8')
train_images = np.array(train_images)


####fix validation images

val_images = []
val_labels = []

val_list = glob.glob(path_val+'/*')
for im in val_list:
    #get the labels
    label = im.split('_')[-1].replace('.png','')
    val_labels.append(label)
    im = cv2.imread(im)
    im =  cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    val_images.append(im)

#convert lists to arrays
#to_categorical converts our array into binary class matrix. 
val_labels = tf.keras.utils.to_categorical(np.array(val_labels), num_classes =2 ,dtype = 'int8')
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



#loading the model
#include_top = false will remove the last layer because i have 2 categories only, not 1000 as imagenet
#predefine image shape
Image_size = (224,224,3)

efnet = efc.EfficientNetB7(input_shape = Image_size , weights = 'imagenet', include_top = False)


#build the model architecture again
x = efnet.input
y = efnet.output # a vector with a size of 2 for each image (2 probabilities)
y = Flatten(name = 'flatten')(y)
#normalize the input to the neural network to speed up training
y = BatchNormalization()(y)
y = Dense(32, activation='relu', name = 'FC1')(y)
y = Dropout(0.2)(y)
#y = Dense(512, activation='relu', name = 'FC2')(y)
#y = Dropout(0.5)(y)
y = Dense(2, activation = 'softmax', name = 'prediction')(y)
model = Model(inputs = x, outputs = y)

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#save results to a csv
csv_logger = tf.keras.callbacks.CSVLogger('train_log.csv', append=True, separator=',')
checkpoint = tf.keras.callbacks.ModelCheckpoint(filepath='model.{epoch:02d}-{val_accuracy:.2f}.h5', monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')
#set patience which is the number of epochs after which no improvment in training is observed
callback = tf.keras.callbacks.EarlyStopping(monitor='val_accuracy', mode = 'max',patience=20)
#train the model #each batch includes 32 batches by default
hist = model.fit(x_train, y_train,epochs=100, batch_size = 8, validation_data=(x_val, y_val), callbacks = [csv_logger,checkpoint,callback],verbose=1)
print("Done!")
model.save_weights('Final_Effnet.h5') 

#plot the results
#Plot loss and accuracy

plt.figure()
plt.plot(hist.history["loss"], label = "train_loss")
plt.plot(hist.history["val_loss"], label = "val_loss")
plt.plot(hist.history["accuracy"], label = "acc")
plt.plot(hist.history["val_accuracy"], label = "val_acc")
plt.title("Training loss and Accuracy on EffB7")
plt.xlabel("Number of epochs")
plt.ylabel("Loss/Accuracy")
plt.legend(loc = "best")
plt.savefig('train9_100epochs.png')

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
plt.ylim(0,5.5)
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train_loss', 'val_loss'],loc='upper left')
plt.show()
fig.savefig('loss_curve.png')
