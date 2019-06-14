import csv
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np

def read_count():
    lap_min,lap_mean,lap_max = [],[],[]
    super_round = [1,3,5,10,15,20]
    for sr in super_round:
        data_0,data_1,data_2,data_3,data_4,data_5,data_6,data_7,data_8,data_15,data_10= [],[],[],[],[],[],[],[],[],[],[]
        for i in range(0,12,2):
            with open('count lap SR '+str(sr)+' '+str(i)+'.csv', 'r') as csvnew:
                read = csv.reader(csvnew)
                for line in read:
                    eval('data_%d'% (i)).append(float(line[1]))
            print(sr, i)
            lap_mean.append(mean(eval('data_%d'% (i))))
    x= ['0','2','4','6','8','10']
    step = len(x)
    count = 0
    for lengh in range(0,len(lap_mean),len(x)):
        xi = [ i for i in x]
        line2 = plt.plot(xi, lap_mean[lengh: lengh+step], marker='|', \
                         label='Super Round is '+str(super_round[count]))
        for i in range(len(lap_mean[lengh: lengh+step])):
            plt.text(x[i], lap_mean[i+lengh], "%.2f"%float(lap_mean[i+lengh]),fontsize = 9)
        count += 1
    plt.legend()
    plt.title("Average Rounds Dissimilar Data of Super Round")
    plt.ylabel('Round')
    plt.xlabel('Dissimilar of Data')
    plt.show()
read_count()
