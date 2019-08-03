import os
import sys
import glob
import matplotlib.pyplot as plt

import cv2
import dlib

options = dlib.simple_object_detector_training_options()
options.be_verbose = True
options.C = 5
dlib.train_simple_object_detector("gripRobotArm_label.xml", 
                                  "gripRobotArm_svm.svm", 
                                  options)
