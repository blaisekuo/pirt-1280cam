# -*- coding: utf-8 -*-
"""
Created on Thu May 31 21:01:35 2018

@author: 45027374
"""

import matplotlib.pyplot as plt  
import numpy as np
#import pandas as pd  
#import os

datastore_path="c:/users/45027374/cloudstor/datastore/SPIE2018/"

    
run_dir="Run4-20180531-photon-noise-neg40c/raw/"

file = "1ms0000.img"

i = []

with open(datastore_path + run_dir + file, "rb") as binary_file:
    # Read the whole file at once
    data = binary_file.read()
    
    

x = 512
while x < len(data):
    i.append(int.from_bytes([data[x],data[x+1]],byteorder='little'))
    x+=2

inp=np.array(i)
i2d=np.reshape(inp,(-1,1280))

plt.imshow(i2d,cmap='gray',origin='lower')
plt.savefig(datastore_path + run_dir + file + ".png", bbox_inches="tight")