### Brief Description of the pipelines evaluated
- Nuclei were evaluated on validation set-images obtained from https://lu.app.box.com/s/mujhztlh3i1vltai9a1ahgajkugmqkki/folder/123251275532. 6 different pipelines with different parameters were tried out on these Images (Total = 10).Another evaluation was carried on 40 images (check Evaluation_Notebooks).

- Cells were evaluated on validation set-images found in /lunarc/nobackup/projects/snic2020-6-41/Mariam/Mariam_Thesis/Results_Pipelines_Images/Images/Images_And_Summary/Original_Raw_Normalized_Images/C01_images/d1_originals/Validation_Images (Total = 15).

- Lysosomes were evaluated on validation set-images found in /home/marmia/snic2020-6-41/Mariam/Mariam_Thesis/Results_Pipelines_Images/Images/Images_And_Summary/Original_Raw_Normalized_Images/lysosome_images/boundary_labels (Total = 13).<br>
<br>
<br>

**P.S. Nuclei were evaluated based on CP segmentation HOWEVER we decided to introduce the raw annotations (ground truth/annotated with CVAT) of the nuclei as objects and segment cells accordingly**. *The reason for this is because CP nuclei segmentation was not perfect*.
<br>
<br>

- All of the pipelines were evaluated with the evaluation script found in /lunarc/nobackup/projects/snic2020-6-41/Mariam/Mariam_Thesis/Results_Pipelines_Images/Images/Images_And_Summary/imageanalysis/Evaluation_Script.
- Cell and lysosomes pipelines were evaluated based on raw annotated-nuclear objects (these were the input). Nuclear objects that were used in cell pipelines were not filtered at the borders for evaluation BUT nuclei whose area is < 100 were removed to discard micronuclei.

- Nuclei and Cell pipelines were evaluated on thresholds ranging from 0.5-0.95. These thresholds were averaged to obtain the average F1 score and average Jaccard index.

- Lysosomes pipelines were evaluated on thresholds ranging from 0.1-0.95. Therefore, even 10% pixels overlap between ground truth and predictions-images will still be considered as true positive.These thresholds were averaged to obtain the average F1 score and average Jaccard index.

- Lysosomes belonging to the first 2 lysosomal pipelines were reduced by 1 pixel in size, the rest were not ( the reason for this was to try increase the evaluation scores for the first two pipelines).
- **Refer to pipelines folder in order to see the differences between pipelines corresponding to same object.**
