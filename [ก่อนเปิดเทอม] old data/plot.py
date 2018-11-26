import csv
import matplotlib.pyplot as plt
from math import log

def plot_data():
    data_plot, cluster_plot = [], []
    count, all_sum, ch_count,time_round, sum_ch = 0, 0, 0, 0, 0
    for x in range(1,10):
        t_predefine = x/10
        data = []
        with open('data t '+str(t_predefine) +' and r0.csv', 'r') as csvnew:
            read = csv.reader(csvnew)
            for line1 in read:
                data.append(list(map(float, line1)))
        testList2 = [(time,lap,float(elem1), float(elem2)) for time,lap,elem1, elem2 in data ]

        for i in range(len(testList2)-1):
            if testList2[i][0] == testList2[i+1][0] \
               and testList2[i][3] == testList2[i+1][3] :
                ch_count += 1
            elif testList2[i][0] != testList2[i+1][0] \
                 and testList2[i][3] == testList2[i+1][3]:
                data_plot.append([testList2[i][3], testList2[i][1], ch_count])
                ch_count = 0
##    print(data_plot)
    data_plot.sort()
    data_plot.append([1,0.0, 0])#sparrr ไม่เกี่ยวกะข้อมูลเด้อ
    for index in range(len(data_plot)-1):
        if data_plot[index][0] == data_plot[index+1][0]:
            time_round += data_plot[index][1]
            sum_ch += data_plot[index][2]
        elif data_plot[index][0] != data_plot[index+1][0]:
            cluster_plot.append([data_plot[index][0], time_round, sum_ch])
            time_round, sum_ch = 0,0
    for i in cluster_plot:
        print(i[0], i[2]/i[1])
plot_data()
