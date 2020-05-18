#!/bin/bash
# file name: gradTrain.sh
source /vol/teaching/drivability/anaconda3/bin/activate
conda init
conda activate proj
sleep 2

cd /vol/teaching/drivability/PycharmProjects/pytorch-grad-semseg

#run training with config
python train.py --config configs/frrnB_cityscapes.yml
