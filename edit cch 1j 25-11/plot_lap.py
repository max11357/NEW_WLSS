import csv
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np
 
def count_lap():
    count_1, count_2, count_3, count_4, count_5 = [], [], [], [],[]
    count_6, count_7, count_8, count_9 = [],[],[],[]
    dyn_1, dyn_2, dyn_3, dyn_4, dyn_5, = [],[],[],[],[]
    dyn_6, dyn_7, dyn_8, dyn_9 = [],[],[],[]
    
    for i in range(1,10):
        f = i/10
        with open('count lap fix '+str(f)+'.csv', 'r') as csvnew:
            read = csv.reader(csvnew)
            for line in read:
                if line[0] == '0.1':
                    count_1.append(list(map(float, line))[1])
                elif line[0] == '0.2':
                    count_2.append(list(map(float, line))[1])
                elif line[0] == '0.3':
                    count_3.append(list(map(float, line))[1])
                elif line[0] == '0.4':
                    count_4.append(list(map(float, line))[1])
                elif line[0] == '0.5':
                    count_5.append(list(map(float, line))[1])
                elif line[0] == '0.6':
                    count_6.append(list(map(float, line))[1])
                elif line[0] == '0.7':
                    count_7.append(list(map(float, line))[1])
                elif line[0] == '0.8':
                    count_8.append(list(map(float, line))[1])
                elif line[0] == '0.9':
                    count_9.append(list(map(float, line))[1])
        with open('count lap dynamic '+str(f)+'.csv', 'r') as csvnew:
            read = csv.reader(csvnew)
            for line in read:
                if line[0] == '0.1':
                    dyn_1.append(list(map(float, line))[1])
                elif line[0] == '0.2':
                    dyn_2.append(list(map(float, line))[1])
                elif line[0] == '0.3':
                    dyn_3.append(list(map(float, line))[1])
                elif line[0] == '0.4':
                    dyn_4.append(list(map(float, line))[1])
                elif line[0] == '0.5':
                    dyn_5.append(list(map(float, line))[1])
                elif line[0] == '0.6':
                    dyn_6.append(list(map(float, line))[1])
                elif line[0] == '0.7':
                    dyn_7.append(list(map(float, line))[1])
                elif line[0] == '0.8':
                    dyn_8.append(list(map(float, line))[1])
                elif line[0] == '0.9':
                    dyn_9.append(list(map(float, line))[1])
    return count_1, count_2, count_3, count_4, count_5, count_6, count_7, count_8, count_9,\
           dyn_1, dyn_2, dyn_3, dyn_4, dyn_5, dyn_6, dyn_7, dyn_8, dyn_9

def plot(count_1, count_2, count_3, count_4, count_5, count_6, count_7, count_8, count_9,\
           dyn_1, dyn_2, dyn_3, dyn_4, dyn_5, dyn_6, dyn_7, dyn_8, dyn_9):
    fig = 18
    width = 0.6
    ind = np.arange(fig)
    lap_min = [min(count_1),min(count_2),min(count_3),min(count_4),min(count_5),
               min(count_6),min(count_7),min(count_8),min(count_9),\
               min(dyn_1),min(dyn_2),min(dyn_3),min(dyn_4),min(dyn_5),\
               min(dyn_6),min(dyn_7),min(dyn_8),min(dyn_9)]
    
    lap_mean = [mean(count_1),mean(count_2),mean(count_3),mean(count_4),mean(count_5),
               mean(count_6),mean(count_7),mean(count_8),mean(count_9),\
               mean(dyn_1),mean(dyn_2),mean(dyn_3),mean(dyn_4),mean(dyn_5),\
               mean(dyn_6),mean(dyn_7),mean(dyn_8),mean(dyn_9)]
    
    lap_max = [max(count_1),max(count_2),max(count_3),max(count_4),max(count_5),
               max(count_6),max(count_7),max(count_8),max(count_9),\
               max(dyn_1),max(dyn_2),max(dyn_3),max(dyn_4),max(dyn_5),\
               max(dyn_6),max(dyn_7),max(dyn_8),max(dyn_9)]
    
    plt.xticks(ind +width / 15 , ('fig 0.1', 'fig 0.2', 'fig 0.3', 'fig 0.4', 'fig 0.5', \
                                 'fig 0.6', 'fig 0.7', 'fig 0.8', 'fig 0.9',\
                                 'dyn 0.1', 'dyn 0.2', 'dyn 0.3', 'dyn 0.4', 'dyn 0.5', \
                                 'dyn 0.6', 'dyn 0.7', 'dyn 0.8', 'dyn 0.9'))
    bar_1 = plt.bar(ind, lap_max, width, label =' maximum round')
    bar_2 = plt.bar(ind, lap_mean, width,  label =' average round')
    bar_3 = plt.bar(ind, lap_min, width, label =' minimum round')
    plt.ylabel('round')
    plt.title("round in difference t_predefine value")
    for rect in bar_1 + bar_2+ bar_3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')

    plt.legend()
    plt.tight_layout()
    plt.savefig('round in difference t_predefine value.png', bbox_inches='tight')
    plt.show()


def run():
    count_1, count_2, count_3, count_4, count_5, count_6, count_7, count_8, count_9,\
           dyn_1, dyn_2, dyn_3, dyn_4, dyn_5, dyn_6, dyn_7, dyn_8, dyn_9 = count_lap()
    plot(count_1, count_2, count_3, count_4, count_5, count_6, count_7, count_8, count_9,\
           dyn_1, dyn_2, dyn_3, dyn_4, dyn_5, dyn_6, dyn_7, dyn_8, dyn_9)
   
run()
