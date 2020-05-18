import cv2
import numpy as np
import os

ROOT = '/vol/research/chewing/shProject/gradSet/camvid'
WORKING = os.path.join(ROOT, 'testImgAndGT', 'GT')
OUT_DIR = os.path.join(ROOT, 'gtFine', 'train')
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
        if (height == 512) & (width == 1024):
            right += 1

            for row in range(height):
                for column in range(width):
                    bval = img[row, column, 0]
                    gval = img[row, column, 1]
                    rval = img[row, column, 2]

                    # blue
                    if (bval == 255) & (gval == 0) & (rval == 0):
                        img.itemset((row, column, 0), 6)
                        img.itemset((row, column, 1), 6)
                        img.itemset((row, column, 2), 6)
                    # green
                    elif (bval == 0) & (gval == 255) & (rval == 0):
                        img.itemset((row, column, 0), 7)
                        img.itemset((row, column, 1), 7)
                        img.itemset((row, column, 2), 7)
                    # red
                    elif (bval == 0) & (gval == 0) & (rval == 255):
                        img.itemset((row, column, 0), 10)
                        img.itemset((row, column, 1), 10)
                        img.itemset((row, column, 2), 10)
                    # yellow
                    elif (bval == 0) & (gval == 255) & (rval == 255):
                        img.itemset((row, column, 0), 11)
                        img.itemset((row, column, 1), 11)
                        img.itemset((row, column, 2), 11)
                    # magenta
                    elif (bval == 255) & (gval == 0) & (rval == 255):
                        img.itemset((row, column, 0), 12)
                        img.itemset((row, column, 1), 12)
                        img.itemset((row, column, 2), 12)
                    # teal
                    elif (bval == 255) & (gval == 255) & (rval == 0):
                        img.itemset((row, column, 0), 16)
                        img.itemset((row, column, 1), 16)
                        img.itemset((row, column, 2), 16)
                    # white
                    elif (bval == 255) & (gval == 255) & (rval == 255):
                        img.itemset((row, column, 0), 18)
                        img.itemset((row, column, 1), 18)
                        img.itemset((row, column, 2), 18)
                    # black
                    else:
                        img.itemset((row, column, 0), 19)
                        img.itemset((row, column, 1), 19)
                        img.itemset((row, column, 2), 19)
            img = Image.convert('L')
            cv2.imwrite(os.path.join(OUT_DIR, filename[:-4] + '_gtFine_labelIds.png'), img)
            os.rename(filename, filename.replace('gt_i', 'i'))
        else:
            wrong += 1

print(right, " images processed, ", wrong, " files not processed.")
