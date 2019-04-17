import random as rd
import math
import matplotlib.pyplot as plt
import csv
import collections
import numpy as np
def read_ch():
    index, index_cm = [],[]
    data, data_cm = [],[]
    energy, energy_cm = [],[]
    count, count_cm = 0,0
    t_pre, t_pre_cm = [],[]
    dead = []
    with open('dead point SR 1.csv', 'r') as csvnew:
        read = csv.reader(csvnew)
        for line in read:
            dead.append(line[:2])
    with open('check ch.csv', 'r') as csvnew:
        read = csv.reader(csvnew)
        for line in read:
            if line != [' ']:
                cut = tuple(map(float, line[2][1:-1].split(',')))
                lst = list(map(float, line[2][1:-1].split(',')))
                eng = float(line[3])
                t_val = line[4]
                data.append(cut)
                if cut not in index:
                    index.append(cut)
                    energy.append([count,lst, eng])
                    t_pre.append([count, lst, [t_val]])
                    count +=1
                for i in range(len(energy)):
                    if lst == energy[i][1]:
                        energy[i][2] = eng
                        t_pre[i][2].append(t_val)
                        
    with open('check cm.csv', 'r') as csvnew:
        read = csv.reader(csvnew)
        for line in read:
            if line != [' ']:
                cut_cm = tuple(map(float, line[2][1:-1].split(',')))
                lst_cm = list(map(float, line[2][1:-1].split(',')))
                eng_cm = float(line[3])
                t_val_cm = line[4]
                data_cm.append(cut_cm)
                if cut_cm not in index_cm:
                    index_cm.append(cut_cm)
                    energy_cm.append([count_cm,lst_cm, eng_cm])
                    t_pre_cm.append([count_cm, lst_cm, [t_val_cm]])
                    count_cm +=1
                
                for i in range(len(energy_cm)):
                    if lst_cm == energy_cm[i][1]:
                        energy_cm[i][2] = eng_cm
                        t_pre_cm[i][2].append(t_val_cm)
        

    width = 0.95
    cluster = collections.Counter(data)
    print(cluster)
    index.sort()
    ind = [ str(i) for i in index]
    index_cm.sort()
    ind_cm = [ str(i) for i in index_cm]
    print(len(index), len(index_cm))
    for i in range(len(index)):
        print(index[i], index_cm[i])
        plt.bar(ind[i],cluster[index[i]],\
                width, color=(0.5,0.7,0.7),align="center")
        plt.text(ind[i], cluster[index[i]]+5,cluster[index[i]], fontsize = 7)
    plt.xticks(np.arange(len(index))- width/8,rotation = 70, fontsize= 8)
    plt.title('statistic of node become to be cluster head '+str(len(energy)))
    plt.ylabel('number of node become to be cluster head')
##    plt.close()
    plt.show()
    plt.xlim(-60,110)
    plt.ylim(-10,110)
    plt.plot(-50, 50, '.', color='green', alpha=0.7)
    plt.text(-50,50,'base station',fontsize=8)
    plt.text(-50,45,"-50,50",fontsize = 6)
    plt.Circle((-50, 59), 20, color='pink', alpha=7)
    for i in range(len(energy_cm)):
        plt.plot(energy_cm[i][1][0], energy_cm[i][1][1], '.', color='b', alpha=0.7)
##        plt.text(energy_cm[i][1][0], energy_cm[i][1][1]+1,str(int(energy_cm[i][1][0]))+','+str(int(energy_cm[i][1][1])), fontsize = 6)
##        for en in range(len(energy_cm)):
##            if str(str(energy_cm[en][1][0])+', '+str(energy_cm[en][1][1])) == str(ind_cm[i])[1:-1]:
##                plt.text(energy_cm[i][1][0],energy_cm[i][1][1]-1,"%.4f"%float(energy[i][2])+' J',fontsize = 6)
##                plt.text(energy_cm[i][1][0],energy_cm[i][1][1]-2,"%.2f"%float(t_pre_cm[en][2][-1]),fontsize = 6)
    for i in range(len(energy)):
        plt.plot(energy[i][1][0], energy[i][1][1], '.', color='red', alpha=0.7)
##        plt.text(energy[i][1][0], energy[i][1][1]+1,str(int(energy[i][1][0]))+','+str(int(energy[i][1][1])), fontsize = 6)
##        for en in range(len(energy)):
##            if str(str(energy[en][1][0])+', '+str(energy[en][1][1])) == str(ind[i])[1:-1]:
##                plt.text(energy[i][1][0],energy[i][1][1]-1,"%.4f"%float(energy[i][2])+' J',fontsize = 6)
##                plt.text(energy[i][1][0],energy[i][1][1]-2,"%.2f"%float(t_pre[en][2][-1]),fontsize = 6)
    plt.plot(int(dead[0][0][:-2]), int(dead[0][1][:-2]), '.', color='k', alpha=1)
    plt.title('statistic of node become to be cluster head '+str(len(index)))
    plt.show()
read_ch()
