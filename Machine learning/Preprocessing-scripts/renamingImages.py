#!/usr/bin/env python3

''' This script aimed at changing the name of the images from different folders
because they had same images

run as : python3 renamedImages.py'''

import glob
import os
import shutil


#get the big directory
folders_list = glob.glob('/Users/mariamsm/Desktop/Binary_Classifier_data/*')

#get the path of all the folders and files in the big directory
path = '/Users/mariamsm/Desktop/Binary_Classifier_data/*'
#loop through the big directory to get the subdirectories
for folders in glob.glob(path):
	#take only the directories and discard the files if the directory has any
	if os.path.isdir(folders):
		#check based on parts of the file name
		if 'Lys' in folders:
			folder = os.listdir(folders)
			for file in folder:
				#rename the images and copy from source directory to the desired directory
				#rename the manually annotated lysosomes
				img1 = file.split('.')[0] + '_Lysd1.png'
				shutil.copy2('/Users/mariamsm/Desktop/Binary_Classifier_data/Lys-annotationset1/' + file, 'renamed_images/' + img1)
				# rename the model-predicted nuclear images
		elif 'labels' in folders:
			folder = os.listdir(folders)
			for file in folder:
				img2 = file.split('.')[0] + '_labd0.png'
				shutil.copy2('/Users/mariamsm/Desktop/Binary_Classifier_data/d0_labels_predictions/' + file, 'renamed_images/' + img2)
				#rename the CP predicted cells images
		elif 'secondary' in folders:
			folder = os.listdir(folders)
			for file in folder:
				img3 = file.split('.')[0] + '_prdd1.png'
				shutil.copy2('/Users/mariamsm/Desktop/Binary_Classifier_data/Binary_secondaryObjects_cells/' + file, 'renamed_images/' + img3)
				#rename the CP output od cells overlay outlines
		elif 'overlay' in folders:
			folder = os.listdir(folders)
			for file in folder:
				img3 = file.split('.')[0] + '_ovrd1.png'
				shutil.copy2('/Users/mariamsm/Desktop/Binary_Classifier_data/Binary_overlay_cells/' + file, 'renamed_images/' + img3)
