#Plotting integrated Intensity 

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv("/lunarc/nobackup/projects/snic2020-6-41/Mariam/Mariam_Thesis/Test_files/CP_plots_and_their_data/170521130001_data/170521130001_d0_data/CP_output_127d0/Classify_Object_C01_Corr05Nuclei.csv") 

out = open('step127_Grouped_5.csv', 'w')
print('ImageNumber', 'Step' , sep = ',', file = out)

#save images number in a dataframe to be able to access them
images = df.ImageNumber.unique()
for i in range(len(images)):
    step_list= []
    #locate the images in the file
    data = df.loc[df.ImageNumber == images[i]].reset_index()
    #locate intensities for each image
    intensity = data.Intensity_IntegratedIntensity_RescaleIntensity_nuclei
    for j in range(len(intensity)):
        #empty the step for each intensty value
        step = 0
        while True:
            if data.Intensity_IntegratedIntensity_RescaleIntensity_nuclei[j] < step:
                step_list.append(step)
                break
            step = step+5 #This can be changed to the desired step size
    for x in step_list:
        print(images[i],x, sep =',', file = out)
            
        
df = pd.read_csv("step127_Grouped_5.csv") 

step = df.Step
plt.rcParams["figure.figsize"] = (45,8)
plt.hist(step, bins = len(np.arange(0,950,10))) #bins = 950/10 ~ 100
plt.xticks(np.arange(950, step=10))
plt.xlabel('Integrated Intensity')
plt.ylabel('Number of Nuclei')
plt.savefig('Intensity_step127_Grouped_5.png')

