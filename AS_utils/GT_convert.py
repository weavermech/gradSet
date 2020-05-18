import cv2
import numpy as np
import os

ROOT = '/vol/research/chewing/shProject/2020-04-21-14-45-13'
WORKING = os.path.join(ROOT, 'GT')
OUT_DIR = os.path.join(ROOT, 'GT_PROCESSED')
if not os.path.exists(OUT_DIR):
    os.makedirs(OUT_DIR)

right = 0
wrong = 0

print("Working on ", WORKING, ", output to ", OUT_DIR)

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

                    # if  ( (rVal & gVal) > 130 ) & ( (rVal & gVal) > bVal ):     #both green and red greater than 130 and both greater than blue
                    #    img.itemset((row,column,0),0)                               #threshhold to yellow
                    #    img.itemset((row,column,1),255)
                    #    img.itemset((row,column,2),255)

                    # if ( bVal > rVal) & (bVal > gVal) & (bVal > ) :
                    #    img.itemset((row,column,0),255)                             #threshhold to blue
                    #    img.itemset((row,column,1),0)
                    #    img.itemset((row,column,2),0)

                    # if r and b are > 50% and both > green #threshhold to pink
                    # elif (bVal > 190) & (gVal < 180) & (rVal > 190):
                    #    img.itemset((row,column,0),255)
                    #    img.itemset((row,column,1),0)
                    #    img.itemset((row,column,2),255)
                    #    #threshhold to red
                    # elif (bVal < 170) & (gVal < 175) & (rVal > 190):
                    #    img.itemset((row,column,0),0)
                    #    img.itemset((row,column,1),0)
                    #    img.itemset((row,column,2),255)
                    ##threshhold to green
                    # elif (bVal < 178) & (gVal > 200) & (rVal < 178):
                    #    img.itemset((row,column,0),0)
                    #    img.itemset((row,column,1),255)
                    #    img.itemset((row,column,2),0)
                    ##threshhold to blue
                    # elif (bVal > 200) & (gVal < 190) & (rVal < 190):
                    #    img.itemset((row,column,0),255)
                    #    img.itemset((row,column,1),0)
                    #    img.itemset((row,column,2),0)
                    # elif (bVal < 127) & (gVal < 127) & (rVal < 127):        # r,g, and b < 50%
                    #    img.itemset((row,column,0),0)
                    #    img.itemset((row,column,1),0)
                    #    img.itemset((row,column,2),0)

            cv2.imwrite(os.path.join(OUT_DIR, 'proc_' + filename), img)
        else:
            wrong += 1

print(right, " images processed, ", wrong, " files not processed.")
