# GradSemSeg

Training a network on gradient-coloured dataset

## Description

A system for taking images raw captured from Unreal via Airsim, processing them into a dataset and training a neural network.

## Getting Started

Place a trained model in the runs/architecture folder, update the config file, and run test a sample image 

### Requirements

* pytorch >=0.4.0
* torchvision ==0.2.0
* scipy ==1.1.0
* tqdm
* tensorboardX



### Executing program


**To validate the model :**

```
usage: validate.py [-h] [--config [CONFIG]] [--model_path [MODEL_PATH]]
                       [--eval_flip] [--measure_time]

  --config              Config file to be used
  --model_path          Path to the saved model
  --eval_flip           Enable evaluation with flipped image | True by default
  --measure_time        Enable evaluation with time (fps) measurement | True
                        by default
```

**To test the model w.r.t. a dataset on custom images(s):**

```
python test.py [-h] [--model_path [MODEL_PATH]] [--dataset [DATASET]]
               [--dcrf [DCRF]] [--img_path [IMG_PATH]] [--out_path [OUT_PATH]]
 
  --model_path          Path to the saved model
  --dataset             Dataset to use ['pascal, camvid, ade20k etc']
  --dcrf                Enable DenseCRF based post-processing
  --img_path            Path of the input image
  --out_path            Path of the output segmap
```



## Authors

Stephen Hanson
stephenhansonj@gmail.com


## Acknowledgments

Inspiration, code snippets, etc.
* [MeetShah for training code base](https://https://github.com/meetshah1995/pytorch-semseg)

