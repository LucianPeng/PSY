#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 20:07:25 2022

@author: lucian
"""
from psychopy import gui
from datetime import datetime

exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 
            'gender':(), 'session':1}
#-create a dialogue box that will collect current participant number, age, gender, handedness

my_dlg = gui.DlgFromDict(dictionary=exp_info,title = ('Subject Info'),
                         order=('session', 'subject_nr', 'age', 'gender', 'handedness'),
                         fixed=('session'),tip=None, screen=-1, sortKeys = True,
                         copyDict=False, labels=None, show=False)
                         

print('All variables have been created! Now ready to show the dialog box!')

my_dlg = gui.DlgFromDict(dictionary=exp_info,title = ('Subject Info'),
                         order=('session', 'subject_nr', 'age', 'gender', 'handedness'),
                         fixed=('session'),tip=None, screen=-1, sortKeys = True,
                         copyDict=False, labels=None, show=True)
#get date and time
date = datetime.now()
exp_info['date'] = str(date.day) + '-' + str(date.month) + '-' + str(date.year)
#-create a unique filename for the data
filename = str(exp_info['subject_nr']) + '_' + exp_info['date'] + '.csv'
print(filename)