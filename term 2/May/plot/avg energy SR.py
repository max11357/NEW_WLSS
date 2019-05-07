import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def read_r0():
    fields = ['A1','B1','C1','D1','E1','F1','G1','H1','I1','J1','K1','L1']
    send_data_pkt = []
    super_round = [1,3,5, 10, 15]
##    diff = [0,0.25,0.5,0.75,1,1.25,1.5,1.75,2]
    diff = [0,2,4,6,8,10]
    group_ch = []
    send_data = []
    done = 0
    for sr in super_round:
        sr = int(sr)
        for i in diff:
            e_avg= []
            dont_send =  0
            for field in fields:
                df = pd.read_csv('used energy SR '+str(sr)+' '+str(i)+'.csv' ,
                                 skipinitialspace=True, usecols=[field])
                count_row = df.shape[0] -1
                total = df.sum(axis = 0, skipna = True)
                average = "%.6f"%float(total)
                e_avg.append(float(average))
            group_ch.append(sum(e_avg[:8])/(count_row/sr))
            send_data.append(sum(e_avg[8:])/(count_row/sr))
            
        send_data_pkt.append((send_data[-1]*(count_row/sr))/(count_row/sr))
    step = len(diff)
    for g in group_ch:
        if g  == 0.0:
            group_ch.remove(g)
    count = 0
    for lengh in range(0,len(group_ch),len(diff)):
        print(count)
        xi = [ i for i in diff]
        plt.plot(xi, group_ch[lengh: lengh+step], marker='|', \
                         label='Super Round is '+str(super_round[count]))
##        for i in range(len(group_ch[lengh: lengh+step])):
##            plt.text(diff[i], group_ch[i+lengh], "%.4f"%float(group_ch[i+lengh]),fontsize = 9)
        count += 1
    plt.title('Average Used Energy to Create a Group of CH in Super round')
    plt.xlabel('Resamblance (%)')
    plt.ylabel('Average Energy(J)' )
    plt.ylim(0,0.012)
    plt.legend()
    plt.show()

    count = 0
    group_ch = send_data
    for lengh in range(0,len(group_ch),len(diff)):
        xi = [ i for i in diff]
        plt.plot(xi, group_ch[lengh: lengh+step], marker='|', \
                         label='Super Round is '+str(super_round[count]))
        for i in range(len(group_ch[lengh: lengh+step])):
            plt.text(diff[i], group_ch[i+lengh], "%.4f"%float(group_ch[i+lengh]),fontsize = 9)
        count += 1
    plt.title('Average Used Energy to Send Data in Super round')
    plt.xlabel('Resamblance (%)')
    plt.ylabel('Average Energy(J)' )
    plt.ylim(0,1.6)
    plt.legend()
    plt.show()

    count = 0
    print(send_data_pkt)
    group_ch = send_data_pkt
    
    plt.plot(send_data_pkt ,marker = '.')
    plt.title('Average Used Energy to Send Data per 1 packet in Super round')
    plt.xlabel('')
    plt.ylabel('Average Energy(J)' )
    plt.ylim(0.0,0.2)
    plt.show()

read_r0()
