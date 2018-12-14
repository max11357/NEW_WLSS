import csv
from statistics import mean
import matplotlib.pyplot as plt
import numpy as np


def count_lap():
    fix_1, fix_2, fix_3, fix_4, fix_5, fix_6, fix_7, fix_8, fix_9 = [], [], [], [], [], [], [], [], []
    dyn_1, dyn_2, dyn_3, dyn_4, dyn_5, dyn_6, dyn_7, dyn_8, dyn_9 = [], [], [], [], [], [], [], [], []
    for i in range(1,10):
        f = i/10
        with open('used energy fix '+str(f)+'.csv', 'r', newline='') as csvnew:
            read = csv.reader(csvnew)
            for line in read:
                if f == 0.1:
                    fix_1.append(line)
                elif f == 0.2:
                    fix_2.append(line)
                elif f == 0.3:
                    fix_3.append(line)
                elif f == 0.4:
                    fix_4.append(line)
                elif f == 0.5:
                    fix_5.append(line)
                elif f == 0.6:
                    fix_6.append(line)
                elif f == 0.7:
                    fix_7.append(line)
                elif f == 0.8:
                    fix_8.append(line)
                elif f == 0.9:
                    fix_9.append(line)
        with open('used energy dmn '+str(f)+'.csv', 'r', newline='') as csvnew:
            read = csv.reader(csvnew)
            for line in read:
                if f == 0.1:
                    dyn_1.append(line)
                elif f == 0.2:
                    dyn_2.append(line)
                elif f == 0.3:
                    dyn_3.append(line)
                elif f == 0.4:
                    dyn_4.append(line)
                elif f == 0.5:
                    dyn_5.append(line)
                elif f == 0.6:
                    dyn_6.append(line)
                elif f == 0.7:
                    dyn_7.append(line)
                elif f == 0.8:
                    dyn_8.append(line)
                elif f == 0.9:
                    dyn_9.append(line)
                    
    data_fix_1, data_fix_2, data_fix_3, data_fix_4, data_fix_5, data_fix_6, data_fix_7, data_fix_8, data_fix_9 =\
                [], [],[],[],[],[],[],[],[]
    data_dyn_1, data_dyn_2, data_dyn_3, data_dyn_4, data_dyn_5, data_dyn_6, data_dyn_7, data_dyn_8, data_dyn_9 =\
                [], [],[],[],[],[],[],[],[]
    
    cch_sent, cch_recive, ch_sent, ch_recive = 0,0,0,0
    cm_send, cm_recive, ch_merg, ch_bs, ch_t, cm_t = 0,0,0,0,0, 0
    c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11 = [],[],[],[],[],[],[],[],[],[],[]
    f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11 = [],[],[],[],[],[],[],[],[],[],[]
    for i in range(1,10):
        xi = ('cch_sent', 'cch_recive', 'ch_sent', 'ch_recive', \
              'cm_send', 'cm_recive', 'ch_merg', 'ch_bs')
        data_list =  eval('fix_%d'% (i))
        for item in data_list:
            cch_sent += float(item[0])
            cch_recive += float(item[1])
            ch_sent += float(item[2])
            ch_recive += float(item[3])
            cm_send += float(item[4])
            cm_recive += float(item[5])
            ch_merg += float(item[6])
            ch_bs += float(item[7])
            
        eval('data_fix_%d'% (i)).append([cch_sent, cch_recive, ch_sent, ch_recive, cm_send, cm_recive, ch_merg, ch_bs])
        cch_sent, cch_recive, ch_sent, ch_recive = 0,0,0,0
        cm_send, cm_recive, ch_merg, ch_bs, ch_t, cm_t = 0,0,0,0,0, 0

        per_fix_1 ,per_fix_2, per_fix_3, per_fix_4, per_fix_5, \
                  per_fix_6, per_fix_7, per_fix_8, per_fix_9 = [], [], [], [], [], [], [], [], []
        for x in range(8):
            data = eval('data_fix_%d'% (i))[0][x]/sum(eval('data_fix_%d'% (i))[0])*100
            eval('per_fix_%d'% (i)).append(data)
            
        plt.bar(xi, eval('per_fix_%d'% (i)))
        plt.ylim(0,30)
        plt.savefig('used_energy fix'+str(i/10)+'.png')
        plt.close()
        
        
        
        data_list_dmn =  eval('dyn_%d'% (i))
        for item in data_list_dmn:
            cch_sent += float(item[0])
            cch_recive += float(item[1])
            ch_sent += float(item[2])
            ch_recive += float(item[3])
            cm_send += float(item[4])
            cm_recive += float(item[5])
            ch_merg += float(item[6])
            ch_bs += float(item[7])
            ch_t += float(item[8])
            cm_t += float(item[9])
        eval('data_dyn_%d'% (i)).append([cch_sent, cch_recive, ch_sent, ch_recive, cm_send, cm_recive, ch_merg, ch_bs, ch_t, cm_t])
        cch_sent, cch_recive, ch_sent, ch_recive = 0,0,0,0
        cm_send, cm_recive, ch_merg, ch_bs, ch_t, cm_t = 0,0,0,0,0, 0
        
        per_dyn_1 ,per_dyn_2, per_dyn_3, per_dyn_4, per_dyn_5, \
                  per_dyn_6, per_dyn_7, per_dyn_8, per_dyn_9 = [], [], [], [], [], [], [], [], []
        xi2 = ('cch_sent', 'cch_recive', 'ch_sent', 'ch_recive', \
              'cm_send', 'cm_recive', 'ch_merg', 'ch_bs', 'ch_t' , 'cm_t')
        
        for x in range(10):
            data = eval('data_dyn_%d'% (i))[0][x]/sum(eval('data_dyn_%d'% (i))[0])*100
            eval('per_dyn_%d'% (i)).append(data)
            
        plt.bar(xi2, eval('per_dyn_%d'% (i)))
        plt.ylim(0,30)
        plt.savefig('used_energy dyn'+str(i/10)+'.png')
        plt.close()

        for mem in range(1,10):
            print(mem)
            eval('c%d'% (mem)).append((eval('per_dyn_%d'% (i))[mem]))

        for fmem in range(1,8):
            eval('f%d'% (fmem)).append((eval('per_fix_%d'% (i))[fmem]))

    a = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]
    ai = [ i for i in a]

    
    plt.subplot(121)
    for n in range(1,8):
        plt.plot(ai, eval('f%d'% (n)), marker='o', label=str(xi[n]))
        plt.legend()
        plt.title('fix')
        plt.ylim(-2,35)


    plt.subplot(122)
    for n in range(1,10):
        plt.title('dynamic')
        plt.plot(ai, eval('c%d'% (n)), marker='o', label=str(xi2[n]))
        plt.legend()
        plt.ylim(-2,35)
    plt.show()

    return data_fix_1, data_fix_2, data_fix_3, data_fix_4, data_fix_5,\
           data_fix_6, data_fix_7, data_fix_8, data_fix_9, \
           data_dyn_1, data_dyn_2, data_dyn_3, data_dyn_4, data_dyn_5,\
           data_dyn_6, data_dyn_7, data_dyn_8, data_dyn_9
count_lap()   
