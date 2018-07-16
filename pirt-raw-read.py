# -*- coding: utf-8 -*-
"""
Created on Thu May 31 21:01:35 2018

@author: 45027374
"""

import matplotlib.pyplot as plt  
import numpy as np
import struct as st
#import pandas as pd  
#import os

    
#wind path
#datastore_path="c:/users/45027374/cloudstor/datastore/SPIE2018/"


#mac path
datastore_path="/Users/wapr/PhD/datastore/SPIE2018/"

run_dir="Run4-20180531-photon-noise-neg40c/raw/"


def open_file(file):
    
        
    with open(datastore_path + run_dir + file, "rb") as binary_file:
        # Read the whole file at once
        data = binary_file.read()
        
    return data


def read_header(data):

    header={
    'ByteSwap':int.from_bytes([data[0],data[1]],byteorder='little',signed='true'),
    'Xsize':int.from_bytes([data[2],data[3]],byteorder='little'),
    'Ysize':int.from_bytes([data[4],data[5]],byteorder='little'),
    'BytesPerPixel':int.from_bytes([data[6],data[7]],byteorder='little'),
    'RowColOrder':int.from_bytes([data[8],data[9]],byteorder='little'),
    'Yorigin':int.from_bytes([data[10],data[11]],byteorder='little'),
    'Year':int.from_bytes([data[12],data[13]],byteorder='little'),
    'Month':int.from_bytes([data[14],data[15]],byteorder='little'),
    'Day':int.from_bytes([data[16],data[17]],byteorder='little'),
    'Hour':int.from_bytes([data[18],data[19]],byteorder='little'),
    'Minute':int.from_bytes([data[20],data[21]],byteorder='little'),
    'Second':int.from_bytes([data[22],data[23]],byteorder='little'),
    'IntensityCold':int.from_bytes([data[24],data[25]],byteorder='little',signed='true'), 
    'TemperatureCold': '%.1f' % st.unpack('<f',bytearray([data[26],data[27],data[28],data[29]])),
    'IntensityHot':int.from_bytes([data[30],data[31]],byteorder='little',signed='true'),     
    'TemperatureHot': '%.1f' % st.unpack('<f',bytearray([data[32],data[33],data[34],data[35]])),
    'TargetGain': '%.1f' % st.unpack('<f',bytearray([data[36],data[37],data[38],data[39]])),
    'Revision':int.from_bytes([data[40],data[41]],byteorder='little'),
    'NumFrames':int.from_bytes([data[42],data[43]],byteorder='little'),
    'UL_Row':int.from_bytes([data[46],data[47]],byteorder='little'),
    'UL_Col':int.from_bytes([data[48],data[49]],byteorder='little'),
    'LR_Row':int.from_bytes([data[50],data[51]],byteorder='little'),
    'LR_Col':int.from_bytes([data[52],data[53]],byteorder='little'),
    'NumFramesSummed':int.from_bytes([data[54],data[55]],byteorder='little'),
    'FrameRate': '%.1f' % st.unpack('<f',bytearray([data[56],data[57],data[58],data[59]])),
    'IntegrationTime': '%.3f' % st.unpack('<f',bytearray([data[60],data[61],data[62],data[63]])),
    'BufBrdNumFrames':int.from_bytes([data[54],data[55]],byteorder='little'),
    }
    
    print(header)
    

def read_pixels(data):
    
    i = []
        
    
    x = 512
    while x < len(data):
        i.append(int.from_bytes([data[x],data[x+1]],byteorder='little'))
        x+=2
    
    inp=np.array(i)
    i2d=np.reshape(inp,(-1,1280))
    
    plt.imshow(i2d,cmap='gray',origin='lower')
    #plt.savefig(datastore_path + run_dir + file + ".png", bbox_inches="tight")
    
    


filein = "1ms0000.img"

datain=open_file(filein)

read_header(datain)
#read_pixels(datain)