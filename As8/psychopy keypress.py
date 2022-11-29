#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 18:57:12 2022

@author: lucian
"""
#----------------------------------------------------------------------------------------------
#PsychoPy Keypress Exercises
#----------------------------------------------------------------------------------------------
from psychopy import core, event, visual, monitors

mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

nTrials=10
my_text=visual.TextStim(win)
fix=visual.TextStim(win, text='+')
sub_resp = []

#1.------------------------

for trial in range(nTrials):
    keys = event.getKeys()
    my_text.text = 'trial %i' %trial
    
    fix.draw()
    win.flip()
    core.wait(2)
    
    event.clearEvents()
    
    my_text.draw()
    win.flip()
    core.wait(1)
    
    print('keys that were pressed', keys)
    
    if keys:
        sub_resp = keys[0]
    print('response that was counted', sub_resp)

win.close()

#2.------------------------
#a. the event.clearEvents is always within the trial loop. If for outside the trial loop, the responses within the trial loop will not be cleared
#b.it only takes the first response in the response for the last trial

nTrials = 3
for trial in range(nTrials):
    keys = event.getKeys()
    my_text.text = 'trial %i' %trial
    
    fix.draw()
    win.flip()
    core.wait(2)
    
    event.clearEvents()
    
    my_text.draw()
    win.flip()
    core.wait(1)
    
    print('keys that were pressed', keys)
    
if keys:
    sub_resp = keys[0]
    print('response that was counted', sub_resp)

win.close()




















