#### This directory contains scripts that were used before and throughout the binary classification task. 
- 4 images directories were created in **renamingImages.py**. Their names were changed to prevent names overlap (e.g. MFGTMPcx7_170528090001_B23f03d1.png corresponds to the original cell image as well as CP output images such as OverlayOutlines/IdentifySecondaryObjects..etc). <br>


- Original as well as CP outputted images were all put in one directory afterwards and were cropped using **crop.py**. This script was originally written by a previous master student in our lab, and then I modified it and adjusted it to the purpose of the task. **P.S.** the output .csv file from CellProfiler has the columns FileName_Cell and FileName_Mitochondria, I replaced the format of the images in these two columns from .C01 to .png and then I ran the script crop.py.


- cross-validation.ipynb contains a script that splits the directories into train, validation and test where train and validation were put in 3 rounds to make cross validation across all the dataset. The splits were made on objects based on the original lysosomal images.


- rotate_flip_augmentation.py is the script where I augmented my dataset by making a 90, 180 and 270 degree rotation of each single cell image and then also of these three and the original image a vertical flip. 


- Brightness_augmentation.ipynb is the script where brightness of 10 test images were increased and decreased to see their pattern.
 
