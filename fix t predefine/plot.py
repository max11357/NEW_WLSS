import csv
import matplotlib.pyplot as plt
from math import log
import pandas as pd

def plot_data():
    data = []
    for x in range(1,10):
        t_predefine = x/10
        with open('data t '+str(t_predefine) +' and r0.csv', 'r') as csvnew:
            read = csv.reader(csvnew)
            for line1 in read:
                data.append(list(map(float, line1)))
        testList2 = [(time,lap,float(elem1), float(elem2)) for time,lap,elem1, elem2 in data ]
        testList2.append([' ',' ',' '])
        ch_plot, cluster_plot, data_plot = [], [], []
        count, all_sum, ch_count,time_round, sum_ch = 0, 0, 0, 0, 0
        for i in range(len(testList2)-1):
            if testList2[i][0] == testList2[i+1][0]:
                count += 1
                all_sum += testList2[i][2]
            elif testList2[i][0] != testList2[i+1][0]:
                data_plot.append([testList2[i][0], all_sum/count])
                count, all_sum = 0, 0
            if testList2[i][0] == testList2[i+1][0] and testList2[i][3] == testList2[i+1][3] :
                ch_count += 1
            elif testList2[i][0] != testList2[i+1][0] and testList2[i][3] == testList2[i+1][3]:
                ch_plot.append([testList2[i][3], testList2[i][1], ch_count])
                ch_count = 0 
        x,y = zip(*data_plot)
        plt.plot(y,label=str(t_predefine))
        plt.legend()
        keep_len = 215
        plt.xlim(0,keep_len)
        
    
        
   
    data = []
    with open('data t dynamic and r0.csv', 'r') as csvnew:
        read = csv.reader(csvnew)
        for line1 in read:
            data.append(list(map(float, line1)))
    testList2 = [(time,lap,float(elem1), float(elem2)) for time,lap,elem1, elem2 in data ]
    testList2.append([' ',' ',' '])
    t_count, count, all_sum, all_t = 0, 0, 0, 0
    data_plot, t_plot = [], []
    for i in range(len(testList2)-1):
        if testList2[i][0] == testList2[i+1][0]:
            count += 1
            all_sum += testList2[i][3]
        elif testList2[i][0] != testList2[i+1][0]:
            data_plot.append([testList2[i][0], all_sum/count])
            count, all_sum = 0, 0
        if testList2[i][0] == testList2[i+1][0]:
            t_count += 1
            all_t += testList2[i][2]
        elif testList2[i][0] != testList2[i+1][0]:
            t_plot.append([testList2[i][2], all_t/t_count])
            t_count, all_t = 0, 0
        
    x,y = zip(*data_plot)
    plt.plot(y,label='dynamic ')
    plt.xlabel('round')
    plt.ylabel('average distance')
    plt.title("average fix and dynamix predefine")
    keep_len = 215
    plt.xlim(0,keep_len)
    plt.legend()
    plt.savefig('dynamic.png')
    plt.show()

    plt.show()
    t,num = zip(*t_plot)
    plt.plot(num,label='dynamic ')
    plt.xlabel('round')
    plt.ylabel('t_predefine')
    plt.title("average dynamix predefine is "+str("%.4f"%float(sum(num)/len(num))))
    keep_len = 215
    plt.xlim(0,keep_len)

    plt.show()

    df = pd.DataFrame(cluster_plot,  )
    df.plot(kind='bar')
    plt.show()

plot_data()
