##########00 import modules##############################


import imutils
from imutils.video import VideoStream
from imutils.video import FPS

import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import time
import ffmpeg

from JM_show_image import show_image
from skimage import io










##########01 read in MIP .tif##############################

'''
    [1] set path to dir where your input .tif stack is located
            make sure path is delimited by '//' instead of escape keys
            make sure path does not terminate in '//'

    [2] set fileName to name of your input .tif stack, without file extension (e.g. 'temp6')
            fileName should not have any '.' characters in it
'''

#read in .tif stack as numpy.ndarray
path = 'C://Users//julia//OneDrive//documents//MSc_UToronto_thesis//project_SNCI_pipeline//data//2020-11_data_hong'
fileName = 'MIP_2021-03-26_worm1run3'
filePath = path + '//' + fileName + '.tif'
inputStack = io.imread(filePath)
frame01 = inputStack[0, :, :]











bp = None