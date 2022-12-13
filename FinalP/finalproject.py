#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:48:43 2022

@author: lucian
"""


#Introduction: As Stroop task is mainly assessing perception response or it is testing immediate/short-term memory, so I am wondering whether people can still remember the 
#perception response after a delay or more specifically, whether their perception memory is still intact in their memory after their working memory is being occupied by 
#doing arithemetic questions. As we know the central executive can simultaneously organize tasks, I am interested in whether this modified stroop task can also be handled well
#as the stroop task nature is highly misleading



#Procedure: This is a modifed stroop task. 
#First, participant will see a color word in different inks as the stimuli in Stroop Task. 
#Then participants will be presented a calculation after each word.
#After doing the calculation, there will be a 0.3s fixation and then they will need to answer the color the word is.



#=====================
#IMPORT MODULES
#=====================
import numpy as np
from psychopy import visual, core, gui, visual, event, monitors
import json
import os
import random
import pandas as pd
import datetime as datetime
#=====================
#PATH SETTINGS
#=====================
directory = os.getcwd()
path = os.path.join(directory, 'dataFiles')
if not os.path.exists(path):
    os.makedirs(path)
   
#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, handedness
expInfo = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi')}

#Display the dialog box
my_dlg = gui.DlgFromDict(dictionary=expInfo,title = ('Subject Info'),
                         order=('subject_nr', 'age', 'handedness'),
                         tip=None, screen=-1, sortKeys = True,
                         copyDict=False, labels=None, show=True)

expInfo['date'] = datetime.datetime.now() #get today's date time
filename = (str(expInfo['subject_nr']) + '_outputFile.csv')

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
nTrials = 12
nBlocks = 3
totalTrials = nTrials*nBlocks
nEach = int(totalTrials/3)

#create the stimulus list for Stroop
word = ['red','green','blue']
ink = ['red','green','blue']
trials = []

#create a list of paired stimuli for one block
for m in word:
    for n in ink:
        trials.append((m,n))
for item in word:
    trials.append((item,item))

#create the stimuli list for calculation 
math_problems = ['2+3=','1+8=','7-3=','8-6='] #write a list of simple arithmetic
solutions = [5,9,4,2] #write solutions
prob_sol = list(zip(math_problems,solutions))

#=====================
#PREPARE CONDITION LISTS
#=====================
#random shuffle each list to make them in random order for each block
trials_1 = trials
trials_2 = trials
trials_3 = trials
random.shuffle(trials_1)
random.shuffle(trials_2)
random.shuffle(trials_3)
trials = trials_1 + trials_2 + trials_3

#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
words = [0]*totalTrials
inks = [0]*totalTrials
accuracies_cal = [0]*totalTrials
accuracies = [0]*totalTrials
probs = [0]*totalTrials
sub_resp = [0]*totalTrials
responseTimes = [0]*totalTrials
trialNumbers = [0]*totalTrials
blockNumbers = [0]*totalTrials
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])

win = visual.Window(
 fullscr=False, 
 monitor=mon, 
 size=(600,600), 
 color='grey', 
 units='pix'
)
#instruction text defined by psychopy 
instructText = visual.TextStim(win, text='Press r for word red, g for word green, b for word blue')
stim = visual.TextStim(win, text = 'blue', color='black') 
fixation = visual.TextStim(win, text='+', color='black')
myMouse = event.Mouse(visible=False,win=win)
cal = visual.TextStim(win)
#=====================
#START EXPERIMENT
#=====================
instructText.draw()
win.flip()
event.waitKeys()

trial_timer = core.Clock()
#=====================
#BLOCK SEQUENCE
#=====================
for iblock in range(nBlocks):
    #start message for each block
    instructText.text = 'Press any key to begin Block ' + str(iblock+1)
    instructText.draw()
    #show the message and wait for keypress
    win.flip()
    event.waitKeys()
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    for itrial in range(nTrials):
        #=====================
        #START TRIAL
        #=====================   
        #define the number of trials have done so far
        overallTrial = iblock*nTrials+itrial
        blockNumbers[overallTrial] = iblock+1
        trialNumbers[overallTrial] = itrial+1
 
        words[overallTrial] = trials[overallTrial][0]
        inks[overallTrial] = trials[overallTrial][1]    
        
        #define the stimulus color setting for each trial
        stim.text= str(trials[overallTrial][0])
        stim.color = str(trials[overallTrial][1])
        
        trial_timer.reset() #reset the trial timer
        #display fixation for 300 ms
        while trial_timer.getTime() < 0.3: 
            fixation.draw()
            win.flip()
        #display the word for 1000 ms
        while trial_timer.getTime() < 1.3:
            stim.draw() 
            win.flip() 
        #choose a random problem from the list
        probs[overallTrial] = prob_sol[np.random.choice(4)]
        #the solution is at index 1 in the zipped list
        accuracies[overallTrial] = probs[overallTrial][1]
        
        trial_timer.reset() #reset the timer to make sure the fixation will only be displayed for 0.3s
        while trial_timer.getTime() < 0.3: 
            fixation.draw()
            win.flip()
        trial_timer.reset() #reset the timer to make sure the calculation will only be displayed for 3s
        count = -1
        while trial_timer.getTime() < 3:
            cal.text = probs[overallTrial][0]
            cal.draw()
            win.flip()

            keys_cal = event.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'escape'])
            
            if keys_cal:
                count += 1 #count up the number of times a key is pressed
                if count == 0: #if this is the first time a key is pressed
                    sub_resp[overallTrial] = keys_cal[0] #get key for only the first response in that loop
        
        #record subject accuracy
        #correct- remembers keys are saved as strings
        if sub_resp[overallTrial] == str(accuracies[overallTrial]):
            accuracies_cal[overallTrial] = 'Correct' #string to be saved to indicate the accuracy
        elif sub_resp[overallTrial] != str(accuracies[overallTrial]):
            accuracies_cal[overallTrial] = 'Incorrect'
        
        event.clearEvents(eventType='keyboard') #clear the keys we might have collected above
        
        stroop = visual.TextStim(win, text = 'please recall the colour the word you just saw is either red, green, or blue through pressing r, g, or b')
        stroop.draw()
        win.flip()
        trial_timer.reset() #reset the timer to reflect the RT for stroop task
        
        #wait for only the r, g and b keypresses
        keys=event.waitKeys(keyList=['r','g','b'])
        responseTimes[overallTrial] = trial_timer.getTime() #get the RT
        
        
        #identify whether the keypress is correct for this trial
        if keys:
            responseTimes[overallTrial] = trial_timer.getTime() 
            if trials[overallTrial][1] == 'red': #check whether the ink is red or not, if so, proceed, no, go to other ink color
                if keys[0] == 'r':
                    accuracies[overallTrial] = 'Correct'
                else:
                    accuracies[overallTrial] = 'Incorrect'
            elif trials[overallTrial][1] == 'blue':
                if keys[0] == 'b':
                    accuracies[overallTrial] = 'Correct'
                else:
                    accuracies[overallTrial] = 'Incorrect'
            else:
                if keys[0] == 'g':
                    accuracies[overallTrial] = 'Correct'
                else: 
                    accuracies[overallTrial] = 'Incorrect'
                    
        print(
         'Block:',
         iblock+1,
         ', Trial:', 
         itrial+1, 
         ',word[', 
         trials[overallTrial][0],
         '],ink[',
         trials[overallTrial][1],
         '], problem[', 
         probs[overallTrial][0],
         '], response[',
         sub_resp[overallTrial],
         ']: accuracies_cal:',
         accuracies_cal[overallTrial],
         ', accuracies_stroop:',
         accuracies[overallTrial], 
         ', RT:', 
         responseTimes[overallTrial]
        )

win.close()

#======================
# END OF EXPERIMENT
df = pd.DataFrame(data={
  "Block Number": blockNumbers, 
  "Trial Number": trialNumbers, 
  'Word': words,
  "Ink": inks, 
  'Prob': probs,
  'Accuracy_Cal': accuracies_cal,
  "Accuracy_Stroop": accuracies, 
  "Response Time": responseTimes
})
df.to_csv(os.path.join(path, filename), sep=',', index=False)

#close the experiment
win.close()
# #======================        