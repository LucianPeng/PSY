#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 12:48:12 2022

@author: lucian
"""

#----------------------------------------------------------------------------------------------
#Save csv Exercises
#----------------------------------------------------------------------------------------------
import csv 
import os

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
os.chdir('/Users/Lucian/Downloads/PSYCH403_Exp')
#-define the directory where you will save your data
main_dir = os.getcwd()
#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir, 'images')
data_dir = os.path.join(main_dir, 'data')


#2 create filename and directory
filename = 'savecsv_example.csv'
print(filename)

import os
main_dir = os.getcwd() #define the main directory where experiment info is stored
#point to a data directory to save the output
data_dir = os.path.join(main_dir,'data',filename)
print(data_dir)

#3: a list of lists of all the data you want to save
data_as_list = [prob, corr_resp, sub_resp, sub_acc, sub_RT]
#print(data_as_list)

#4: mode='w' means 'write mode'. "sub_data" is arbitrary, but stay consistent
with open(data_dir, mode='w') as sub_data:
    #delimiter=',' for lists of values separated by commas
    data_writer = csv.writer(sub_data, delimiter=',')
    data_writer.writerow(data_as_list) #write
    