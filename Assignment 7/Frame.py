#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 11:34:57 2022

@author: lucian
"""

#Frame-based timing

refresh = 1.0/60.0
#set durations
fix_dur = 1
image_dur = 2
text_dur = 1.5

#set frame counts
fix_frames = int(fix_dur/refresh)
image_frames = int(image_dur/refresh)
text_frames = int(text_dur/refresh)
total_frames = int(fix_frames + image_frames + text_frames)

os.chdir('/Users/Lucian/Downloads/PSYCH403_Exp')
#-define the directory where you will save your data
main_dir = os.getcwd()
#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir, 'images')
data_dir = os.path.join(main_dir, 'data')

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
press_timer = core.CountdownTimer()
nBlocks = 1
for block in range(nBlocks):
    block_timer.reset()
    #-present block start message
    start_block_Msg.draw()
    win.flip()
    event.waitKeys()
    #-randomize order of trials here *
    np.random.shuffle(stims)
    #-reset response time clock here
    block_timer.reset()
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for trial in range(nTrials):
        trial_timer.reset()
        #-set stimuli and stimulus properties for the current trial
        my_image.image = os.path.join(image_dir, stims[trial])
        my_image = visual.ImageStim(win, image = my_image.image)
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================   
        for frameN in range(total_frames):
            if 0 <= frameN <= fix_frames:
                fix_text.draw()
                win.flip()

            if fix_frames < frameN <= (fix_frames + image_frames):
                my_image.draw()
                win.flip()
            
            if (fix_frames + image_frames) < frameN < total_frames:
                endtrial_Msg.draw()
                win.flip()
        
        print('Overall, %i frames were dropped.' % win.nDroppedFrames)
        if win.nDroppedFrames > 20:
            press_timer.reset()
            press-timer.add(4.5)
            if press.timer > 3.5:
                fix_text.draw()
                win.flip()
            if 3.5 >= press.timer > 1.5:
                my_image.draw()
                win.flip()
            if 1.5 >= press.timer > 0:
                endtrial_Msg.draw()
                win.flip()

     #-wait time (stimulus duration)
    print('Block'+str(block)+' time =', block_timer.getTime())
     
win.close()