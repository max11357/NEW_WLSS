import csv
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np
import pandas as pd

def read_energy():
    lap_min,lap_mean,lap_max = [],[],[]
    super_round = [1,3,5,10, 15]
    for sr in super_round:
        data_0,data_1,data_2,data_3,data_4,data_5,data_6,data_7,data_8,data_9,data_10= [],[],[],[],[],[],[],[],[],[],[]
        for i in range(0,12,2):
            df = pd.read_csv('used energy SR '+str(sr)+' '+str(i)+'.csv')
            count_row = df.shape[0]
            per_sr = 0
            print(sr,i)
            for loop in range(0,count_row):
                if loop % sr == 0:
                    eval('data_%d'% (i)).append(per_sr)
                    add = df.iloc[[loop]].sum(axis=1)
                    per_sr = 0
                else:
                    add = df.iloc[[loop]].sum(axis=1)
                per_sr += float(add[loop])
            lap_mean.append(mean(eval('data_%d'% (i)))/sr)
    
    x= ['0%','2%','4%','6%','8%','10%']
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
    plt.title("Used Energy in Difference of Data in Super Round")
    plt.ylabel('Joule')
    plt.xlabel('Resamblance of Data')
    plt.ylim(0,0.15)
    plt.show()

read_energy()
