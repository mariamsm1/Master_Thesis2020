### Cellprofiler pipelines: 
- Nuclei were evaluated on validation set-images obtained from https://lu.app.box.com/s/mujhztlh3i1vltai9a1ahgajkugmqkki/folder/123251275532. 6 different pipelines with different parameters were tried out on these Images (Total = 15).
- Cells were evaluated on validation set-images found in /lunarc/nobackup/projects/snic2020-6-41/Mariam/Mariam_Thesis/Results_Pipelines_Images/Images/Images_And_Summary/Original_Raw_Normalized_Images/C01_images/d1_originals/Validation_Images (Total = 15).
- Lysosomes were evaluated on validation set-images found in /home/marmia/snic2020-6-41/Mariam/Mariam_Thesis/Results_Pipelines_Images/Images/Images_And_Summary/Original_Raw_Normalized_Images/lysosome_images/boundary_labels (Total = 13).
- All of the pipelines were evaluated with the evaluation script found in /lunarc/nobackup/projects/snic2020-6-41/Mariam/Mariam_Thesis/Results_Pipelines_Images/Images/Images_And_Summary/imageanalysis/Evaluation_Script.
- Nuclei and Cell pipelines were evaluated on thresholds ranging from 0.5-0.95. These thresholds were averaged to obtain the average F1 score and average Jaccard index.
- Lysosomes pipelines were evaluated on thresholds ranging from 0.1-0.95. Therefore, even 10% pixels overlap between ground truth and predictions will still be considered as true positive.These thresholds were averaged to obtain the average F1 score and average Jaccard index.
- **Refer to pipelines folder in order to see the differences between pipelines corresponding to same object.**
