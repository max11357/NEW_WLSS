import csv
import matplotlib.pyplot as plt
from math import log
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
        print(len(fix))
    return fix

def data_fix(fix):
    dis_fix, t_fix, data_plot, cluster_plot = [], [], [], []
    count, dis_sum, f_count, f_sum = 0, 0, 0, 0
    time_round, sum_ch, ch_count = 0, 0, 0
    for i in range(len(fix)-1):
        if fix[i][0] == 0:
            pass
        
##        if fix[i][0] == fix[i+1][0] :
##            count += 1
##            f_count += 1
##            dis_sum += fix[i][2]
##            f_sum += fix[i][2]
##        elif fix[i][0] != fix[i+1][0]  and fix[i] != [' ',' ',' ']:
##            dis_fix.append([fix[i][3], dis_sum/count])
##            t_fix.append(f_sum/f_count)
##            count, dis_sum = 0, 0
##            f_count, f_sum = 0, 0

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
    dynamic = []
    with open('data t dynamic and r0.csv', 'r') as csvnew:
        read = csv.reader(csvnew)
        for line in read:
            dynamic.append(list(map(float, line)))
    dynamic.append([' ',' ',' '])
    return dynamic

def data_dynamic(t_dynamic):
    count, dis_sum, t_count, t_sum = 0, 0, 0, 0
    dis_dynamic, t_dy, t_val = [], [],[]
    for i in range(len(t_dynamic)-1):
        if t_dynamic[i][0] == t_dynamic[i+1][0]:
            count += 1
            t_count += 1
            dis_sum += t_dynamic[i][2]
            t_sum += t_dynamic[i][1]
            t_val.append(t_dynamic[i][1])
        elif t_dynamic[i][0] != t_dynamic[i+1][0]:
            dis_dynamic.append(dis_sum/count)
            t_dy.append([t_dynamic[i][2], t_sum/t_count])
            count, dis_sum = 0, 0
            t_count, t_sum = 0, 0
    return dis_dynamic, t_dy, t_val
    
    
def plot(fix_t_1, fix_t_2, fix_t_3, fix_t_4, fix_t_5, \
         fix_t_6, fix_t_7, fix_t_8, fix_t_9, dis_dynamic, t_dy, t_val):
    
    plt.plot(fix_t_1, label='0.1')
    plt.plot(fix_t_2, label='0.2')
    plt.plot(fix_t_3, label='0.3')
    plt.plot(fix_t_4, label='0.4')
    plt.plot(fix_t_5, label='0.5')
    plt.plot(fix_t_6, label='0.6')
    plt.plot(fix_t_7, label='0.7')
    plt.plot(fix_t_8, label='0.8')
    plt.plot(fix_t_9, label='0.9')
    plt.plot(dis_dynamic,label='dynamic  ' )
    plt.xlabel('round')
    plt.ylabel('average distance')
    plt.title("average fix and dynamix predefine")
    keep_len = 250
    plt.xlim(0,keep_len)
    plt.legend()
    plt.savefig('dis_dynamic.png')
    plt.show()

    t_val, avg_t = zip(*t_dy)
    plt.plot(avg_t,label='dynamic averge is' +str("%.3f"%float(sum(avg_t)/len(avg_t))))
    plt.xlabel('round')
    plt.ylabel('t_predefine')
    plt.title("average  dynamix predefine")
    plt.xlim(0,keep_len)
    plt.legend()
    plt.savefig('t_dynamic.png')
    plt.show()
    
    a, avg_t = zip(*t_dy)
    plt.plot(avg_t,label='dynamic averge is')
    plt.xlabel('round')
    plt.ylabel('t_predefine')
    plt.title("average  dynamix predefine")
    plt.xlim(0,keep_len)
    plt.legend()
    plt.savefig('t_dynamic.png')
    plt.show()
    plot_t = []
    for i in range(200):
        plot_t.append(t_val[i])
##    plt.plot(plot_t,label='t_predefine')
##    plt.show()

def read():
    fix = read_t_1()
    dis_fix, cluster_plot = data_fix(fix)
    fix_t_1, fix_t_2, fix_t_3, fix_t_4, fix_t_5, \
             fix_t_6, fix_t_7, fix_t_8, fix_t_9 = keep(dis_fix, cluster_plot)
    t_dynamic = dynamic()
    dis_dynamic, t_dy, t_val = data_dynamic(t_dynamic)
    plot(fix_t_1, fix_t_2, fix_t_3, fix_t_4, fix_t_5, \
         fix_t_6, fix_t_7, fix_t_8, fix_t_9, dis_dynamic, t_dy, t_val)
read()
