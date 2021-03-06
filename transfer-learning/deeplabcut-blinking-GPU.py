# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 15:40:32 2019

@author: gtsror
"""

# DLC Set up on blinking

import deeplabcut
import matplotlib
import tensorflow as tf

task='eyes_only' # Enter the name of your experiment Task
sides='lr-gpu' # Enter the name of the experimenter

training_videos = ['dlc-blinking/blinking-lr-2019-02-06/videos/2018_03_08_animal_1_video_1b.mp4',
                   'dlc-blinking/blinking-lr-2019-02-06/videos/2018_03_09_animal_3_video_2.mp4',
                   'dlc-blinking/blinking-lr-2019-02-06/videos/2019_01_07_animal_2.mp4',
                   'dlc-blinking/blinking-lr-2019-02-06/videos/2019_01_07_animal_3.mp4',
                   'dlc-blinking/blinking-lr-2019-02-06/videos/2019_01_07_animal_5.mp4'
                   ]

# video=['videos/animal_3_video_2_150fps_correct.mp4', 'videos/march_8_animal_1_video_150fps_correct.mp4'] # Enter the paths of your videos you want to grab frames from.

deeplabcut.create_new_project(task,sides,training_videos, working_directory='dlc-blinking',copy_videos=True) #change the working directory to where you want the folders created.

%matplotlib inline
path_config_file = '/dlc-blinking/an3_vid2_full/eyes_only-Guy-gpu-2019-01-29/config.yaml' # Enter the path of the config file that was just created from the above step (check the folder)
path_config_file = '/dlc-blinking/blinking-lr-2019-02-07/config.yaml' # Enter the path of the config file that was just created from the above step (check the folder)

deeplabcut.extract_frames(path_config_file,'automatic','uniform'),crop=True, checkcropping=True) #there are other ways to grab frames, such as by clustering 'kmeans'; please see the paper. 

# changed the cropping dimensions in the config.yaml file
%gui wx
deeplabcut.label_frames(path_config_file)

# Lables have now been created

deeplabcut.check_labels(path_config_file) #this creates a subdirectory with the frames + your labels
# Reviewed the labels, the seem to be ok

# Downloading the ResNets dataset:
deeplabcut.create_training_dataset(path_config_file)

# Training the dataset
deeplabcut.train_network(path_config_file)

# Evaluating the results
deeplabcut.evaluate_network(path_config_file)

# Analyzing video
videofile_path = ['crush_videos_from_zip/2019_02_07/animal_6/2019_02_07_animal_6_downs.mp4']
videofile_path = ['crush_videos_from_zip/2019_02_07/animal_4/2019_02_07_animal_4.mp4']


deeplabcut.analyze_videos(path_config_file,videofile_path,save_as_csv=True)

deeplabcut.create_labeled_video(path_config_file, ['D:\\crush_videos_from_zip\\2019_02_07\\\\animal_6\\2019_02_07_animal_6_downs.mp4'], save_frames=True)

%matplotlib notebook #for making interactive plots.
deeplabcut.plot_trajectories(path_config_file,videofile_path)


# TICTOCS:
# training - up to 72/96 hours
# analyzing - 45 minutes and 1.5 hours
# labeling - 25 minutes and 50 minutes