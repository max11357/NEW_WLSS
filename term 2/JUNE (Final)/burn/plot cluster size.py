import csv
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np
import pandas as pd

def read_r0():
    
    fields = ['C1']
    lap_min,lap_mean,lap_max = [],[],[]
    super_round = [1,3,5,10,15,20]
    x= ['0','2','4','6','8','10']
    step = len(x)
    for sr in super_round:
        data_0,data_1,data_2,data_3,data_4,data_5,data_6,data_7,data_8,data_9,data_10= [],[],[],[],[],[],[],[],[],[],[]
        for i in range(0,len(x)*2,2):
            df = pd.read_csv('data t and rd SR '+str(sr)+' '+str(i)+'.csv' , \
                             skipinitialspace=True, usecols=fields)
            count_row = df.shape[0] 
            total = df.sum(axis = 0, skipna = True)
            average = "%.2f"%float(int(total)/count_row)
            lap_mean.append(float(average))
            print(sr, i)
    count = 0
    for lengh in range(0,len(lap_mean),len(x)):
        
        xi = [ i for i in x]
        line2 = plt.plot(xi, lap_mean[lengh: lengh+step], marker='|', \
                         label='Super Round is '+str(super_round[count]))
##        for i in range(len(lap_mean[lengh: lengh+step])):
##            plt.text(x[i], lap_mean[i+lengh], lap_mean[i+lengh],fontsize = 9)
        count += 1

    plt.legend()
    plt.title("Operation Cluster size in Super Round at Deploy Cluster Size = 30 meter")
    plt.ylabel('Operation Cluster size')
    plt.ylim(0,35)
    plt.xlabel('Resamblance of Data')
    plt.show()

read_r0()
