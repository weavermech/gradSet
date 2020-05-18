import cv2
import numpy as np
import os
import timeit

ROOT = '/home/weaver/PycharmProjects/datasets/gradSet/finalGrad/'

OUT_DIR = os.path.join(ROOT, 'cyOut')

try:
    os.mkdir(OUT_DIR)
except OSError as error:
    print(error)

def gtThreshold(workDir):

    WORKING = os.path.join(ROOT, workDir)
    right = 0
    wrong = 0
    kernel = np.ones((3, 3), np.uint8)


    print("Working on ", WORKING, ", output to ", OUT_DIR)


    starttime = timeit.default_timer()
    for y in range(0,1):        
        for filename in os.listdir(WORKING):
            print(filename)
            if filename.endswith(".png"):
                img = cv2.imread(os.path.join(WORKING, filename))
                height, width, channels = img.shape                     # use try in case no shape?
                if (height == 512) & (width == 1024) & (channels == 3):
                    right += 1

                    # PROCESS - wider if elses for each colour, thresh each colour pix didn't work, dropper in GIMP

                    for row in range(height):
                        for column in range(width):
                            bval = img[row, column, 0]
                            gval = img[row, column, 1]
                            rval = img[row, column, 2]

                            # convert sky to white
                            if ((bval == 0) & (gval > 220) & (rval > 220)):
                                img.itemset((row, column, 0), 255)
                                img.itemset((row, column, 1), 255)
                                img.itemset((row, column, 2), 255)
                            # threshhold to yellow
                            if ((bval < 190) & (gval > 220) & (rval > 220)) | ((bval < 150) & (gval > 200) & (rval > 200)):
                                img.itemset((row, column, 0), 0)
                                img.itemset((row, column, 1), 255)
                                img.itemset((row, column, 2), 255)
                            # threshhold to pink
                            elif (bval > 190) & (gval < 180) & (rval > 190):
                                img.itemset((row, column, 0), 255)
                                img.itemset((row, column, 1), 0)
                                img.itemset((row, column, 2), 255)
                                # threshhold to red
                            elif (bval < 170) & (gval < 175) & (rval > 190):
                                img.itemset((row, column, 0), 0)
                                img.itemset((row, column, 1), 0)
                                img.itemset((row, column, 2), 255)
                            # threshhold to green
                            elif (bval < 178) & (gval > 200) & (rval < 178):
                                img.itemset((row, column, 0), 0)
                                img.itemset((row, column, 1), 255)
                                img.itemset((row, column, 2), 0)
                            # threshhold to blue
                            elif (bval > 190) & (gval < 180) & (rval < 180):
                                img.itemset((row, column, 0), 255)
                                img.itemset((row, column, 1), 0)
                                img.itemset((row, column, 2), 0)
                            elif (bval > 190) & (gval > 190) & (rval < 180):
                                img.itemset((row, column, 0), 255)
                                img.itemset((row, column, 1), 255)
                                img.itemset((row, column, 2), 0)
                            elif (bval < 50) & (gval < 50) & (rval < 50):
                                img.itemset((row, column, 0), 0)
                                img.itemset((row, column, 1), 0)
                                img.itemset((row, column, 2), 0)
                            else:
                                img.itemset((row, column, 0), 255)
                                img.itemset((row, column, 1), 255)
                                img.itemset((row, column, 2), 255)

                            
                    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
                    cv2.imwrite(os.path.join(OUT_DIR, 'proc_' + filename), img)
                else:
                    wrong += 1
    print("The time difference is :", timeit.default_timer() - starttime)

    print(right, " images processed, ", wrong, " files not processed.")