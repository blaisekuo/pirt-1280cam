# pirt-1280cam
Code for working with Princeton Infrared Technologies 1280cam

The camera uses WINIRC software to take frame grabs.

We use WINIRC version 4.5

WINIRC provides sample C and Matlab code to decode the header and pixel intensities stored in a raw file.

Code here decodes the raw file and store them in fits as a numpy array, the image array is decoded first, since I needed the data for SPIE. The headers are about half done and are not stored in the fits file yet.

Andy Monson has done the same thing in C at Penn State and he has done the headers as well.


The general format of the raw files is a 512 byte header, then an integer value corresponding to the A/D count produced by the 14-bit ADC for each pixel stored in 2 bytes for all 1.3 Megapixels (1024x1280). The two bytes are little edian, so will need to swap most significant and least significant bits.






