'''This script masks out all the objects around the center object the cropped image so
it will copy the pixels of the center objects only. '''

import skimage.io
import matplotlib.pyplot as plt
from skimage.color import rgb2lab,rgb2grey
import glob
import os,sys
import cv2

path_mask = '/home/marmia/snic2020-6-41/Mariam/Mariam_Thesis/Results_Pipelines_Images/Binary_Classifier_data/All_images_r1r2_pred'
path_im = '/home/marmia/snic2020-6-41/Mariam/Mariam_Thesis/Results_Pipelines_Images/Binary_Classifier_data/All_images_r1r2_orig'

all_mask = sorted(os.listdir(path_mask))
all_im = sorted(os.listdir(path_im))

subdir = '/home/marmia/snic2020-6-41/Mariam/Mariam_Thesis/Notebooks_Master/Masked_cropped_cells'
for i,j in zip(all_mask, all_im):
    maskpath = os.path.join(path_mask, i)
    mask = cv2.imread(maskpath)
    impath = os.path.join(path_im, j)
    im = cv2.imread(impath)
    
    mask = rgb2grey(mask)
    #take the center of the image
    #length/2
    centerx = int(im.shape[0]/2)
    #width/2
    centery = int(im.shape[1]/2)
    #find the color of the center mask
    maskcolor = mask[centerx-1][centery-1]
    newim= im.copy()
    #Set the surrounding masks pixels to 0 if they have a different color from the center mask
    newim[mask!=maskcolor] = 0
    #fig,[ax0,ax1,ax2] = plt.subplots(1,3,figsize = (20,15))
    #ax0.imshow(mask)
    #ax1.imshow(im)
    #ax2.imshow(newim)
    #plt.show()
    cv2.imwrite("{0}/{1}".format(subdir,j),newim)



# 
