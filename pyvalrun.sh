#!/bin/bash
# file name: pyvalrun.sh
source /vol/teaching/drivability/anaconda3/bin/activate
conda init
conda activate proj

sleep 7

cd /vol/teaching/drivability/PycharmProjects/pytorch-semseg

python validate.py --config configs/frrnB_cityscapes.yml --model_path runs/frrnB_cityscapes/21981_14th/frrnB_cityscapes_best_.pkl

#python test.py --model_path best.6669/frrnB_cityscapes_best_model.pkl --img_path test/t1.png --out_path test/out1.png
