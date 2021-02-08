#!/usr/bin/env python3
'''This script aimed at cropping original d0,d1,d2 images or images generated from CellProfiler.
All images were put in one directory (All_images).
In cropImg, the x and y are swapped because the code takes the second argument as the first.

run as:  python3 crop.py MyExpt_FilterObjects_pred.csv All_images'''


#Load packages
import argparse
import os
import cv2
import glob
import pandas as pd
import re
#argparse stuff
parser = argparse.ArgumentParser()
parser.add_argument('c', type = str, help = 'cell profiler data')
#argument for the cellprofiler data, should be name of the file
parser.add_argument('im', type = str, help = 'directory with microscopy images')
#directory where the images are (these are uncropped images)
#probably 1104x1104
args = parser.parse_args()
#####################

#Import and process cellPro output data
os.chdir('/Users/mariamsm/Desktop/Binary_Classifier_data')
#change this to whatever directory#
#your cellprofiler result csv is in#
print("Directory changed to script directory // READING CSV DATA")
imData = pd.read_csv(args.c) #Make this into a pandas df
print("DATA DONE READING")
imData = imData.drop(imData.columns.difference(['ImageNumber','ObjectNumber','FileName_DNA','FileName_Cell','FileName_Mito','Location_Center_X', 'Location_Center_Y']), axis = 1)
#Drop all columns that aren't important
imData.to_csv("Locations.csv", index = False)
#Save remaining data to new csv
print("DATA SAVED to Locations.csv")
#Import and process image(s).
imRaw = glob.glob('All_images/*') # '/*' will create a list that contains "/" at the end of the directory and the images names one by one in that directory e.g.['Original_d0_d1_d2/MFGTMPcx7_170528090001_B23f03d0.png',..etc)
imTest = cv2.imread(imRaw[0])#check content of directory is image files
imExt = imRaw[0].split('.')[-1] #get the extension of the images
#(this assumes all images are the same format)
dim = imTest[0].shape #get dimensions
#print(dim)

# counter = 0
subdirs = ['Lys_crop', 'secObj_crop', 'overlay_crop', 'd0Pred_crop','ch0Res', 'ch1Res', 'ch2Res']
#Using set to get a list of all image names
for subdir in subdirs:
	if not os.path.exists(subdir):
		os.makedirs(subdir)
	else:
		os.system('rm -rf %s/*' % subdir)
#
image_name = imData.FileName_DNA.unique()
#ImNum = imData.ImageNumber
#
for i in imRaw:
	if '_Lysd1' in i or '_prdd1' in i or '_ovrd1' in i or '_labd0' in i:
		# get the full name before the .png
		imName = re.split('[./]',i)[1]
		#get the name until d0.png,d1.png to use later
		i = re.split('[./]',i)[1][0:31] + '.' + imExt
		#consider taking the Lysd1 as the channel and so on
		imCh = imName[-5:]
		#read the desired images and save them to a variable
		imageVar = cv2.imread('All_images/' + imName + '.' + imExt )
		#create the directories depending on the how many images categories i have
		if imCh == 'Lysd1':
			subdir = subdirs[0]
		elif imCh == 'prdd1':
			subdir = subdirs[1]
		elif imCh == 'ovrd1':
			subdir = subdirs[2]
		elif imCh == 'labd0':
			subdir = subdirs[3]
		# the above categories are only d0 and d1 images so call the d0 and d1 images from the .csv
		images = imData.loc[(imData.FileName_DNA == i) | (imData.FileName_Cell == i)]
		objNum = images.ObjectNumber.unique()
		#each image had several objects so loop through them and save them to a variable
		for j in range(len(objNum)):
			objects = images.loc[images.ObjectNumber == objNum[j]]
			if objects.empty:
				continue
				#get the images whose objects x and y locations and greater than 112 because we need to cut from the object's center 112 in each direction
				#we don't want the cropped image to get out of the border
			else:
				nonBordIm = objects.loc[(objects['Location_Center_X'] > 112) & (objects['Location_Center_X'] < (dim[0] - 112))
							& (objects['Location_Center_Y'] > 112) & (objects['Location_Center_Y'] < (dim[0] - 112))]
				if nonBordIm.empty:
					continue
				else:
					x = nonBordIm['Location_Center_X'].tolist()
					x = [round(m) for m in x]
					y = nonBordIm['Location_Center_Y'].tolist()
					y = [round(k) for k in y]
					for m,k in zip(x,y):
						#crop based on the y and x locations (112 pixels from each direction)
						cropImg = imageVar[k - 112: k + 112, m - 112: m + 112].copy()
						cv2.imwrite("{0}/{1}_{2}_{3}_{4}-{5}.{6}".format(subdir,imName, j, str(m), str(k), '8bits',imExt), cropImg)
	else:
		imName = re.split('[./]',i)[1]
		i = re.split('[./]',i)[1][0:31] + '.' + imExt
		imCh = imName[-2:]
		imageVar = cv2.imread('All_images/' + imName + '.' + imExt)
		if imCh == 'd0':
			subdir = subdirs[4]
		elif imCh == 'd1':
			subdir = subdirs[5]
		elif imCh == 'd2':
			subdir = subdirs[6]
	#
		images = imData.loc[(imData.FileName_DNA == i) | (imData.FileName_Cell == i) | (imData.FileName_Mito == i)]
		objNum = images.ObjectNumber.unique()
		for j in range(len(objNum)):
			objects = images.loc[images.ObjectNumber == objNum[j]]
			if objects.empty:
				continue
			else:
				nonBordIm = objects.loc[(objects['Location_Center_X'] > 112) & (objects['Location_Center_X'] < (dim[0] - 112))
							& (objects['Location_Center_Y'] > 112) & (objects['Location_Center_Y'] < (dim[0] - 112))]
				if nonBordIm.empty:
					continue
				else:
					x = nonBordIm['Location_Center_X'].tolist()
					x = [round(m) for m in x]
					y = nonBordIm['Location_Center_Y'].tolist()
					y = [round(k) for k in y]
					for m,k in zip(x,y):
						cropImg = imageVar[k - 112: k + 112, m - 112: m + 112].copy()
						cv2.imwrite("{0}/{1}_{2}_{3}_{4}-{5}.{6}".format(subdir,imName, j, str(m), str(k), '8bits',imExt), cropImg)
print('Yay!Done.')
