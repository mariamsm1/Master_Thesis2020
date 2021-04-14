# Master thesis in Bioinformatics
**This project is carried out at Lund University's biomedical center (BMC) under the supervision of Sonja Aits.**

The aim of the project is to analyze microscopic images of transfected U2OS osteocarcinoma cells. The analysis involves segmentation of cells' cellular components such as nuclei, lysosomes, and mitochondria. This plays an important role in not just the detection of morphological changes in the tumor cells but also in counting these objects. <br>
The project involves two main tasks : objects segmentation through CellProfiler software (v4.0.7) and a machine learning task to train a binary classifier on broken lysosomes- and normal-cells images. <br> 
For the first task, different pipelines were built to try identify the objects and to do some measurements like measuring objects intensity and measuring objects size and shape. These pipelines were evaluated using an evaluation script, written originally at the Broad Institue, and the best object-segmentation pipeline was chosen to build a full image analysis pipeline at the end. Running the scripts and building the pipelines were done on Lunarc cluster.<br>
In the second task, the first step was to use 24 Unet segmented-nuclei images (done by a colleague) as input images in CellProfiler to get the corresponding x and y coordinates of each object (i.e. nucleus) in order to crop, based on each object's center, a 224x224 image. This was applied on several images sets and most importantly on the cells images which were used for the binary classification step.

## Dependencies, softwares, and platforms
* python v3.7.0 <br>
* Cellprofiler v4.0.7 <br>
* ThinLinc Client for macOS v4.12.0 <br>

## Packages and libraries
* See packages.py
* Matplotlib library v2.2.3

## Quick tour in the directories
* Images <br>
Includes the list of annotated images for each of the channels (d0,d1,and d2). These Images were used in the evaluation of my pipelines.There are 40 nuclei images that were evaluated to further test whether pipelines are better with or without illumination correction. See folder's READme for more details about the paths.<br>


* Pipelines <br>
Includes all the illumination correction pipelines that were tested during the project (see *Illumination_Correction*) as well as nuclei, cell and lysosomes pipelines that were evaluated using the evaluation script (see *Nuclei_pipelines, Cell_pipelines, and Lysosomes_pipelines* respectively). The directory contains as well the full segmentation pipeline for all the objects mentioned earlier (all grouped together). The difference in the pipelines for each object segmentation lies mainly in the IdentifyPrimaryObjects module, specifically Thresholding strategy/Thresholding method/Threshold smoothing scale/Threshold correction factor. Some other changes in the parameters were done if the pipeline has smoothing modules (e.g. lysosomes pipeline) and Morph (e.g. mitochondria). See folders' READme files for more details about each folder's content.<br>


* Results <br>
Contains the evaluation script that was modified by one of the master students at our lab and further modified by me to be able to run multiple cellprofiler images at once. One evaluation script was run per one pipeline for a given object and the same was true for illumination-corrected pipelines and illumination-uncorrected pipelines. Note that the **utils** folder must be placed in the same directory as the evaluation script before running it. for changing the false positive and false negative thresholds in the script: <br>
  1. Go to **utils/evaluation.py** 
  2. Change threshold = ... in FPs and FNs functions (e.g. threshold = 0.1).
  3. OR add to the FPs and FNs def functions in the evaluation script (4th cell) the desired threshold(after image_name).

  This folder contains also the plotting scripts:<br>
    1. To compare the effect of illumination correction on the evaluation (see IlluminationVsNoIllumination.ipynb). 
    2. To see the size distribution of ground truth objects belonging to lysosomes, nuclei, an cells (see Size_Distribution_Plots_Raw_Annotation folder).
    3. To compare the number of spots and area distribution of lysosomes in ground truth images vs cellprofiler segmented images.
    4. To calculate the average number of lysosomes per cell.
  
  For points 3 and 4, see LysoSpots_number_and_area_CPvsRaw folder. Note that the best pipeline (i.e. the pipeline with the best evaluation) was used for calculations and comparisons.

* Machine Learning <br>
Contains the main analysis scripts that were used before and throughout the classification task.<br>
The folder involves the following: <br>
1. Preprocessing-scripts : 
. crop.py : crops original nuclei, cells, mitochondria images + lysosome images + predicted CellProfiler's cell images + predicted nuclei images from the best Unet's model + overlay lysosomes on top of cells images. All of these images were cropped to 224x224 based on center coordinates of the predicted nuclei images.
. mask-and-split.py : masks objects around the center object (cell) to obtain a single cell image or training the classifier.
. cross-validation.ipynb : script for splitting data into train,validation and test images.
. rotate_flip_augmentation.py: performs rotation and flipping augmentation on the single cell images.
. Brightness_augmentation.ipynb : performs brightness augmentation on single cell images.

2. Models:
See Models_summary.ipynb to have an insight about the different models trained in this project.

3. Loss_and_accuracy_curves.ipynb:
Summarizes the loss and accuracy curves of the trained models in one plot for each.

