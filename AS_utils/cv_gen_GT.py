
# In settings.json first activate computer vision mode: 
# https://github.com/Microsoft/AirSim/blob/master/docs/image_apis.md#computer-vision-mode

import airsim
import setup_path 



import numpy as np
import PIL
import pandas as pd
import time
import os
import pprint
import tempfile
import math
from math import *


from abc import ABC, abstractmethod

#set directory paths
ROOT = os.path.join('D:\\','Users','weave','Documents','AirSim')
WORKING = os.path.join(ROOT,'2020-04-21-14-45-13')
OUT_DIR = os.path.join(WORKING,'GT')

try: 
    os.mkdir(OUT_DIR)
except OSError as error: 
    print(error) 

client = airsim.VehicleClient()
client.confirmConnection()

data = pd.read_csv(os.path.join(ROOT,WORKING,'airsim_rec.txt'), sep="\s+|;", usecols=[1,2,3,4,5,6,7,8])



for index, row in data.iterrows():

    client.simSetVehiclePose(airsim.Pose(airsim.Vector3r(row['POS_X'], row['POS_Y'], row['POS_Z']), airsim.Quaternionr(	row['Q_X'],	row['Q_Y'],	row['Q_Z'],row['Q_W'])), True)
    png_image = client.simGetImage("0", airsim.ImageType.Scene)

    
    #airsim.write_file(row['ImageFile'], png_image)
    airsim.write_file(os.path.join(OUT_DIR , 'gt_' + row['ImageFile']), png_image)

#client = airsim.VehicleClient()
#client.confirmConnection()
#pose = client.simGetVehiclePose()

#client.simSetVehiclePose(airsim.Pose(airsim.Vector3r(0, 0, 0), airsim.to_quaternion(0, 0, 0)), True)
#pose = client.simGetVehiclePose()
#print("x={}, y={}, z={}".format(pose.position.x_val, pose.position.y_val, pose.position.z_val))

#angles = airsim.to_eularian_angles(client.simGetVehiclePose().orientation)
#print("pitch={}, roll={}, yaw={}".format(angles[0], angles[1], angles[2]))

#angles = client.simGetVehiclePose().orientation
#print("A={}, B={}, C={}, D={}".format(angles.w_val, angles.x_val, angles.y_val, angles.z_val))

#time.sleep(3)


#client.simSetVehiclePose(airsim.Pose(airsim.Vector3r(-3.964199,	-9.594883,	-1.995352), airsim.Quaternionr(	-0.000000,	0.000000,	0.446206,0.894930)), True)
#pose = client.simGetVehiclePose()
#print("x={}, y={}, z={}".format(pose.position.x_val, pose.position.y_val, pose.position.z_val))

#angles = airsim.to_eularian_angles(client.simGetVehiclePose().orientation)
#print("pitch={}, roll={}, yaw={}".format(angles[0], angles[1], angles[2]))

#angles = client.simGetVehiclePose().orientation
#print("A={}, B={}, C={}, D={}".format(angles.w_val, angles.x_val, angles.y_val, angles.z_val))
#time.sleep(3)


#client.simSetVehiclePose(airsim.Pose(airsim.Vector3r(696.525940,	895.578247,	-8.553124), airsim.Quaternionr(0.894962,	-0.000000,	0.000000,	0.446143)), True)
#pose = client.simGetVehiclePose()
#print("x={}, y={}, z={}".format(pose.position.x_val, pose.position.y_val, pose.position.z_val))

#angles = airsim.to_eularian_angles(client.simGetVehiclePose().orientation)
#print("pitch={}, roll={}, yaw={}".format(angles[0], angles[1], angles[2]))

#angles = client.simGetVehiclePose().orientation
#print("A={}, B={}, C={}, D={}".format(angles.w_val, angles.x_val, angles.y_val, angles.z_val))
#time.sleep(3)


#client.simSetVehiclePose(airsim.Pose(airsim.Vector3r(641.415833,	717.130188,	44.242771),	airsim.Quaternionr(0.216400,	0.000000,	-0.000000,	-0.976305)), True)
#pose = client.simGetVehiclePose()
#print("x={}, y={}, z={}".format(pose.position.x_val, pose.position.y_val, pose.position.z_val))

#angles = airsim.to_eularian_angles(client.simGetVehiclePose().orientation)
#print("pitch={}, roll={}, yaw={}".format(angles[0], angles[1], angles[2]))

#angles = client.simGetVehiclePose().orientation
#print("A={}, B={}, C={}, D={}".format(angles.w_val, angles.x_val, angles.y_val, angles.z_val))
#time.sleep(3)


## currently reset() doesn't work in CV mode. Below is the workaround
#client.simSetVehiclePose(airsim.Pose(airsim.Vector3r(0, 0, -5), airsim.to_quaternion(0, 0, 0)), True)
#pose = client.simGetVehiclePose()
#print("x={}, y={}, z={}".format(pose.position.x_val, pose.position.y_val, pose.position.z_val))

#angles = airsim.to_eularian_angles(client.simGetVehiclePose().orientation)
#print("pitch={}, roll={}, yaw={}".format(angles[0], angles[1], angles[2]))

#angles = client.simGetVehiclePose().orientation
#print("A={}, B={}, C={}, D={}".format(angles.w_val, angles.x_val, angles.y_val, angles.z_val))












#################### OLD CODE
#    timer = 0
#    time_obs = 50
#    bObstacle = False

#    if (bObstacle):
#        timer = timer + 1
#        if timer > time_obs:
#            bObstacle = False
#            timer = 0
#    else:
#        yaw = target_angle

#    print (target_angle,target_vec,target_dist,x,y,goal[0],goal[1])


#    if (np.average(img2d_box) < coll_thres):
#        img2d_box_l = img2d_box = img2d[int((h-roi_h)/2):int((h+roi_h)/2),int((w-roi_w)/2)-50:int((w+roi_w)/2)-50]
#        img2d_box_r = img2d_box = img2d[int((h-roi_h)/2):int((h+roi_h)/2),int((w-roi_w)/2)+50:int((w+roi_w)/2)+50]
#        img2d_box_l_avg = np.average(np.multiply(img2d_box_l,w_mtx))
#        img2d_box_r_avg = np.average(np.multiply(img2d_box_r,w_mtx))
#        print('left: ', img2d_box_l_avg)
#        print('right: ', img2d_box_r_avg)
#        if img2d_box_l_avg > img2d_box_r_avg:
#            ##Go LEFT
#            #y_offset = y_offset-1
#            yaw = yaw - radians(10)
#            bObstacle = True
#        else:
#            ##Go RIGHT
#            #y_offset = y_offset+1
#            yaw = yaw + radians(10)
#            bObstacle = true
#        print('yaw: ', yaw)
