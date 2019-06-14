import csv
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np
import pandas as pd

def read_offen():
    fields = ['B1']
    super_round = [3,5,10,15,20]
    x = [0,2,4,6,8,10]
    all_cm, cm_send, all_ch, ch_send = [], [], [], []
    offen = []
    original = []
    keep = []
    for sr in super_round:
        sr = int(sr)
        vv = []
        for i in x:
            print(sr,i)
            df = pd.read_csv('offen send SR '+str(sr)+' '+str(i)+'.csv' ,
                             skipinitialspace=True, usecols=fields)
##            df.hist(column='B1', alpha=0.5)
            plt.show()
            if sr == 1:
                mode = df.mode(axis=0)['B1'][0]
            else:
                mode = sr - df.mode(axis=0)['B1'][0]
            mean = sr - df.mean(axis=0)
            offen.append(mode)
            original.append(mean)
    count = 0
    xi = [ i for i in x]
    
    for item in range(0,len(offen),len(x)):
        plt.plot(xi,offen[item:item+len(x)], label= 'Super Round at N = '\
                 +str(super_round[count]))
        for i in range(len(offen[item: item+len(x)])):
            plt.text(x[i],offen[i+item],str(offen[i+item]),fontsize = 9)
        count += 1
    plt.title('BS will receive packet from CH in every period round, When using different data = 1%')
    plt.legend()
    plt.ylabel('period round until recive new update ')
    plt.ylim(-1,15)
    plt.xlabel('Dissimilar Data of send data from CM to CH (%)')
    plt.show()
##    count = 0
##    for item in range(0,len(offen),len(x)):
##        plt.plot(xi,original[item:item+len(x)], label= 'Super Round at N = '\
##                 +str(super_round[count]))
##        for i in range(len(offen[item: item+len(x)])):
##            plt.text(x[i], original[i+item], "%.3f"%float(original[i+item]),fontsize = 9)
##        count += 1
##    plt.title('offentimes of BS accepted update Data from CH in each Super Round at Dissimilar data = 1%')
##    plt.legend()
##    plt.ylabel('offentimes')
##    plt.ylim(-1,20)
##    plt.xlabel('Dissimilar Data (%)')
##    plt.show()      

read_offen()
