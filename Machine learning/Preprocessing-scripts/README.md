#### This directory contains scripts that were used before the binary classification task. 
- 4 images directories were created in **renamingImages.py**. Their names were changed to prevent names overlap (e.g. MFGTMPcx7_170528090001_B23f03d1.png corresponds to the original cell image as well as CP output images such as OverlayOutlines/IdentifySecondaryObjects..etc). <br>
- Original as well as CP outputted images were all put in one directory afterwards and were cropped using crop.py. This script was originally written by a previous master student in our lab, and then I modified it and adjusted it to the purpose of the task.
- cross-validation.ipynb contains a script that splits the directories into train, validation and test where train and validation were put in 3 rounds to make cross validation across all the dataset. The splits were made on objects based on the original lysosomal images.
 
