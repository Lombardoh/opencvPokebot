import cv2 as cv
import numpy as np
import os
from numpy.lib.type_check import imag
from time import time
from windowcapture import WindowCapture

#set dir for images as base dir
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#set windowcapture instance
wincap = WindowCapture('VisualBoyAdvance')

loop_time = time()
while(True):

    screenshot = wincap.get_screenshot()
    
    cv.imshow('Computer vision', screenshot)

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print("done")
