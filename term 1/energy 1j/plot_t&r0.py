import csv
import matplotlib.pyplot as plt
import math 
import pandas as pd
from statistics import mean
import numpy as np

def fix():
    fix_1, fix_2, fix_3, fix_4, fix_5, = [],[],[],[],[]
    fix_6, fix_7, fix_8, fix_9 = [],[],[],[]
    for i in range(1,10):
        f = i/10
        with open('data t '+str(f)+' and r0.csv', 'r') as csvnew:
            read = csv.reader(csvnew)
            for line in read:
                if f == 0.1:
                    fix_1.append(list(map(float, line)))
                elif f == 0.2:
                    fix_2.append(list(map(float, line)))
                elif f == 0.3:
                    fix_3.append(list(map(float, line)))
                elif f == 0.4:
                    fix_4.append(list(map(float, line)))
                elif f == 0.5:
                    fix_5.append(list(map(float, line)))
                elif f == 0.6:
                    fix_6.append(list(map(float, line)))
                elif f == 0.7:
                    fix_7.append(list(map(float, line)))
                elif f == 0.8:
                    fix_8.append(list(map(float, line)))
                else:
                    fix_9.append(list(map(float, line)))
    fix_1.append(['','','',])
    fix_2.append(['','','',])
    fix_3.append(['','','',])
    fix_4.append(['','','',])
    fix_5.append(['','','',])
    fix_6.append(['','','',])
    fix_7.append(['','','',])
    fix_8.append(['','','',])
    fix_9.append(['','','',])
    
    return fix_1, fix_2, fix_3, fix_4, fix_5, fix_6, fix_7, fix_8, fix_9

def dfix_1(fix_1):
    count, r, avg_rfix1 = 0, 0, []
    for index in range(len(fix_1)-1):
        if fix_1[index][0] == 1.0:
            if fix_1[index][1] == fix_1[index+1][1]:
                count += 1
                r += fix_1[index][2]
            else:
                avg_rfix1.append(r/count)
                count, r = 0, 0
    return avg_rfix1

def dfix_2(fix_2):
    count, r, avg_rfix2 = 0, 0, []
    for index in range(len(fix_2)-1):
        if fix_2[index][0] == 1.0:
            if fix_2[index][1] == fix_2[index+1][1]:
                count += 1
                r += fix_2[index][2]
            else:
                avg_rfix2.append(r/count)
                count, r = 0, 0
    return avg_rfix2

def dfix_3(fix_3):
    count, r, avg_rfix3 = 0, 0, []
    for index in range(len(fix_3)-1):
        if fix_3[index][0] == 1.0:
            if fix_3[index][1] == fix_3[index+1][1]:
                count += 1
                r += fix_3[index][2]
            else:
                avg_rfix3.append(r/count)
                count, r = 0, 0
    return avg_rfix3

def dfix_4(fix_4):
    count, r, avg_rfix4 = 0, 0, []
    for index in range(len(fix_4)-1):
        if fix_4[index][0] == 1.0:
            if fix_4[index][1] == fix_4[index+1][1]:
                count += 1
                r += fix_4[index][2]
            else:
                avg_rfix4.append(r/count)
                count, r = 0, 0
    return avg_rfix4

def dfix_5(fix_5):
    count, r, avg_rfix5 = 0, 0, []
    for index in range(len(fix_5)-1):
        if fix_5[index][0] == 1.0:
            if fix_5[index][1] == fix_5[index+1][1]:
                count += 1
                r += fix_5[index][2]
            else:
                avg_rfix5.append(r/count)
                count, r = 0, 0
    return avg_rfix5

def dfix_6(fix_6):
    count, r, avg_rfix6 = 0, 0, []
    for index in range(len(fix_6)-1):
        if fix_6[index][0] == 1.0:
            if fix_6[index][1] == fix_6[index+1][1]:
                count += 1
                r += fix_6[index][2]
            else:
                avg_rfix6.append(r/count)
                count, r = 0, 0
    return avg_rfix6

def dfix_7(fix_7):
    count, r, avg_rfix7 = 0, 0, []
    for index in range(len(fix_7)-1):
        if fix_7[index][0] == 1.0:
            if fix_7[index][1] == fix_7[index+1][1]:
                count += 1
                r += fix_7[index][2]
            else:
                avg_rfix7.append(r/count)
                count, r = 0, 0
    return avg_rfix7

def dfix_8(fix_8):
    count, r, avg_rfix8 = 0, 0, []
    for index in range(len(fix_8)-1):
        if fix_8[index][0] == 1.0:
            if fix_8[index][1] == fix_8[index+1][1]:
                count += 1
                r += fix_8[index][2]
            else:
                avg_rfix8.append(r/count)
                count, r = 0, 0
    return avg_rfix8

def dfix_9(fix_9):
    count, r, avg_rfix9 = 0, 0, []
    for index in range(len(fix_9)-1):
        if fix_9[index][0] == 1.0:
            if fix_9[index][1] == fix_9[index+1][1]:
                count += 1
                r += fix_9[index][2]
            else:
                avg_rfix9.append(r/count)
                count, r = 0, 0
    return avg_rfix9

def dynamic():
    t_dynamic = []
    dyn_1, dyn_2, dyn_3, dyn_4, dyn_5, = [],[],[],[],[]
    dyn_6, dyn_7, dyn_8, dyn_9 = [],[],[],[]
    for i in range(1,10):
        f = i/10
        with open('data t dynamic '+str(f)+' and r0.csv', 'r') as csvnew:
            read = csv.reader(csvnew)
            for line in read:
                if f == 0.1:
                    dyn_1.append(list(map(float, line)))
                elif f == 0.2:
                    dyn_2.append(list(map(float, line)))
                elif f == 0.3:
                    dyn_3.append(list(map(float, line)))
                elif f == 0.4:
                    dyn_4.append(list(map(float, line)))
                elif f == 0.5:
                    dyn_5.append(list(map(float, line)))
                elif f == 0.6:
                    dyn_6.append(list(map(float, line)))
                elif f == 0.7:
                    dyn_7.append(list(map(float, line)))
                elif f == 0.8:
                    dyn_8.append(list(map(float, line)))
                else:
                    dyn_9.append(list(map(float, line)))
    dyn_1.append(['','','',])
    dyn_2.append(['','','',])
    dyn_3.append(['','','',])
    dyn_4.append(['','','',])
    dyn_5.append(['','','',])
    dyn_6.append(['','','',])
    dyn_7.append(['','','',])
    dyn_8.append(['','','',])
    dyn_9.append(['','','',])
    
    return t_dynamic, dyn_1, dyn_2, dyn_3, dyn_4, dyn_5, dyn_6, dyn_7, dyn_8, dyn_9

def dynamic_1(dyn_1):
    count, t, r, avg_t1, avg_r01 = 0, 0, 0, [], []
    for index in range(len(dyn_1)-1):
        if dyn_1[index][0] == 26.0:
            if dyn_1[index][1] == dyn_1[index+1][1]:
                count += 1
                t += dyn_1[index][2]
                r += dyn_1[index][3]
            else:
                avg_t1.append(t/count)
                avg_r01.append(r/count)
                count, t, r = 0,0, 0
    return avg_t1, avg_r01

def dynamic_2(dyn_2):
    count, t, r, avg_t2, avg_r02 = 0, 0, 0, [], []
    for index in range(len(dyn_2)-1):
        if dyn_2[index][0] == 22.0:
            if dyn_2[index][1] == dyn_2[index+1][1]:
                count += 1
                t += dyn_2[index][2]
                r += dyn_2[index][3]
            else:
                avg_t2.append(t/count)
                avg_r02.append(r/count)
                count, t, r = 0,0, 0
    return avg_t2, avg_r02

def dynamic_3(dyn_3):
    count, t, r, avg_t3, avg_r03 = 0, 0, 0, [], []
    for index in range(len(dyn_3)-1):
        if dyn_3[index][0] == 92.0:
            if dyn_3[index][1] == dyn_3[index+1][1]:
                count += 1
                t += dyn_3[index][2]
                r += dyn_3[index][3]
            else:
                avg_t3.append(t/count)
                avg_r03.append(r/count)
                count, t, r = 0,0, 0
    return avg_t3, avg_r03

def dynamic_4(dyn_4):
    count, t, r, avg_t4, avg_r04 = 0, 0, 0, [], []
    for index in range(len(dyn_4)-1):
        if dyn_4[index][0] == 35.0:
            if dyn_4[index][1] == dyn_4[index+1][1]:
                count += 1
                t += dyn_4[index][2]
                r += dyn_4[index][3]
            else:
                avg_t4.append(t/count)
                avg_r04.append(r/count)
                count, t, r = 0,0, 0
    return avg_t4, avg_r04

def dynamic_5(dyn_5):
    count, t, r, avg_t5, avg_r05 = 0, 0, 0, [], []
    for index in range(len(dyn_5)-1):
        if dyn_5[index][0] == 59.0:
            if dyn_5[index][1] == dyn_5[index+1][1]:
                count += 1
                t += dyn_5[index][2]
                r += dyn_5[index][3]
            else:
                avg_t5.append(t/count)
                avg_r05.append(r/count)
                count, t, r = 0,0, 0
    return avg_t5, avg_r05

def dynamic_6(dyn_6):
    count, t, r, avg_t6, avg_r06 = 0, 0, 0, [], []
    for index in range(len(dyn_6)-1):
        if dyn_6[index][0] == 56.0:
            if dyn_6[index][1] == dyn_6[index+1][1]:
                count += 1
                t += dyn_6[index][2]
                r += dyn_6[index][3]
            else:
                avg_t6.append(t/count)
                avg_r06.append(r/count)
                count, t, r = 0,0, 0
    return avg_t6, avg_r06

def dynamic_7(dyn_7):
    count, t, r, avg_t7, avg_r07 = 0, 0, 0, [], []
    for index in range(len(dyn_7)-1):
        if dyn_7[index][0] == 19.0:
            if dyn_7[index][1] == dyn_7[index+1][1]:
                count += 1
                t += dyn_7[index][2]
                r += dyn_7[index][3]
            else:
                avg_t7.append(t/count)
                avg_r07.append(r/count)
                count, t, r = 0,0, 0
    return avg_t7, avg_r07

def dynamic_8(dyn_8):
    count, t, r, avg_t8, avg_r08 = 0, 0, 0, [], []
    for index in range(len(dyn_8)-1):
        if dyn_8[index][0] == 4.0:
            if dyn_8[index][1] == dyn_8[index+1][1]:
                count += 1
                t += dyn_8[index][2]
                r += dyn_8[index][3]
            else:
                avg_t8.append(t/count)
                avg_r08.append(r/count)
                count, t, r = 0,0, 0
    return avg_t8, avg_r08

def dynamic_9(dyn_9):
    count, t, r, avg_t9, avg_r09 = 0, 0, 0, [], []
    for index in range(len(dyn_9)-1):
        if dyn_9[index][0] == 82.0:
            if dyn_9[index][1] == dyn_9[index+1][1]:
                count += 1
                t += dyn_9[index][2]
                r += dyn_9[index][3]
            else:
                avg_t9.append(t/count)
                avg_r09.append(r/count)
                count, t, r = 0,0, 0
    return avg_t9, avg_r09


def plot(avg_t1, avg_r01, avg_t2, avg_r02,avg_t3, avg_r03, avg_t4, avg_r04,\
         avg_t5, avg_r05, avg_t6, avg_r06,avg_t7, avg_r07, avg_t8, avg_r08,\
         avg_t9, avg_r09,\
         avg_rfix1, avg_rfix2, avg_rfix3, avg_rfix4, avg_rfix5, avg_rfix6, \
         avg_rfix7, avg_rfix8, avg_rfix9):
    fig, ax = plt.subplots(1,1)
    plt.plot(avg_t1[200:400], label ='t predefine 0.1 averge is '+str("%.2f"%float((mean(avg_t1[200:400])))))
    plt.plot(avg_t2[200:400], label ='t predefine 0.2 averge is '+str("%.2f"%float((mean(avg_t2[200:400])))))
    plt.plot(avg_t3[200:400], label ='t predefine 0.3 averge is '+str("%.2f"%float((mean(avg_t1[200:400])))))
    plt.plot(avg_t4[200:400], label ='t predefine 0.4 averge is '+str("%.2f"%float((mean(avg_t4[200:400])))))
    plt.plot(avg_t5[200:400], label ='t predefine 0.5 averge is '+str("%.2f"%float((mean(avg_t5[200:400])))))
    plt.plot(avg_t6[200:400], label ='t predefine 0.6 averge is '+str("%.2f"%float((mean(avg_t6[200:400])))))
    plt.plot(avg_t7[200:400], label ='t predefine 0.7 averge is '+str("%.2f"%float((mean(avg_t7[200:400])))))
    plt.plot(avg_t8[200:400], label ='t predefine 0.8 averge is '+str("%.2f"%float((mean(avg_t8[200:400])))))
    plt.plot(avg_t9[200:400], label ='t predefine 0.9 averge is '+str("%.2f"%float((mean(avg_t9[200:400])))))
    plt.xlabel('round')
    plt.ylabel('t_predefine')
    plt.title("average dynamix predefine")
    plt.legend()
    plt.show()

    fig = 18
    width = 0.2
    ind = np.arange(fig)
    lap_min = [min( avg_rfix1),min( avg_rfix2),min( avg_rfix3),min( avg_rfix4),min( avg_rfix5),
               min( avg_rfix6),min( avg_rfix7),min( avg_rfix8),min( avg_rfix9),\
               min(avg_r01),min(avg_r03),min(avg_r03),min(avg_r04),min(avg_r05),
               min(avg_r06),min(avg_r07),min(avg_r08),min(avg_r09)]
    lap_mean = [mean( avg_rfix1),mean( avg_rfix2),mean( avg_rfix3),mean( avg_rfix4),mean( avg_rfix5),
               mean( avg_rfix6),mean( avg_rfix7),mean( avg_rfix8),mean( avg_rfix9),\
                mean(avg_r01),mean(avg_r03),mean(avg_r03),mean(avg_r04),mean(avg_r05),
               mean(avg_r06),mean(avg_r07),mean(avg_r08),mean(avg_r09)]
    lap_max = [max( avg_rfix1),max( avg_rfix2),max( avg_rfix3),max( avg_rfix4),max( avg_rfix5),
               max( avg_rfix6),max( avg_rfix7),max( avg_rfix8),max( avg_rfix9),\
               max(avg_r01),max(avg_r03),max(avg_r03),max(avg_r04),max(avg_r05),\
               max(avg_r06),max(avg_r07),max(avg_r08),max(avg_r09)]
    plt.xticks(ind + width / 2, ('fix 0.1', 'fix 0.2', 'fix 0.3', 'fix 0.4', 'fix 0.5', \
                                 'fix 0.6', 'fix 0.7', 'fix 0.8', 'fix 0.9',\
                                 'dnm 0.1', 'dnm 0.2', 'dnm 0.3', 'dnm 0.4', 'dnm 0.5', \
                                 'dnm 0.6', 'dnm 0.7', 'dnm 0.8', 'dnm 0.9'))
    bar_1 = plt.bar(ind, lap_min, width, label =' minimum distance')
    bar_2 = plt.bar(ind+width, lap_mean, width,  label =' average distance')
    bar_3 = plt.bar(ind+(2*width), lap_max, width, label =' maximum distance')
    plt.xlabel('t_predefine')
    plt.ylabel('distance')
    plt.title("maximum distance in difference t_predefine value")
    for rect in bar_1 + bar_2+ bar_3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
    plt.legend()
    plt.tight_layout()
    plt.show()

    
def start():
    fix_1, fix_2, fix_3, fix_4, fix_5, fix_6, fix_7, fix_8, fix_9 = fix()
    t_dynamic, dyn_1, dyn_2, dyn_3, dyn_4, dyn_5, dyn_6, dyn_7, dyn_8, dyn_9 = dynamic()
    avg_t1, avg_r01 = dynamic_1(dyn_1)
    avg_t2, avg_r02 = dynamic_2(dyn_2)
    avg_t3, avg_r03 = dynamic_3(dyn_3)
    avg_t4, avg_r04 = dynamic_4(dyn_4)
    avg_t5, avg_r05 = dynamic_5(dyn_5)
    avg_t6, avg_r06 = dynamic_6(dyn_6)
    avg_t7, avg_r07 = dynamic_7(dyn_7)
    avg_t8, avg_r08 = dynamic_8(dyn_8)
    avg_t9, avg_r09 = dynamic_9(dyn_9)
    avg_rfix1 = dfix_1(fix_1)
    avg_rfix2 = dfix_2(fix_2)
    avg_rfix3 = dfix_3(fix_3)
    avg_rfix4 = dfix_4(fix_4)
    avg_rfix5 = dfix_5(fix_5)
    avg_rfix6 = dfix_6(fix_6)
    avg_rfix7 = dfix_7(fix_7)
    avg_rfix8 = dfix_8(fix_8)
    avg_rfix9 = dfix_9(fix_9)
    plot(avg_t1, avg_r01, avg_t2, avg_r02,avg_t3, avg_r03, avg_t4, avg_r04,\
         avg_t5, avg_r05, avg_t6, avg_r06,avg_t7, avg_r07, avg_t8, avg_r08, avg_t9, avg_r09,\
         avg_rfix1, avg_rfix2, avg_rfix3, avg_rfix4, avg_rfix5, avg_rfix6, \
         avg_rfix7, avg_rfix8, avg_rfix9)
start()
