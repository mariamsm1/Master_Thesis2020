# Master thesis in Bioinformatics
**This project is carried out at Lund University's biomedical center (BMC) under the supervision of Sonja Aits.**

The aim of the project is to analyze microscopic images of transfected U2OS osteocarcinoma cells. The analysis involves segmentation of cells' cellular components such as nuclei, lysosomes, and mitochondria. This plays an important role in not just the detection of morphological changes in the tumor cells but also in counting these objects. <br>
The project involves two main tasks : objects segmentation through CellProfiler software (v4.0.7) and *write later about the ML task*. <br> 
For the first task, different pipelines were built to try identify the objects and to do some measurements like measuring objects intensity and measuring objects size and shape. These pipelines were evaluated using an evaluation script, written originally at the Broad Institue, and the best object-segmentation pipeline was chosen to build a full image analysis pipeline at the end. Running the scripts and building the pipelines were done on Lunarc cluster.

## Dependencies, softwares, and platforms
* python v3.7.0 <br>
* Cellprofiler v4.0.7 <br>
* ThinLinc Client v4.12.0 <br>

## Quick tour in the directories
* Images <br>
Includes the list of annotated images for each of the channels (d0,d1,and d2). These Images were used in the evaluation of my pipelines.There are 40 nuclei images that were evaluated to further test whether pipelines are better with or without illumination correction. See folder's READme for more details about the paths.<br>
* Pipelines <br>
Includes all the illumination correction pipelines that were tested during the project (see *Illumination_Correction*) as well as nuclei, cell and lysosomes pipelines that were evaluated using the evaluation script (see *Nuclei_pipelines, Cell_pipelines, and Lysosomes_pipelines* respectively). The difference in the pipelines for each object segmentation lies mainly in the IdentifyPrimaryObjects module, specifically Thresholding strategy/Thresholding method/Threshold smoothing scale/Threshold correction factor. Some other changes in the parameters were done if the pipeline has smoothing modules (e.g. lysosomes pipeline) and Morph (e.g. mitochondria). See folders' READme files for more details about each folder's content.
