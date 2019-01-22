import csv
from statistics import mean
import matplotlib.pyplot as plt
import numpy as np


def count_lap():
    fix_1, fix_2, fix_3, fix_4, fix_5, fix_6, fix_7, fix_8, fix_9 = [], [], [], [], [], [], [], [], []
    dyn_1, dyn_2, dyn_3, dyn_4, dyn_5, dyn_6, dyn_7, dyn_8, dyn_9 = [], [], [], [], [], [], [], [], []
    per_fix_1 ,per_fix_2, per_fix_3, per_fix_4, per_fix_5, \
                  per_fix_6, per_fix_7, per_fix_8, per_fix_9 = [], [], [], [], [], [], [], [], []
    per_dyn_1 ,per_dyn_2, per_dyn_3, per_dyn_4, per_dyn_5, \
                  per_dyn_6, per_dyn_7, per_dyn_8, per_dyn_9 = [], [], [], [], [], [], [], [], []
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
    
    cch_recive, cch_send, ch_sent, ch_recive, \
              cm_join, ch_recive_join, ch_cf_join, cm_recive_cf,\
              cm_send_data, ch_recive_data, ch_merge, ch_bs =\
              0,0,0,0,0,0,0,0,0,0,0,0
    c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11 = [],[],[],[],[],[],[],[],[],[],[]
    f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11 = [],[],[],[],[],[],[],[],[],[],[]
    for i in range(1,10):
        xi = ('cch recive', 'cch send', 'ch sent', 'chrecive', 'cm join', 'ch recive join', 'ch cf join', 'cm recive cf', 'cm send data', 'ch recive data', 'ch merge', 'ch bs')
        
        data_list =  eval('fix_%d'% (i))
        for item in data_list:
            cch_recive += float(item[0])
            cch_send += float(item[1])
            ch_sent += float(item[2])
            ch_recive += float(item[3])
            cm_join += float(item[4])
            ch_recive_join += float(item[5])
            ch_cf_join += float(item[6])
            cm_recive_cf += float(item[7])
            cm_send_data += float(item[8])
            ch_recive_data += float(item[9])
            ch_merge += float(item[10])
            ch_bs += float(item[11])
            
        eval('data_fix_%d'% (i)).append([cch_recive, cch_send, ch_sent, ch_recive, cm_join, ch_recive_join, ch_cf_join, cm_recive_cf,cm_send_data, ch_recive_data, ch_merge, ch_bs])

        for x in range(12):
            if sum(eval('data_fix_%d'% (i))[0]) == 0:
                pass
            else:
                data = eval('data_fix_%d'% (i))[0][x]#/sum(eval('data_dyn_%d'% (i))[0])*100
                eval('per_fix_%d'% (i)).append(data)
                
        cch_recive, cch_send, ch_sent, ch_recive, cm_join, ch_recive_join, ch_cf_join, cm_recive_cf, cm_send_data, ch_recive_data, ch_merge, ch_bs =\
              0,0,0,0,0,0,0,0,0,0,0,0
        
        data_list_dmn =  eval('dyn_%d'% (i))
        for item in data_list_dmn:
            cch_recive += float(item[0])
            cch_send += float(item[1])
            ch_sent += float(item[2])
            ch_recive += float(item[3])
            cm_join += float(item[4])
            ch_recive_join += float(item[5])
            ch_cf_join += float(item[6])
            cm_recive_cf += float(item[7])
            cm_send_data += float(item[8])
            ch_recive_data += float(item[9])
            ch_merge += float(item[10])
            ch_bs += float(item[11])

        eval('data_dyn_%d'% (i)).append([cch_recive, cch_send, ch_sent, ch_recive, cm_join, ch_recive_join, ch_cf_join, cm_recive_cf,cm_send_data, ch_recive_data, ch_merge, ch_bs])

        for x in range(12):
            if sum(eval('data_dyn_%d'% (i))[0]) == 0:
                pass
            else:
                data = eval('data_dyn_%d'% (i))[0][x]#/sum(eval('data_dyn_%d'% (i))[0])*100
                eval('per_dyn_%d'% (i)).append(data)
        cch_recive, cch_send, ch_sent, ch_recive, cm_join, ch_recive_join, ch_cf_join, cm_recive_cf, cm_send_data, ch_recive_data, ch_merge, ch_bs =\
              0,0,0,0,0,0,0,0,0,0,0,0
    fix = []
    dmn = []
    fix.append(sum(per_fix_1)/661/125)
    fix.append(sum(per_fix_2)/593/125)
    fix.append(sum(per_fix_3)/543/125)
    fix.append(sum(per_fix_4)/486/125)
    fix.append(sum(per_fix_5)/464/125)
    fix.append(sum(per_fix_6)/457/125)
    fix.append(sum(per_fix_7)/435/125)
    fix.append(sum(per_fix_8)/397/125)
    fix.append(sum(per_fix_9)/378/125)
    a = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]
    ai = [ i for i in a]
    plt.subplot(121)
    plt.plot(ai,fix, marker='o' )
    plt.ylabel('Energy used')
    plt.ylim(0.05,0.1)
    plt.xlabel('Fix T Predefine')
    plt.title('Energy Used for Fix T Predefine')
    plt.legend()
    dmn.append(sum(per_dyn_1)/554/125)
    dmn.append(sum(per_dyn_2)/548/125)
    dmn.append(sum(per_dyn_3)/520/125)
    dmn.append(sum(per_dyn_4)/525/125)
    dmn.append(sum(per_dyn_5)/523/125)
    dmn.append(sum(per_dyn_6)/518/125)
    dmn.append(sum(per_dyn_7)/515/125)
    dmn.append(sum(per_dyn_8)/494/125)
    dmn.append(sum(per_dyn_9)/500/125)

    plt.subplot(122)
    plt.plot(ai,dmn, marker='o' )
    plt.ylim(0.05,0.1)
    plt.ylabel('Energy used')
    plt.xlabel(' Initial Dynamic T Predefine')
    plt.title('Energy Used for Dynamic T Predefine')
    plt.legend()
    plt.show()
    print(fix)
    print(dmn)
        
####        cch_recive, cch_send, ch_sent, ch_recive, \
####              cm_join, ch_recive_join, ch_cf_join, cm_recive_cf,\
####              cm_send_data, ch_recive_data, ch_merge, ch_bs =\
####              0,0,0,0,0,0,0,0,0,0,0,0
####        
####        data_list_dmn =  eval('dyn_%d'% (i))
####        for item in data_list_dmn:
####            cch_recive += float(item[0])
####            cch_send += float(item[1])
####            ch_sent += float(item[2])
####            ch_recive += float(item[3])
####            cm_join += float(item[4])
####            ch_recive_join += float(item[5])
####            ch_cf_join += float(item[6])
####            cm_recive_cf += float(item[7])
####            cm_send_data += float(item[8])
####            ch_recive_data += float(item[9])
####            ch_merge += float(item[10])
####            ch_bs += float(item[11])
####
####            
####        eval('data_dyn_%d'% (i)).append([cch_recive, cch_send, ch_sent, ch_recive, cm_join, ch_recive_join, ch_cf_join, cm_recive_cf,cm_send_data, ch_recive_data, ch_merge, ch_bs])
####
####        
####        per_dyn_1 ,per_dyn_2, per_dyn_3, per_dyn_4, per_dyn_5, \
####                  per_dyn_6, per_dyn_7, per_dyn_8, per_dyn_9 = [], [], [], [], [], [], [], [], []
####        xi2 = ('cch recive', 'cch send', 'ch sent', 'chrecive', \
####              'cm join', 'ch recive join', 'ch cf join', 'cm recive cf',\
####              'cm send data', 'ch recive data', 'ch merge', 'ch bs')
####        
####        for x in range(12):
####            if sum(eval('data_dyn_%d'% (i))[0]) == 0:
####                pass
####            else:
####                data = eval('data_dyn_%d'% (i))[0][x]#/sum(eval('data_dyn_%d'% (i))[0])*100
####                eval('per_dyn_%d'% (i)).append(data)
####        if eval('per_dyn_%d'% (i)) != []:
####            plt.bar(xi2, eval('per_dyn_%d'% (i)))
####            plt.ylim(0,30)
####            plt.savefig('used_energy dyn'+str(i/10)+'.png')
####            plt.close()
####
####    
####        for val in range(1,10):
####            for index in eval('per_dyn_%d'% (val)):
####                eval('c%d'%(val)).append(index)
####
####        for val in range(1,10):
####            for index in eval('per_fix_%d'% (val)):
####                eval('f%d'%(val)).append(index)
####                
####    a = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]
####    ai = [ i for i in a]
####
####    
####    plt.subplot(121)
####    keep1,keep2,keep3,keep4,keep5 = [],[],[],[],[]
####    keep6,keep7,keep8,keep9, keep10,keep11,keep12 = [],[],[],[],[],[],[]
####    dkeep1,dkeep2,dkeep3,dkeep4,dkeep5 = [],[],[],[],[]
####    dkeep6,dkeep7,dkeep8,dkeep9,dkeep10 ,dkeep11,dkeep12 = [],[],[],[],[],[],[]
####    for n in range(1,10):
####        print(eval('per_fix_%d'% (n)))
####        print(sum(eval('per_fix_%d'% (n))))
####        print(sum(eval('per_fix_%d'% (n)))/50)
##            keep1.append(eval('f%d'% (n))[0])
##            keep2.append(eval('f%d'% (n))[1])
##            keep3.append(eval('f%d'% (n))[2])
##            keep4.append(eval('f%d'% (n))[3])
##            keep5.append(eval('f%d'% (n))[4])
##            keep6.append(eval('f%d'% (n))[5])
##            keep7.append(eval('f%d'% (n))[6])
##            keep8.append(eval('f%d'% (n))[7])
##            keep9.append(eval('f%d'% (n))[8])
##            keep10.append(eval('f%d'% (n))[9])
##            keep11.append(eval('f%d'% (n))[10])
##            keep12.append(eval('f%d'% (n))[11])

##    for n in range(1,10):
##        if (eval('c%d'% (n))) != []:
##            keep1.append(eval('f%d'% (n)))
####            keep1.append(eval('f%d'% (n))[0])
####            keep2.append(eval('f%d'% (n))[1])
####            keep3.append(eval('f%d'% (n))[2])
####            keep4.append(eval('f%d'% (n))[3])
####            keep5.append(eval('f%d'% (n))[4])
####            keep6.append(eval('f%d'% (n))[5])
####            keep7.append(eval('f%d'% (n))[6])
####            keep8.append(eval('f%d'% (n))[7])
####            keep9.append(eval('f%d'% (n))[8])
####            keep10.append(eval('f%d'% (n))[9])
####            keep11.append(eval('f%d'% (n))[10])
####            keep12.append(eval('f%d'% (n))[11])
##        if (eval('c%d'% (n))) != []:
##            dkeep1.append(eval('c%d'% (n))[0])
##            dkeep2.append(eval('c%d'% (n))[1])
##            dkeep3.append(eval('c%d'% (n))[2])
##            dkeep4.append(eval('c%d'% (n))[3])
##            dkeep5.append(eval('c%d'% (n))[4])
##            dkeep6.append(eval('c%d'% (n))[5])
##            dkeep7.append(eval('c%d'% (n))[6])
##            dkeep8.append(eval('c%d'% (n))[7])
##            dkeep9.append(eval('c%d'% (n))[8])
##            dkeep10.append(eval('c%d'% (n))[9])
##            dkeep11.append(eval('f%d'% (n))[10])
##            dkeep12.append(eval('f%d'% (n))[11])
##    
##    print(keep1)
##    plt.plot(ai, keep1, marker='o', label= 'CCH recive')
####    plt.plot(ai, keep2, marker='o', label= 'cch announcement ')
####    plt.plot(ai, keep3, marker='o', label= 'CH anouncement')
####    plt.plot(ai, keep4, marker='o', label= 'CH recive ')
####    plt.plot(ai, keep5, marker='o', label= 'CM join CH')
####    plt.plot(ai, keep6, marker='o', label= 'CH recive join')
####    plt.plot(ai, keep7, marker='o', label= 'CH confirm join ')
####    plt.plot(ai, keep8, marker='o', label= 'CM recive confirm')
####    plt.plot(ai, keep5, marker='o', label= 'CM send data')
####    plt.plot(ai, keep6, marker='o', label= 'CH recive data')
####    plt.plot(ai, keep7, marker='o', label= 'CH merge ')
####    plt.plot(ai, keep8, marker='o', label= 'CM send to BS')
##    plt.ylabel('Percent')
##    plt.xlabel('Fix T Predefine')
##    plt.title('Used Energy for Fix T Predefine')
##    plt.legend()
##
####    plt.subplot(122)
####    plt.plot(ai, dkeep1, marker='o', label= 'CCH recive')
####    plt.plot(ai, dkeep2, marker='o', label= 'cch announcement ')
####    plt.plot(ai, dkeep3, marker='o', label= 'CH anouncement')
####    plt.plot(ai, dkeep4, marker='o', label= 'CH recive ')
####    plt.plot(ai, dkeep5, marker='o', label= 'CM join CH')
####    plt.plot(ai, dkeep6, marker='o', label= 'CH recive join')
####    plt.plot(ai, dkeep7, marker='o', label= 'CH confirm join ')
####    plt.plot(ai, dkeep8, marker='o', label= 'CM recive confirm')
####    plt.plot(ai, dkeep5, marker='o', label= 'CM send data')
####    plt.plot(ai, dkeep6, marker='o', label= 'CH recive data')
####    plt.plot(ai, dkeep7, marker='o', label= 'CH merge ')
####    plt.plot(ai, dkeep8, marker='o', label= 'CM send to BS')
####    plt.ylabel('Percent')
####    plt.xlabel('Dynamic T Predefine')
####    plt.ylim(-2,50)
####    plt.title('Used Energy for Dynamic T Predefine')
####    plt.legend()
##    plt.show()
##
    plt.subplot(121)
    plt.plot(ai, keep1, marker='o', label= 'Fix T predefine')
    plt.plot(ai, dkeep1, marker='o', label= 'Dynamic T predefine')
    plt.ylim(-2,50)
    plt.ylabel('Percent')
    plt.xlabel('T Predefine')
    plt.title('Used Energy for send CCH anouncement')
    plt.legend()

##    plt.subplot(122)
##    plt.plot(ai, keep1, marker='o', label= 'CCH anouncement')
##    plt.ylim(-2,40)
##    plt.ylabel('Percent')
##    plt.xlabel('Fix T Predefine')
##    plt.title('Used Energy for Fix T Predefine')
##    plt.legend()
    plt.show()
##    
####    for b in range(1, 10):
####        eval('keep'%(b)).append(eval('f%d'% (b))[b])
####    plt.plot(ai, keep1, marker='o')
####    plt.show()
####            plt.legend()
####            plt.title('fix')
####            plt.ylim(-2,35)
##        
##        

    return data_fix_1, data_fix_2, data_fix_3, data_fix_4, data_fix_5,\
           data_fix_6, data_fix_7, data_fix_8, data_fix_9, \
           data_dyn_1, data_dyn_2, data_dyn_3, data_dyn_4, data_dyn_5,\
           data_dyn_6, data_dyn_7, data_dyn_8, data_dyn_9
count_lap()   
