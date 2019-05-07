import random as rd
import math
import matplotlib.pyplot as plt
import csv
import collections
import numpy as np

def read_cch():
    dead , keep_lap, index, cch_data, ch_data = [],[],[],[],[]
    with open('dead point SR 1.csv', 'r') as csvnew:
        read = csv.reader(csvnew)
        for line in read:
            dead.append(list(map(float,line[:2])))
    with open('check ch.csv', 'r') as csvnew:
        read = csv.reader(csvnew)
        for line in read:
            if line != [' ']:
                cut = [int(line[0]),\
                       list(map(float, line[2][1:-1].split(',')))[0],\
                       list(map(float, line[2][1:-1].split(',')))[1],\
                       float(line[3]), float(line[4])]
                ch_data.append(cut)
                if dead[0] == cut[1:3]:
                    keep_lap.append(cut[0])
    with open('check cch.csv', 'r') as csvnew:
        read = csv.reader(csvnew)
        for line in read:
            if line != [' ']:
                cut = list(map(float,line[:4]))
                cch_data.append(cut)
    
    for index in keep_lap:
        count = index
        x,y = [],[]
        for cch in cch_data:
            if cch[0] == index and index == count:                
                plt.plot(cch[1], cch[2], '.', color='b', alpha=0.7)
                plt.text(cch[1], cch[2]+1,'energy '+str("%.2f"%float(cch[-1])), fontsize=6)
        for ch in ch_data:
            if ch[0] == index and index == count:
                plt.plot(ch[1],ch[2],'s', color='r' )
##                plt.text(ch[1],ch[2]-2,'ch = '+str("%.2f"%float(ch[3])), fontsize=6)
        plt.title('candidate cluster head become cluster head')
        plt.savefig('cch round '+str(index)+'.png', bbox_inches='tight', dpi=1000)
        plt.close()
        
##        plt.show()
                
read_cch()