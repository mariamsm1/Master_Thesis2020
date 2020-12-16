# Master thesis in Bioinformatics
**This project is carried out at Lund University's biomedical center (BMC) under the supervision of Sonja Aits.**

The aim of the project is to analyze microscopic images of transfected U2OS osteocarcinoma cells. The analysis involves segmentation of cells' cellular components such as nuclei, lysosomes, and mitochondria. This plays an important role in not just the detection of morphological changes in the tumor cells but also in counting these objects. <br>
The project involves two main tasks : objects segmentation through CellProfiler software (v4.0.7) and *write later about the ML task*. <br> 
For the first task, different pipelines were built to try identify the objects and to do some measurements like measuring objects intensity and measuring objects size and shape. These pipelines were evaluated and the best object-segmentation pipeline was chosen to build a full image analysis pipeline at the end. Running the scripts and building the pipelines were done on Lunarc cluster.

## Dependencies, softwares, and platforms
* python v3.7.0 <br>
* Cellprofiler v4.0.7 <br>
* ThinLinc Client v4.12.0 <br>

## Quick tour in the directories
* Images <br>
Includes the list of annotated images for each of the channels (d0,d1,and d2)
