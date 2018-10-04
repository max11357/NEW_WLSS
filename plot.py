import csv
import matplotlib.pyplot as plt
from math import log

def plot_data():
    data_plot, cluster_plot = [], []
    count, all_sum, cluster_count = 0, 0, 0
    for x in range(1,10):
        t_predefine = x/10
        data = []
        with open('data t '+str(t_predefine) +' and r0.csv', 'r') as csvnew:
            read = csv.reader(csvnew)
            for line1 in read:
                data.append(list(map(float, line1)))
        testList2 = [(time,lap,float(elem1), float(elem2)) for time,lap,elem1, elem2 in data ]

        for i in range(len(testList2)-1):
            if testList2[i][0] == testList2[i+1][0] and \
               testList2[i][1] == testList2[i+1][1]:
                cluster_count += testList2[i][1]
            elif testList2[i][0] != testList2[i+1][0] or \
                 testList2[i][1] != testList2[i+1][1]:
                print(cluster_count)
                cluster_plot.append([testList2[i][3],testList2[i][0], testList2[i][1], cluster_count])
            cluster_count = 0
    for i in cluster_plot:     
        print(i)

plot_data()
