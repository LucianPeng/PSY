#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 13:05:50 2022

@author: lucian
"""

import pandas as pd


#1. ----------------------------------------
#load the imported data as a variable (df)
df = pd.read_json(data_dir+'_block1.txt')
print(df)

print(df.problem)

pd.DataFrame(df)


mean(sub_acc)


#2. ----------------------------------------

acc_trials = df.loc[df['sub_acc'] == 1] #show only trials on which subject was correct
print(acc_trials)


#3. ----------------------------------------
rp_trials = df.loc[df['sub_resp'] != None]
print(rp_trials)
