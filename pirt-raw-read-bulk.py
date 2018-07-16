# -*- coding: utf-8 -*-
"""
Created on Thu May 31 21:01:35 2018

@author: 45027374
"""
  
import numpy as np
import struct as st
from astropy.io import fits 
#import pandas as pd  
import os

    
#wind path
datastore_path="c:/cloudstor/datastore/SPIE2018/"


#mac path
#datastore_path="/Users/wapr/PhD/datastore/SPIE2018/"


#run_dir="Run4-20180531-photon-noise-neg40c/"
#run_dir="Run5-20180602-neg40c/"
#run_dir="Run6-20180602-neg20c/"
run_dir="Run8-20180713-neg60c/"

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
    'UL_Row':int.from_bytes([data[44],data[45]],byteorder='little'),
    'UL_Col':int.from_bytes([data[46],data[47]],byteorder='little'),
    'LR_Row':int.from_bytes([data[48],data[49]],byteorder='little'),
    'LR_Col':int.from_bytes([data[50],data[51]],byteorder='little'),
    'NumFramesSummed':int.from_bytes([data[56],data[57]],byteorder='little'),
    'FrameRate': '%.1f' % st.unpack('<f',bytearray([data[56],data[57],data[58],data[59]])),
    'IntegrationTime': '%.3f' % st.unpack('<f',bytearray([data[60],data[61],data[62],data[63]])),
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

    
    return i2d
    
#    plt.imshow(i2d,cmap='gray',origin='lower')
#    plt.savefig(datastore_path + run_dir + file + ".png", bbox_inches="tight")
    
    

#filebase = "1ms0000.img"

imgar = []

if "20c" in run_dir:
    hdubias = fits.open(datastore_path + '20c-bias.fits')
    print("using 20c bias file")
elif "60c" in run_dir:
    hdubias = fits.open(datastore_path + '60c-bias.fits')
    print("using 60c bias file")
else:
    hdubias = fits.open(datastore_path + 'bias.fits')
    print("using 40c bias file")

biasin = hdubias[0].data

print(biasin.shape)

vec = np.full((1024,1280),16384)


x=0
 
#for x in range (0,20):
 #   datain=open_file('raw/1ms00' + '%02d' % (x,) + '.img')
  #  #read_header(datain)
   # oneimgar=read_pixels(datain)

#files = []
for onefile in  os.listdir(datastore_path + run_dir + 'raw/'):
    if onefile.endswith("img"):
    #files.append(onefile)
    
        print(onefile)

#for x in range (0,20):
        datain=open_file('raw/' + onefile)
        #read_header(datain)
        oneimgar=read_pixels(datain)
    
    
        offsetimgar = oneimgar + vec
    
        biasoneimgar = offsetimgar - biasin
        
        
        hdu = fits.PrimaryHDU(biasoneimgar)
        hdulist = fits.HDUList([hdu])
        hdulist.writeto(datastore_path + run_dir + 'fits/' + onefile + '-subbias.fits')
        hdulist.close()
    
        hdu = fits.PrimaryHDU(offsetimgar)
        hdulist = fits.HDUList([hdu])
        hdulist.writeto(datastore_path + run_dir + 'fits/' + onefile + '-plus2sup14.fits')
        hdulist.close()

        hdu = fits.PrimaryHDU(oneimgar)
        hdulist = fits.HDUList([hdu])
        hdulist.writeto(datastore_path + run_dir + 'fits/' + onefile + '.fits')
        hdulist.close()

# calculate bias
    
 #   imgar.append(oneimgar)

#imgar= np.asarray(imgar)

#bias=np.mean(imgar,axis=0)

#print(bias.astype(int))

#print(bias.shape)

#hdu = fits.PrimaryHDU(bias.astype(int))
#hdulist = fits.HDUList([hdu])
#hdulist.writeto(datastore_path + run_dir + 'bias' + '.fits')
#hdulist.close()


####

#plt.imshow(bias,cmap='gray',origin='lower')    