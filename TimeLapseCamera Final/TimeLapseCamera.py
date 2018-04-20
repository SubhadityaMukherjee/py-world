#TimeLapse Camera

#!/usr/bin/env python

import SimpleCV
import time
cam = SimpleCV.Camera()
n = int(raw_input('Enter time in seconds '))
i = int(raw_input('Enter interval in seconds '))
m = raw_input('Enter default name ')
p = 1
bw = 0
r = raw_input('For black and white images type b For color just hit enter. ')
if r == 'b':
    bw = 1
for a in range(n/i):
    print 'Clicking image', p, 'in 3 seconds'
    time.sleep(i)
    img = cam.getImage()
    if bw == 1:
        img = img.grayscale()
    img.save(m+str(p)+'.png') 
    p += 1
print 'Done.. Check folder..'

