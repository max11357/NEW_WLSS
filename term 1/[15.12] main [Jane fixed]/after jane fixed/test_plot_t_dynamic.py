import csv
import matplotlib.pyplot as plt
import math 
import pandas as pd
from statistics import mode, mean
import numpy as np

def fix():
    fix_1, fix_2, fix_3, fix_4, fix_5, = [],[],[],[],[]
    fix_6, fix_7, fix_8, fix_9 = [],[],[],[]

    dmn_1, dmn_2, dmn_3, dmn_4, dmn_5, = [],[],[],[],[]
    dmn_6, dmn_7, dmn_8, dmn_9 = [],[],[],[]

    avg_rfix_1, avg_rfix_2, avg_rfix_3, avg_rfix_4, avg_rfix_5, = [],[],[],[],[]
    avg_rfix_6, avg_rfix_7, avg_rfix_8, avg_rfix_9 = [],[],[],[]

    mode_rfix_1, mode_rfix_2, mode_rfix_3, mode_rfix_4, mode_rfix_5, = [],[],[],[],[]
    mode_rfix_6, mode_rfix_7, mode_rfix_8, mode_rfix_9 = [],[],[],[]

    mode_rdmn_1, mode_rdmn_2, mode_rdmn_3, mode_rdmn_4, mode_rdmn_5, = [],[],[],[],[]
    mode_rdmn_6, mode_rdmn_7, mode_rdmn_8, mode_rdmn_9 = [],[],[],[]

    rfix_1, rfix_2, rfix_3, rfix_4, rfix_5, = [],[],[],[],[]
    rfix_6, rfix_7, rfix_8, rfix_9 = [],[],[],[]
    
    tdmn_1, tdmn_2, tdmn_3, tdmn_4, tdmn_5, = [],[],[],[],[]
    tdmn_6, tdmn_7, tdmn_8, tdmn_9 = [],[],[],[]
    
    keepf, keepd = [],[]
    for i in range(1,10):
        f = i/10
        with open('data t '+str(f)+' and r0.csv', 'r') as csvnew:
            read = csv.reader(csvnew)
            for line in read:
                
                eval('fix_%d'% (i)).append(line)
        eval('fix_%d'% (i)).append(['','','',])
        
        count, r = 0, 0
        for index in range(len(eval('fix_%d'% (i)))-1):
##            if int(eval('fix_%d'% (i))[index][0]) >= 30:
                eval('mode_rfix_%d'% (i)).append(math.ceil(float(eval('fix_%d'% (i))[index][2])))
                eval('rfix_%d'% (i)).append(math.ceil(float(eval('fix_%d'% (i))[index][2])))
                if eval('fix_%d'% (i))[index][1] == eval('fix_%d'% (i))[index+1][1]:
                    count += 1
                    r += float(eval('fix_%d'% (i))[index][2])
                else:
                    if count == 0:
                        pass
                    else:
                        eval('avg_rfix_%d'% (i)).append(r/count)
                        count, r = 0, 0

##dynamic
        with open('data t dynamic '+str(f)+' and r0.csv', 'r') as csvnew:
            read = csv.reader(csvnew)
            for line in read:
                eval('dmn_%d'% (i)).append(line)
        eval('dmn_%d'% (i)).append(['','','',])
        
        count, sum_t= 0, 0
        for index in range(len(eval('dmn_%d'% (i)))-1):
            if eval('dmn_%d'% (i))[index][0] == '0.03' and eval('dmn_%d'% (i))[index][0] == '25.942243542145693':
                pass
##            elif float(eval('dmn_%d'% (i))[index][0]) > 5:
            cur = eval('dmn_%d'% (i))[index][1]
            nex = eval('dmn_%d'% (i))[index+1][1]
            if cur == nex and int(cur) > 0 :
                eval('mode_rdmn_%d'% (i)).append(math.ceil(float(eval('dmn_%d'% (i))[index][2])))
                sum_t += float(eval('dmn_%d'% (i))[index][4])
                count +=1
            elif int(cur)>0:
##                print(sum_t, count, eval('dmn_%d'% (i))[index], eval('dmn_%d'% (i))[index+1])
                eval('tdmn_%d'% (i)).append(sum_t/count)
                count, sum_t= 0, 0
##                eval('tdmn%d'% (i)).append(math.ceil(float(eval('dmn_%d'% (i))[index][4])))
                
                    
##        print(len(eval('tdmn_%d'% (i))))
            elif int(eval('dmn_%d'% (i))[index][0]) >=30 :
                eval('mode_rdmn_%d'% (i)).append(math.ceil(float(eval('dmn_%d'% (i))[index][2])))
                eval('rfix_%d'% (i)).append(math.ceil(float(eval('fix_%d'% (i))[index][2])))
                if eval('fix_%d'% (i))[index][1] == eval('fix_%d'% (i))[index+1][1]:
                    count += 1
                    r += float(eval('fix_%d'% (i))[index][2])
                else:
                    if count == 0:
                        pass
                    else:
                        eval('avg_rfix_%d'% (i)).append(r/count)
                        count, r = 0, 0

        keepf.append(mean(eval('mode_rfix_%d'% (i))))
        keepd.append(mean(eval('mode_rdmn_%d'% (i))))
    print(keepf)
    print(keepd)
        
##        tdmn_1[len(tdmn_1)-20:]
##        print(tdmn_2[len(tdmn_2)-20:])
##        print(tdmn_3[len(tdmn_3)-20:])
##        print(tdmn_4[len(tdmn_4)-20:])
##        print(tdmn_5[len(tdmn_5)-20:])
##        print(tdmn_6[len(tdmn_6)-20:])
##        print(tdmn_7[len(tdmn_7)-20:])
##        print(tdmn_8[len(tdmn_8)-20:])
##        print(tdmn_9[len(tdmn_9)-20:])
    
##    plt.plot(tdmn_1[len(tdmn_1)-40:])
##    plt.plot(tdmn_2[len(tdmn_2)-40:])
##    plt.plot(tdmn_3[len(tdmn_3)-40:])
##    plt.plot(tdmn_4[len(tdmn_4)-40:])
##    plt.plot(tdmn_5[len(tdmn_5)-40:])
##    plt.plot(tdmn_6[len(tdmn_6)-40:])
##    plt.plot(tdmn_7[len(tdmn_7)-40:])
##    plt.plot(tdmn_8[len(tdmn_8)-40:])
##    plt.plot(tdmn_9[len(tdmn_9)-40:])
##    plt.plot(tdmn_7[:300], label='Initiate T at 0.7')
##    plt.plot(tdmn_8[:300], label='Initiate T at 0.8')
##    plt.plot(tdmn_9[:300], label='Initiate T at 0.9')
##    plt.legend()
##    
##    plt.ylim(0,1)
##    plt.xlabel('Rounds')
##    plt.ylabel('T predefine')
##    plt.title('Differentiation of Dynamic T predefine  ')
##    plt.show()
##        plt.hist(eval('rfix_%d'% (i)), bins= max(eval('rfix_%d'% (i)))-3)
##        plt.ylabel('')
##        plt.ylim(0, 60000)
##        plt.xlim(0,70)
##        plt.savefig('rf'+str(i)+'.png')
##        plt.close()
##        mode = []
##        mode.append(mode(eval('mode_rfix_%d'% (1))))
    a = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]
    ai = [ i for i in a]
##    
    plt.plot(ai,keepf, marker='o', label='Cluster Size of Fix')
##    plt.plot(ai,keepd, marker='o', label='Cluster Size of Dynamic')
    plt.xlabel('T predefine')
    plt.ylabel('Operation Cluster Size')
    plt.title('Differentiation of Operation Cluster Size')
    plt.ylim(10,35)
    plt.show()
    
##    plt.plot(mode(eval('mode_rfix_%d'% (2))))

    plt.show()
fix()
