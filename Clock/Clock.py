#!/usr/bin/env python
import subprocess as sp
import time
class Time:
    def __init__(self):
        self.h = time.strftime('%H')
        self.m = time.strftime('%M')
        self.s = time.strftime('%S')
        self.dlen1 = {1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE'}
        self.dlen2 = {1: 'TEN', 2: 'TWENTY', 3: 'THIRTY', 4: 'FOURTY', 5: 'FIFTY'}
        self.dsmall = {11: 'ELEVEN', 12: 'TWELVE', 13: 'THIRTEEN', 14: 'FOURTEEN', 15: 'FIFTEEN', 16: 'SIXTEEN', 17: 'SEVENTEEN', 18: 'EIGHTEEN', 19: 'NINETEEN'}

    def display(self):

        print '---------------------'
        print self.upgradeddisplay(self.h), 'HOURS'
        print self.upgradeddisplay(self.m), 'MINUTES'
        print self.upgradeddisplay(self.s), 'SECONDS'
        print '---------------------'


    def upgradeddisplay(self,n):
        l = list(str(n))
        if 11<= int(n)<= 19:
            return self.dsmall[int(n)]
        elif int(l[0]) == 0 and int(l[1]) == 0:
            return 'ZERO'
        elif int(l[0]) != 0 and int(l[1]) == 0:
            return self.dlen2[int(l[0])]
        elif int(l[0]) == 0 and int(l[1])!= 0:
            return self.dlen1[int(l[1])]
        else:
            return self.dlen2[int(l[0])] +' '+ self.dlen1[int(l[1])]
while True:
    a = Time()
    time.sleep(1)
    x=sp.call('clear',shell=True)
    a.display()
