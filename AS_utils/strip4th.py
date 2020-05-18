import cv2
import os

#place aplha images in /alph
#writes noAlph to root (saves swapping)

ROOT = '/vol/research/chewing/shProject/gradSet/finalGrad/leftImg8bit/val/'
WORKING = os.path.join(ROOT, 'alph')

#if not os.path.exists(OUT_DIR):
#   os.makedirs(OUT_DIR)

good = 0
bad = 0

for filename in os.listdir(WORKING):
    img = cv2.imread(os.path.join(WORKING, filename), cv2.IMREAD_UNCHANGED)

    try:
        if len(img.shape) > 2 and img.shape[2] == 4:
            print(filename)
            # convert the image from RGBA2RGB
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            cv2.imwrite(os.path.join(ROOT, filename), img)      
            good +=1

    except AttributeError as aError:
        print('ERROR: ', aError, filename)
        bad += 1


print('Good: ', good, '  Bad: ', bad)
print('End')
