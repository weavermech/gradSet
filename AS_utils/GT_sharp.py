import cv2
import numpy as np
import os


ROOT = '/vol/research/chewing/shProject/2020-04-21-14-45-13'
WORKING = os.path.join(ROOT, 'GT_PROCESSED')
OUT_DIR = os.path.join(ROOT, 'GT_PROCESSED_OPENED')
#if not os.path.exists(ROOT/'citySAND2/leftImg8bit'):
#    os.makedirs(ROOT/'citySAND2/leftImg8bit')
try: 
    os.mkdir(OUT_DIR)
except OSError as error: 
    print(error) 


right = 0
wrong = 0
kernel = np.ones((3, 3), np.uint8)


print("Working on ", WORKING, ", output to ", OUT_DIR)


for filename in os.listdir(WORKING):
    if filename.endswith(".png"):
        right += 1
        print(right)
        img = cv2.imread(os.path.join(WORKING, filename))
        
        opened_image = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

        cv2.imwrite(os.path.join(OUT_DIR, 'opened_'+filename), opened_image)
    else:
        wrong += 1

print(right, " images processed, ", wrong, " files not processed.")
