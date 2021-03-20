count = 0

#I have 3 rounds (i.e. 3 folds) and each have train and validation folders so change the paths according to the round
#round1 (same thing for round2 and round3)
train_dir = glob.glob('/home/marmia/snic2020-6-41/Mariam/Mariam_Thesis/Results_Pipelines_Images/Binary_Classifier_data/Objects_split/round1/Train/*') 
val_dir = glob.glob('/home/marmia/snic2020-6-41/Mariam/Mariam_Thesis/Results_Pipelines_Images/Binary_Classifier_data/Objects_split/round1/Validation/*') 
round1_path = '/home/marmia/snic2020-6-41/Mariam/Mariam_Thesis/Results_Pipelines_Images/Binary_Classifier_data/Objects_split/round1/'


#create directories for the augmented train and validation images
subdirs = ['aug_train', 'aug_val']
for subdir in subdirs:
    if not os.path.exists(os.path.join(round1_path, subdir)):
        os.makedirs(os.path.join(round1_path, subdir))
    else:
        os.system('rm -rf %s/*' % os.path.join(round1_path, subdir))


        
#do the vertical flip and the rotations on the original images
for imt in train_dir:
    #copy the original images to the augmentation folders 
    shutil.copy2(imt,os.path.join(round1_path, subdirs[0]))
    #start with train images
    imt_label = imt.split('_')[-1] #0.png or 1.png
    #get train image name
    imtName = imt.split('/')[11].replace('_'+imt_label,'')#.replace(imt_label,'vflip_'+imt_label)
    imt = cv2.imread(imt)
    #flip vertically
    flip_imt= cv2.flip(imt, 0)
    cv2.imwrite("{0}/{1}_{2}_{3}".format(os.path.join(round1_path, subdirs[0]),imtName, 'vflip', imt_label), flip_imt)
    #rotate the original images 90 degrees
    Rotated_imt = imutils.rotate(imt, angle=90) 
    cv2.imwrite("{0}/{1}_{2}_{3}".format(os.path.join(round1_path, subdirs[0]),imtName, 'r90', imt_label), Rotated_imt)
    #rotate the original images 180 degrees
    Rotated_imt = imutils.rotate(imt, angle=180) 
    cv2.imwrite("{0}/{1}_{2}_{3}".format(os.path.join(round1_path, subdirs[0]),imtName, 'r180', imt_label), Rotated_imt)
    #rotate the original images 270 degrees
    Rotated_imt = imutils.rotate(imt, angle=270) 
    cv2.imwrite("{0}/{1}_{2}_{3}".format(os.path.join(round1_path, subdirs[0]),imtName, 'r270', imt_label), Rotated_imt)
    
for imv in val_dir:
    #start with validation images
    imv_label = imv.split('_')[-1] #0.png or 1.png
    shutil.copy2(imv,os.path.join(round1_path, subdirs[1]))
    #get validation image name
    imvName = imv.split('/')[11].replace('_'+imv_label,'')#.replace(imt_label,'vflip_'+imt_label)
    imv = cv2.imread(imv)
    #flip vertically
    flip_imv= cv2.flip(imv, 0)
    cv2.imwrite("{0}/{1}_{2}_{3}".format(os.path.join(round1_path, subdirs[1]),imvName, 'vflip', imv_label), flip_imv)
    #rotate the original images 90 degrees
    Rotated_imv = imutils.rotate(imv, angle=90) 
    cv2.imwrite("{0}/{1}_{2}_{3}".format(os.path.join(round1_path, subdirs[1]),imvName, 'r90', imv_label), Rotated_imv)
    #rotate the original images 180 degrees
    Rotated_imv = imutils.rotate(imv, angle=180) 
    cv2.imwrite("{0}/{1}_{2}_{3}".format(os.path.join(round1_path, subdirs[1]),imvName, 'r180', imv_label), Rotated_imv)
    #rotate the original images 270 degrees
    Rotated_imv = imutils.rotate(imv, angle=270) 
    cv2.imwrite("{0}/{1}_{2}_{3}".format(os.path.join(round1_path, subdirs[1]),imvName, 'r270', imv_label), Rotated_imv)
    


 #Do a vertical flip on the rotated images

aug_train_dir = glob.glob(os.path.join(round1_path, subdirs[0] + '/*'))
aug_val_dir =  glob.glob(os.path.join(round1_path, subdirs[1] + '/*'))

for imt in aug_train_dir: 
    imt_label = imt.split('_')[-1] #0.png or 1.png
    #get train image name
    imtName = imt.split('/')[11].replace('_'+imt_label,'')#.replace(imt_label,'vflip_'+imt_label)
    #flip the rotated images vertically
    if '_r90' in imtName or '_r180' in imtName or '_r270' in imtName:
        imt = cv2.imread(imt)
        flip_imt= cv2.flip(imt, 0)
        cv2.imwrite("{0}/{1}_{2}_{3}".format(os.path.join(round1_path, subdirs[0]),imtName, 'vflip', imt_label), flip_imt)

#start with validation images
for imv in aug_val_dir:
    imv_label = imv.split('_')[-1] #0.png or 1.png
    imvName = imv.split('/')[11].replace('_'+imv_label,'')#.replace(imt_label,'vflip_'+imt_label)
    #flip the rotated images vertically
    if '_r90' in imvName or '_r180' in imvName or '_r270' in imvName:
        imv = cv2.imread(imv)
        flip_imv= cv2.flip(imv, 0)
        cv2.imwrite("{0}/{1}_{2}_{3}".format(os.path.join(round1_path, subdirs[1]),imvName, 'vflip', imv_label), flip_imv)
   
    
    

