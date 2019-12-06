
import random
import os
import subprocess
import sys
import argparse

def split_data_set(image_dir):

    f_val = open("demo2_test.txt", 'w+')
    f_train = open("demo2_train.txt", 'w+')
    
    path, dirs, files = next(os.walk(image_dir))
    data_size = len(files)

    ind = 0
    data_test_size = int(0.1 * data_size)
    test_array = random.sample(range(data_size), k=data_test_size)
    
    for f in os.listdir(image_dir):
        if(f.split(".")[1] == "jpg"):
            ind += 1
            
            if ind in test_array:
                f_val.write(image_dir+'/'+f+'\n')
            else:
                f_train.write(image_dir+'/'+f+'\n')

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--folder", required=True)
args = vars(ap.parse_args(["-fJPEG_PRISE4/"]))

split_data_set(args["folder"])


