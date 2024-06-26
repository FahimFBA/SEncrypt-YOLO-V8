# Import
import resize.resize_train
from resize.resize_train import *

# GLOBAL VARIABLE
target_width = 640
target_height = 640


# Directory
train_raw_dir = '/home/fahim/Documents/Model_SEncrypt/raw_dataset/test/images'
train_resize_dir = '/home/fahim/Documents/Model_SEncrypt/resized_dataset/train'


# Resize the raw train dataset
resize_train(train_raw_dir, train_resize_dir, target_width, target_height)