# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 21:41:05 2018

@author: 71097803
"""

import imageio
import glob
import os

#######Inputs######
image_path = 'C:\\Top\\Secret\\Folder\\Dont\\Tell\\Anyone'
file_type='.png'
output_file_name='test1.gif'
####################

##Covnert string to raw
def str_to_raw(s):
    raw_map = {8:r'\b', 7:r'\a', 12:r'\f', 10:r'\n', 13:r'\r', 9:r'\t', 11:r'\v'}
    return r''.join(i if ord(i) > 32 else raw_map.get(ord(i), i) for i in s)

#file name and path joining
image_path_raw=str_to_raw(image_path)
image_path_raw=image_path_raw+'\\*'+file_type
output_file_name=image_path+ '\\' + output_file_name


files = glob.glob(image_path_raw)
files.sort(key=lambda x: os.path.getmtime(x))
images = []
times=[]
for file in files:
    time_pre=file.split('image_')
    time_s=time_pre[1].split(file_type)
    time=float(time_s[0])
    times.append(time)
sorted_files=[x for _,x in sorted(zip(times,files))]
for file in sorted_files:
    images.append(imageio.imread(file))
imageio.mimsave(output_file_name, images, duration=.2)