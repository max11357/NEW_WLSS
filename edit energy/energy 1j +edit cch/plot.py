import csv
import matplotlib.pyplot as plt
import math 
import pandas as pd

def read_t_1():
    fix = []
    for i in range(1,10):
        f = i/10
        with open('data t '+str(f)+' and r0.csv', 'r') as csvnew:
            read = csv.reader(csvnew)
            for line in read:
                fix.append(list(map(float, line)))
        fix.append([' ',' ',' ']) 
    return fix

def data_fix(fix):
    dis_fix, t_fix, data_plot, cluster_plot = [], [], [], []
    count, dis_sum, f_count, f_sum = 0, 0, 0, 0
    time_round, sum_ch, ch_count = 0, 0, 0
    for i in range(len(fix)-1):
        if fix[i][0] == fix[i+1][0] :
            count += 1
            f_count += 1
            dis_sum += fix[i][2]
            f_sum += fix[i][2]
        elif fix[i][0] != fix[i+1][0]  and fix[i] != [' ',' ',' ']:
            dis_fix.append([fix[i][3], dis_sum/count])
            t_fix.append(f_sum/f_count)
            count, dis_sum = 0, 0
            f_count, f_sum = 0, 0

    return dis_fix, cluster_plot
        
def keep(dis_fix, cluster_plot):
    fix_t_1, fix_t_2, fix_t_3, fix_t_4, fix_t_5= [], [], [], [], []
    fix_t_6, fix_t_7, fix_t_8, fix_t_9 = [], [], [], []
    
    count = 0
    for index in dis_fix:
        if index[0] == 0.1:
            fix_t_1.append(index[1])
        elif index[0] == 0.2:
            fix_t_2.append(index[1])
        elif index[0] == 0.3:
            fix_t_3.append(index[1])
        elif index[0] == 0.4:
            fix_t_4.append(index[1])
        elif index[0] == 0.5:
            fix_t_5.append(index[1])
        elif index[0] == 0.6:
            fix_t_6.append(index[1])
        elif index[0] == 0.7:
            fix_t_7.append(index[1])
        elif index[0] == 0.8:
            fix_t_8.append(index[1])
        elif index[0] == 0.9:
            fix_t_9.append(index[1])
    return fix_t_1, fix_t_2, fix_t_3, fix_t_4, fix_t_5, \
           fix_t_6, fix_t_7, fix_t_8, fix_t_9

def dynamic():
    t_dynamic = []
    dyn_1, dyn_2, dyn_3, dyn_4, dyn_5, = [],[],[],[],[]
    dyn_6, dyn_7, dyn_8, dyn_9 = [],[],[],[]
    for i in range(1,10):
        f = i/10
        with open('data t dynamic '+str(f)+' and r0.csv', 'r') as csvnew:
            read = csv.reader(csvnew)
            for line in read:
                t_dynamic.append(list(map(float, line)))
            t_dynamic.append([' ',' ',' '])
            
    print(t_dynamic[0])
    for index in range(len(t_dynamic)-1):
        if t_dynamic[index][2] == 0.1:
            if t_dynamic[index][1] == t_dynamic[index+1][1]:
                dyn_1.append()

    print(dyn_6)
    return t_dynamic, dyn_1, dyn_2, dyn_3, dyn_4, dyn_5, dyn_6, dyn_7, dyn_8, dyn_9

def data_dynamic(t_dynamic):
    count, dis_sum, t_count, t_sum = 0, 0, 0, 0
    dis_dynamic, t_dy, t_val = [], [],[]
    for i in range(len(t_dynamic)-1):
        
        if t_dynamic[i][0] == t_dynamic[i+1][0] :
            count += 1
            t_count += 1
            dis_sum += t_dynamic[i][3]
            t_sum += t_dynamic[i][2]
            t_val.append(t_dynamic[i][2])
        elif t_dynamic[i][0] != t_dynamic[i+1][0]:
            dis_dynamic.append(dis_sum/count)
            t_dy.append(t_sum/t_count)
            count, dis_sum = 0, 0
            t_count, t_sum = 0, 0
    return dis_dynamic, t_dy, t_val
    

def plot(dyn_1, dyn_2, dyn_3, dyn_4, dyn_5, dyn_6, dyn_7, dyn_8, dyn_9):



    plt.plot(dyn_1, label ='t predefine 0.1 averge is '+str("%.2f"%float(sum(dyn_1)/len(dyn_1))))
    plt.plot(dyn_2, label ='t predefine 0.2 averge is '+str("%.2f"%float(sum(dyn_2)/len(dyn_2))))
    plt.plot(dyn_3, label ='t predefine 0.3 averge is '+str("%.2f"%float(sum(dyn_3)/len(dyn_3))))
    plt.plot(dyn_4, label ='t predefine 0.4 averge is '+str("%.2f"%float(sum(dyn_4)/len(dyn_4))))
    plt.plot(dyn_5, label ='t predefine 0.5 averge is '+str("%.2f"%float(sum(dyn_5)/len(dyn_5))))
    plt.plot(dyn_6, label ='t predefine 0.6 averge is '+str("%.2f"%float(sum(dyn_6)/len(dyn_6))))
    plt.plot(dyn_7, label ='t predefine 0.7 averge is '+str("%.2f"%float(sum(dyn_7)/len(dyn_7))))
    plt.plot(dyn_8, label ='t predefine 0.8 averge is '+str("%.2f"%float(sum(dyn_8)/len(dyn_8))))
    plt.plot(dyn_9, label ='t predefine 0.9 averge is '+str("%.2f"%float(sum(dyn_9)/len(dyn_9))))
    plt.xlabel('round')
    plt.ylabel('t_predefine')
    plt.title("average  dynamix predefine")
    plt.xlim(0,930)
    plt.legend()
    plt.show()

    


def read():
    fix = read_t_1()
    dis_fix, cluster_plot = data_fix(fix)
    fix_t_1, fix_t_2, fix_t_3, fix_t_4, fix_t_5, \
             fix_t_6, fix_t_7, fix_t_8, fix_t_9 = keep(dis_fix, cluster_plot)
    
    t_dynamic, dyn_1, dyn_2, dyn_3, dyn_4, dyn_5, dyn_6, dyn_7, dyn_8, dyn_9 = dynamic()
    dis_dynamic, t_dy, t_val = data_dynamic(t_dynamic)
    plot(dyn_1, dyn_2, dyn_3, dyn_4, dyn_5, dyn_6, dyn_7, dyn_8, dyn_9)
read()
