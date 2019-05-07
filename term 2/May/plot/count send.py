import csv
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np
import pandas as pd

def read_energy():
    lap_min,lap_mean,lap_max = [],[],[]
    super_round = [1,3,5, 10]
##    for sr in super_round:
##        data_0,data_1,data_2,data_3,data_4,data_5,data_6,data_7,data_8,data_9,data_10= [],[],[],[],[],[],[],[],[],[],[]
##        
##        for i in range(0,12,2):
##            per_sr = 0
##            df = pd.read_csv('used energy SR '+str(sr)+' '+str(i)+'.csv')
##            count_row = df.shape[0]
##            for loop in range(0,count_row):
##                add = df.iloc[[loop]].sum(axis=1)
##                if add[loop] == 0.0:
##                    per_sr += 1
##            lap_mean.append([count_row,per_sr])
    all_send = []
    real_send = []
    read = [[23623, 0], [27746, 0], [27335, 0], [27525, 0], [27901, 0], [25043, 0], [30436, 0], [60900, 12106], [71935, 28101], [80309, 40049], [72579, 41202], [81285, 49478], [29442, 0], [87070, 15329], [119841, 46388], [124949, 66347], [131169, 81460], [131524, 90043], [29691, 0], [94026, 13195], [162322, 53872], [169969, 82938], [212137, 128815], [232242, 160098]]
    
    for item in range(len(read)):
            all_send.append(read[item][0])
            real_send.append(read[item][0] - read[item][1])
    print(len(all_send))
    bar_width = 0.2
    x =[0,2,4,6,8,10]
    y_pos = np.arange(len(x))
    plt.bar(y_pos, all_send[18:24], color = (0.5,0.4,0.5,0.6))
    plt.bar(y_pos, real_send[18:24], color = (0.3,0.7,0.6,0.5))
    
    plt.xticks(y_pos,x )
    plt.title('Sending data of super round 10 in resamble data')
    plt.xlabel('resamble (%)')
    plt.ylabel('round' )
    plt.show()
##    print(all_send)
##    print(real_send)
##    x= ['0%','2%','4%','6%','8%','10%']
##    step = len(x)
##    count = 0
##    for lengh in range(0,len(lap_mean),len(x)):
##        print(lengh)
##        xi = [ i for i in x]
##        line2 = plt.plot(xi, lap_mean[lengh: lengh+step], marker='|', \
##                         label='Super Round is '+str(super_round[count]))
##        for i in range(len(lap_mean[lengh: lengh+step])):
##            plt.text(x[i], lap_mean[i+lengh], "%.2f"%float(lap_mean[i+lengh]),fontsize = 9)
##        count += 1
##    plt.legend()
####    plt.title("Used Energy in Difference of Data in Super Round")
####    plt.ylabel('Joule')
####    plt.xlabel('Resamblance of Data')
####    plt.ylim(0,0.15)
##    plt.show()

read_energy()
