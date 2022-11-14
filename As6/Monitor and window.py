#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 20:08:52 2022

@author: lucian
"""
from psychopy import monitors, visual
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width = 35.36, distance = 60)
mon.setSizePix([1600, 900])

#changing units may potentially making the stimuli bigger than the window as for example, height units everything is specified relative to the height of the window
#by setting colorSpace as 'rgb', we can use the rgb values to define the color. Yes, for example, writing a string 'rgb255'.


#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor = mon)
win = visual.Window(monitor = mon, size = (800, 800), color = [-1, -1, -1], units = None, fullscr = False)