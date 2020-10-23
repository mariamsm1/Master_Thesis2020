#plot 2d histogram

import matplotlib.pyplot as plt
import numpy as np
 
df = pd.read_csv("/lunarc/nobackup/projects/snic2020-6-41/Mariam/Mariam_Thesis/Test_files/CP_plots_and_their_data/170521130001_data/170521130001_d0_data/CP_output_127d0/Classify_Object_C01_Corr05Nuclei.csv") 

area = df.AreaShape_Area
intensity = df.Intensity_IntegratedIntensity_RescaleIntensity_nuclei

 
# Big bins
plt.hist2d(intensity, area, bins=[100,70], cmap=plt.cm.jet) 
plt.xticks(np.arange(910, step=10))
plt.colorbar()
plt.rcParams["figure.figsize"] = (35,15)
plt.xticks(np.arange(950, step=50))
plt.yticks(np.arange(6800, step = 100))
plt.savefig("histogram_2d_02.png")



#2nd way 

# df = pd.read_csv("/Users/mariamsm/Desktop/Classify_Object_C01_Corr05Nuclei.csv") 

# area = df.AreaShape_Area
# intensity = df.Intensity_IntegratedIntensity_RescaleIntensity_nuclei

# intensity_min = np.min(intensity)
# intensity_max = np.max(intensity)

# area_min = np.min(area)
# area_max = np.max(area)

# intensity_bins = np.linspace(intensity_min,intensity_max,100)
# area_bins = np.linspace(area_min,area_max,70)

# plt.hist2d(intensity,area,bins=[intensity_bins,area_bins], cmap=plt.cm.jet)
# plt.colorbar()
# plt.xlabel('Integrated Intensity')
# plt.ylabel('Nuclear Area')
# plt.xticks(np.arange(950, step=10))
# plt.yticks(np.arange(7000, step = 100))
# plt.rcParams["figure.figsize"] = (35,15)
# plt.savefig("histogram_2d_corr05.png")


