#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 11:23:12 2022

@author: lucian
"""

#Clock
wait_timer = core.Clock()
stims = ['face01.jpg', 'face02.jpg', 'face03.jpg']
    
for trial in range(nTrials):
    my_image.image = os.path.join(image_dir, stims[trial])
    my_image = visual.ImageStim(win, image = my_image.image)
    wait_timer.reset()
    my_image.draw()
    win.flip
    core.wait(2)
    wait_timer.getTime()
    print("Trial" + str(trial) + ' time =', wait_timer.getTime())
           

clock_wait_timer = core.Clock()
for trial in range(nTrials):
    my_image.image = os.path.join(image_dir, stims[trial])
    my_image = visual.ImageStim(win, image = my_image.image)
    clock_wait_timer.reset()
    while clock_wait_timer.getTime() <= 2:
        my_image.draw()
        win.flip()
    print("Trial" + str(trial) + ' time =', clock_wait_timer.getTime())
win.close()


countdown_timer = core.CountdownTimer()
for trial in range(nTrials):
    my_image.image = os.path.join(image_dir, stims[trial])
    my_image = visual.ImageStim(win, image = my_image.image)
    countdown_timer.reset()
    countdown_timer.add(2)
    while countdown_timer.getTime() > 0:
        my_image.draw()
        win.flip()
    print("Trial" + str(trial) + ' time =', countdown_timer.getTime())
win.close()







#CREATION OF WINDOW AND STIMULI
#-define experiment start text unsing psychopy functions
start_Msg = 'Welcome to the experiment'
#-define block (start)/end text using psychopy functions
start_block_Msg = visual.TextStim(win, text='Start of Block')
end_block_Msg = visual.TextStim(win, text = 'End of Block')
#-define stimuli using psychopy  (images, fixation cross)

my_image = visual.ImageStim(win)
stims = ['face01.jpg','face02.jpg','face03.jpg']
nTrials = 3
fix_text = visual.TextStim(win, text = '+')
endtrial_Msg = visual.TextStim(win, text = 'End of Trial')
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
block_timer = core.Clock()
trial_timer = core.Clock()
for block in nBlocks:
    block_timer.reset()
    #-present block start message
    start_block_Msg.draw()
    win.flip()
    event.waitKeys()
    #-randomize order of trials here *
    np.random.shuffle(pics)
    #-reset response time clock here
    block_timer.reset()
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for trial in nTrials:
        trial_timer.reset()
        #-set stimuli and stimulus properties for the current trial
        my_image.image = os.path.join(image_dir, stims[trial])
        my_image = visual.ImageStim(win, image = my_image.image)
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================   
        while trial_timer <= 1:
            #-draw fixation
            fix_text.draw()
            #-flip window
            win.flip()
        
        while 1 < trial_timer <= 2:
            my_image.draw()
            win.flip()
        
        while 2 < trial_timer <= 3:
            endtrial_Msg.draw()
            win.flip
        
        print('Trial'+str(trial)+' time =', trial_timer.getTime())
        
     #-draw end block text
     end_block_Msg.draw()
     #-flip window
     win.flip()
     #-wait time (stimulus duration)
     print('Block'+str(block)+' time =', block_timer.getTime())