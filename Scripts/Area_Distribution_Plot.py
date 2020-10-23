
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv("/lunarc/nobackup/projects/snic2020-6-41/Mariam/Mariam_Thesis/Test_files/CP_plots_and_their_data/170521130001_data/170521130001_d0_data/CP_output_127d0/Classify_Object_C01_Corr05Nuclei.csv") 

out = open('step_Area127Corr05_Grouped_5.csv', 'w')
print('Area', 'Step' , sep = ',', file = out)

#save images number in a dataframe to be able to access them
images = df.ImageNumber.unique()
for i in range(len(images)):
    step_list= []
    data = df.loc[df.ImageNumber == images[i]].reset_index()
    area = data.AreaShape_Area
    for j in range(len(area)):
        step = 0
        while True:
            if data.AreaShape_Area[j] < step:
                step_list.append(step)
                break
            step = step+5
    for x in step_list:
        print(images[i],x, sep =',', file = out)
            
        
df = pd.read_csv("step_Area127Corr05_Grouped_5.csv") 

step = df.Step
plt.rcParams["figure.figsize"] = (60,8)
plt.hist(step, bins = len(np.arange(0,7000,100))) #bins = 70000/100 = 70
plt.xticks(np.arange(7000, step=100))
plt.xlabel('Nuclei Area')
plt.ylabel('Number of Nuclei')
plt.savefig('d0_Area127Corr05_images_step5.png')
