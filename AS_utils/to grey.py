import os
from PIL import Image

ROOT = '/home/weaver/PycharmProjects/datasets/gradSet/full/testImgAndGT/GT'


def toGrey(working):
    OUT_DIR = os.path.join(working, 'greyProc')
    if not os.path.exists(OUT_DIR):
        os.makedirs(OUT_DIR)

    
    right = 0
    wrong = 0

    print("Working on ", working, ", output to ", OUT_DIR)

    for filename in os.listdir(working):
        if filename.endswith(".png"):
            img = Image.open(os.path.join(working, filename)).convert('L')
            img.save(os.path.join(OUT_DIR, filename))
            right += 1
        else:
            wrong += 1
    
    print('Processed: ', right, '    Not Processed: ', wrong)
           

working = os.path.join(ROOT, 'train')
toGrey(working)

#WORKING = os.path.join(ROOT, 'val')
#toGrey(WORKING)