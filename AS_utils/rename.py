import os

WORKING = '/vol/research/chewing/shProject/gradSet/SANDedGrad/leftImg8bit/test'
os.chdir(WORKING)
for filename in os.listdir(WORKING):
    os.rename(filename, filename.replace('__', '_'))