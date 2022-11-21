#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 20:08:57 2022

@author: lucian
"""

from psychopy import visual, core, visual, event
import os
import random
from psychopy import monitors

os.chdir('/Users/Lucian/Downloads/PSYCH403_Exp')
#-define the directory where you will save your data
main_dir = os.getcwd()
#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir, 'images')
data_dir = os.path.join(main_dir, 'data')

#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width = 35.36, distance = 60)
mon.setSizePix([1600, 900])

#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor = mon)
win = visual.Window(monitor = mon, size = (800, 800), color = [-1, -1, -1], units = None, fullscr = False)

my_image = visual.ImageStim(win, image = '/Users/lucian/Downloads/PSYCH403_Exp/images/face01.jpg')
nTrials = 3
fix_text = visual.TextStim(win, text = '+')
endtrial_Msg = visual.TextStim(win, text = 'End of Trial')
#=====================
#START TRIAL
#===================== 
#-draw fixation
fix_text.draw()
#-flip window
win.flip()
#-wait time (stimulus duration)
core.wait(1)
#-draw image

my_image.draw()
#-flip window
win.flip()
#-wait time (stimulus duration)
core.wait(1)
#draw end trial text
endtrial_Msg.draw()
#-flip window
win.flip()
#-wait time (stimulus duration)
core.wait(1)

























