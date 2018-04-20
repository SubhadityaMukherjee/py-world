#!/usr/bin/env python

import SimpleCV
import time
cam = SimpleCV.Camera()
n = int(raw_input('Enter no of images '))
m = raw_input('Enter default name ')
p = 1
bw = 0
r = raw_input('For black and white images type b For color just hit enter. ')
if r == 'b':
    bw = 1
for a in range(n):
    print 'Clicking image', p, 'in 3 seconds'
    time.sleep(3)
    img = cam.getImage()
    print img.readText()
print 'Done.. Check folder..'

