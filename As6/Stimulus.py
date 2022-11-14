#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 19:52:28 2022

@author: lucian
"""
#import modules
import numpy as np
from psychopy import visual, core, visual, event
import os
import random
from psychopy import monitors


#Q1.
count = 0
for number in range(10):
    count +=1
    if number < 10:
        dpy = visual.ImageStim(win,image='/Users/lucian/downloads/PSYCH403_Exp/images/face%0i.jpg'%count, 
                          units='pix',pos=(0,0),size=(400,400))
    else:
        dpy = visual.ImageStim(win,image='/Users/lucian/downloads/PSYCH403_Exp/images/face%i.jpg' %count, 
                          units='cm',pos=(0,0),size=(400,400))

#Q2
count = 0
for number in range(10):
    count +=1
    if number%4 == 1:
        if count == 10:
            dpy = visual.ImageStim(win,image='/Users/lucian/downloads/PSYCH403_Exp/images/face%i.jpg' %count, 
                             units='pix',pos=(0.5,0.5),size=(400,400))
        else:
            dpy = visual.ImageStim(win,image='/Users/lucian/downloads/PSYCH403_Exp/images/face%0i.jpg'%count, 
                         units='pix',pos=(0.5,0.5),size=(400,400))
    if number%4 == 2:
        dpy = visual.ImageStim(win,image='/Users/lucian/downloads/PSYCH403_Exp/images/face%0i.jpg' %count, 
                         units='pix',pos=(-0.5,0.5),size=(400, 00))
    if number%4 == 3:
        dpy = visual.ImageStim(win,image='/Users/lucian/downloads/PSYCH403_Exp/images/face%0i.jpg' %count, 
                         units='pix',pos=(-0.5,-0.5),size=(400,400))
    else:
        dpy = visual.ImageStim(win,image='/Users/lucian/downloads/PSYCH403_Exp/images/face%0i.jpg' %count, 
                         units='pix',pos=(0.5,-0.5),size=(400,400))

#Q3
fix_text = visual.TextStim(win, text='+')
fix_text.draw()


#Q4
#CREATION OF WINDOW AND STIMULI
#-define experiment start text unsing psychopy functions
start_Msg = 'Welcome to the experiment'
#-define block (start)/end text using psychopy functions
start_block_Msg = visual.TextStim(win, text='Start of Block')
end_block_Msg = visual.TextStim(win, text = 'End of Block')
#-define stimuli using psychopy  (images, fixation cross)
count = 0
for number in range(10):
    count +=1
    if number < 10:
        dpy = visual.ImageStim(win,image='/Users/lucian/downloads/PSYCH403_Exp/images/face%0i.jpg'%count, 
                          units='pix',pos=(0,0),size=(400,400))
    else:
        dpy = visual.ImageStim(win,image='/Users/lucian/downloads/PSYCH403_Exp/images/face%i.jpg' %count, 
                          units='cm',pos=(0,0),size=(400,400))
fix_text = visual.TextStim(win, text = '+')



#START EXPERIMENT
#=====================
#-present start message text
start_Exp = visual.TextStim(win, text=start_Msg)
start_Exp.draw()
win.flip()
#-allow participant to begin experiment with button press
event.waitKeys()
#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
count = 0
for block in nBlocks:
    #-present block start message
    start_block_Msg.draw()
    win.flip()
    event.waitKeys()
    #-randomize order of trials here *
    np.random.shuffle(pics)
    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for trial in nTrials:
        #-set stimuli and stimulus properties for the current trial
        count +=1
        if number < 10:
            dpy = visual.ImageStim(win,image='/Users/lucian/downloads/PSYCH403_Exp/images/face%0i.jpg'%count, 
                              units='pix',pos=(0,0),size=(400,400))
        else:
            dpy = visual.ImageStim(win,image='/Users/lucian/downloads/PSYCH403_Exp/images/face%i.jpg'%count, 
                              units='pix',pos=(0,0),size=(400,400))
            
            dpy = visual.ImageStim(win,image='/Users/lucian/downloads/PSYCH403_Exp/images/face%i.jpg' %count, 
                              units='cm',pos=(0,0),size=(400,400))
        #-empty keypresses
        
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
        dpy.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(1)
        
        #draw end trial text
        end_trial_Msg = visual.TextStim(win, text = 'End of trial')
        end_trial_Msg.draw()
        #flip window
        win.flip()
        #wait time
        core.wait(1)
        
     #-draw end block text
     end_block_Msg.draw()
     #-flip window
     win.flip()
     #-wait time (stimulus duration)
     core.wait(1)
        
     #-collect subject response for that trial
     #-collect subject response time for that trial
     #-collect accuracy for that trial
        
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
win.close()
#-quit experiment
        
#CREATION OF WINDOW AND STIMULI