#scatterplot corr5 Area vs integrated intensity
import matplotlib.pyplot as plt
import numpy as np

area_list = []
intensity_list = []

df = pd.read_csv("/lunarc/nobackup/projects/snic2020-6-41/Mariam/Mariam_Thesis/Test_files/CP_plots_and_their_data/170521130001_data/170521130001_d0_data/CP_output_127d0/Classify_Object_C01_Corr05Nuclei.csv") 

area = df.AreaShape_Area
intensity = df.Intensity_IntegratedIntensity_RescaleIntensity_nuclei
plt.scatter(intensity, area, color='r')
plt.xlabel('Integrated Intensity')
plt.ylabel('Nuclear Area')
plt.savefig('AreaVSIntensity_corr05.png')
