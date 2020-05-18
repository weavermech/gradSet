
import os
from os.path import join

ROOT = '/vol/research/chewing/shProject/gradSet/finalGrad/gtFine'

def splitValSet(dSet):
    WORK = join(ROOT, dSet)
    V_OUT_DIR = join(ROOT, 'val')
    i = 0

    if not os.path.exists(V_OUT_DIR):
        os.makedirs(V_OUT_DIR)

     
    os.chdir(WORK)
    for filename in sorted(os.listdir(WORK)):
        if filename.endswith("_gtFine_labelIds.png"):
            if i % 7 == 0:
                os.rename(filename, join(V_OUT_DIR, filename) )
                
            i += 1
            print(i)

splitValSet('train')

# ROOT = '/vol/research/chewing/shProject/gradSet/finalGrad/leftImg8bit/'
# REFERENCE = '/vol/research/chewing/shProject/gradSet/finalGrad/gtFine/train/'
# DEST_DIR = '/vol/research/chewing/shProject/gradSet/finalGrad/leftImg8bit/train/'
# SOURCE_DIR = '/vol/research/chewing/shProject/gradSet/finalGrad/leftImg8bit/val/'

    
# sourceStr = 'd'

# s = 0   #skipped
# i = 0   #copied

# for filename in sorted(os.listdir(REFERENCE)):
#     if filename.endswith("_gtFine.png"):
#         sourceStr = filename[:-11] + '.png'
#         if os.path.exists(join(DEST_DIR,sourceStr)):
#             i += 1
#         else:
#             s +=1
    
#         # try:
#         #     os.rename(join(SOURCE_DIR,sourceStr ), join(DEST_DIR, sourceStr) )
#         #     i += 1
#         # except OSError as error:
#         #     print (error)
#         #     s += 1
        
        
# print(i, '   ',s)

