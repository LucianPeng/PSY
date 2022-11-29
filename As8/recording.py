#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 22:36:30 2022

@author: lucian
"""



#----------------------------------------------------------------------------------------------
#Recording data Exercises
#----------------------------------------------------------------------------------------------

#1. -------------------------------------------------------------
from psychopy import core, event, visual, monitors
import numpy as np
import json as json

#monitor specs
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

#blocks, trials, stims, and clocks
nBlocks=2
nTrials=4
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#prefill dictionary for responses

resp_1 = {'sub_resp':[], 'sub_acc':[], 'prob':[], 'corr_resp':[], 'sub_RT':[]}
resp_2 = {'sub_resp':[], 'sub_acc':[], 'prob':[], 'corr_resp':[], 'sub_RT':[]}
resp = [resp_1, resp_2]


#create problems and solutions to show
math_problems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
solutions = [4,2,1,3] #write solutions
prob_sol = list(zip(math_problems,solutions))

for block in range(nBlocks):
    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        resp[block]['prob'].append(prob_sol[np.random.choice(4)])
        resp[block]['corr_resp'].append(resp[block]['prob'][trial][1])
        
        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial
        
        count=-1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = resp[block]['prob'][trial][0] #present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed

                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    resp[block]['sub_RT'].append(rt_clock.getTime())
                    #get key for only the first response in that loop
                    resp[block]['sub_resp'].append(keys[0]) #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if resp[block]['sub_resp'][trial] == str(resp[block]['corr_resp'][trial]):
            resp[block]['sub_acc'].append(1) #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings              
        elif resp[block]['sub_resp'][trial] != str(resp[block]['corr_resp'][trial]):
            resp[block]['sub_acc'].append(2) #arbitrary number for inaccurate response 
                                    #(should be something other than 0 to distinguish 
                                    #from non-responses)
                    
        #print results
        print('problem=', resp[block]['prob'][trial], 'correct response=', 
              resp[block]['sub_resp'][trial], 'subject response=',resp[block]['sub_resp'][trial], 
              'subject accuracy=',resp[block]['sub_acc'][trial])
        


win.close()


#2. -------------------------------------------------------------
from psychopy import core, event, visual, monitors
import numpy as np

#monitor specs
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

#blocks, trials, stims, and clocks
nBlocks=2
nTrials=4
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#prefill dictionary for responses



#create problems and solutions to show
math_problems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
solutions = [4,2,1,3] #write solutions
prob_sol = list(zip(math_problems,solutions))

for block in range(nBlocks):
    resp = {'sub_resp':[], 'sub_acc':[], 'prob':[], 'corr_resp':[], 'sub_RT':[]}
    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        resp['prob'].append(prob_sol[np.random.choice(4)])
        resp['corr_resp'].append(resp['prob'][trial][1])
        
        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial
        
        count=-1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = resp['prob'][trial][0] #present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed

                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    resp['sub_RT'].append(rt_clock.getTime())
                    #get key for only the first response in that loop
                    resp['sub_resp'].append(keys[0]) #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if resp['sub_resp'][trial] == str(resp['corr_resp'][trial]):
            resp['sub_acc'].append(1) #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings              
        elif resp['sub_resp'][trial] != str(resp['corr_resp'][trial]):
            resp['sub_acc'].append(2) #arbitrary number for inaccurate response 
                                    #(should be something other than 0 to distinguish 
                                    #from non-responses)
                    
        #print results
        print('problem=', resp['prob'][trial], 'correct response=', 
              resp['sub_resp'][trial], 'subject response=',resp['sub_resp'][trial], 
              'subject accuracy=',resp['sub_acc'][trial])

#----------------------------------------------------------------------------------------------
#json Exercises
#----------------------------------------------------------------------------------------------
    
    
    #JSON files can be saved with txt or JSON extension, I like to use .txt
    filename = 'savejson_example'
    data_dir = os.path.join(main_dir,'data',filename)

    data_as_dict = []
    for a,b,c,d,e in zip(prob[block], corr_resp[block], sub_resp[block], sub_acc[block], sub_RT[block]):
        #the names listed here do not need to be the samr as the variable names
        data_as_dict.append({'problem':a,'corr_resp':b,'sub_resp':c,'sub_acc':d},'sub_RT':e)
               
    with open(data_dir + '_block%i.txt'%block, 'w') as outfile:
        son.dump(data_as_dict, outfile)
            
win.close()




















