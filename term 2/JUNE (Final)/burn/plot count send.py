import csv
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np
import pandas as pd

def read_energy():
    fields = ['num CM','CM send','num CH','CH send']
    send_data_pkt = []
    super_round = [1,3,5,10,15,20]
    sim = int(100)
    x = [0,2,4,6,8,10]
    all_cm, cm_send, all_ch, ch_send = [], [], [], []
    done = 0
    per_sr = 0
##    for sr in super_round:
##        sr = int(sr)
##        read = []
##        for i in x:
##            e_avg= []
##            
##            dont_send =  0
##            print(sr,i)
##            for field in fields:
##                df = pd.read_csv('real send '+str(sr)+' '+str(i)+'.csv' ,
##                                 skipinitialspace=True, usecols=[field])
##                count_row = df.shape[0] -1
##                total = df.sum(axis = 0, skipna = True)
##                print(total)
##                print(type(float(total)))
##                average = float("%.4f"%float(total))/sim
##                read.append(average)
##            print(read)
    read = [[269939.58, 269939.58, 15020.42, 15020.42],\
            [269953.06, 269953.06, 14980.69, 14980.69], \
            [267957.17, 267957.17, 15009.08, 15009.08], \
            [269380.84, 269380.84, 15086.66, 15086.66],\
            [273796.26, 273796.26, 15159.99, 15159.99],\
            [271700.36, 271700.36, 15103.39, 15103.39],\
            
            [360260.84, 360260.84, 19580.41, 11255.64],\
            [528228.85, 254965.59, 28837.4, 14425.21],\
            [641719.09, 246468.95, 35460.91, 15433.89],\
            [681286.44, 240828.36, 37712.31, 14998.7],\
            [751010.84, 256988.48, 41820.41, 15631.22],\
            [767806.9, 259430.92, 42888.1, 15431.38],\
            
            [351674.76, 351674.76, 18645.24, 9657.96],\
            [559292.83, 227430.58, 30208.42, 13741.25],\
            [733862.1, 207157.92, 40117.9, 15089.38],\
            [893759.87, 213164.99, 49131.38, 15683.86],\
            [980575.5, 215916.84, 54352.0, 15478.33], \
            [1078737.68, 227733.05, 60086.07, 15596.47],\
            
            [303187.33, 303187.33, 15206.42, 7120.12],\
            [476306.04, 166425.65, 24678.96, 10458.95],\
            [665986.13, 143498.23, 34936.37, 12658.44],\
            [846280.38, 139161.41, 45105.87, 13696.41],\
            [1037659.99, 145181.62, 55637.51, 14443.55], \
            [1268805.63, 159729.91, 68494.37, 15408.33],\
            
            [280366.66, 280366.66, 13577.09, 6221.05],\
            [423719.99, 139244.67, 21070.01, 8742.93],\
            [564927.67, 110233.98, 28812.33, 10465.45],\
            [701754.55, 100069.21, 36199.2, 11289.07], \
            [862719.18, 100281.96, 45118.32, 12124.69],\
            [1105120.43, 111511.20, 58476.07, 13622.23],\
            
            [269643.56, 269643.56, 12871.44, 5812.94],\
            [403148.41, 129071.85, 19806.59, 8144.72],\
            [496587.1, 90872.74, 24747.9, 8920.47],\
            [618451.6,81113.9, 31237.15, 9896.25],\
            [751234.61, 78994.06, 38472.89, 10641.78], \
            [971110.1, 86408.66, 50332.4, 12129.88]]

    for i in read:
        all_cm.append(i[0])
        cm_send.append(i[1])
        all_ch.append(i[2])
        ch_send.append(i[3])
    x =[0,2,4,6,8,10]
    y_pos = np.arange(len(x))
    count = 0
    
    for lengh in range(0,len(all_cm), len(x)):
        
        plt.subplot(121)
        plt.title('Data Transmition from CM to CH\n When ues Dissimilar data')
        plt.bar(y_pos , all_cm[lengh:lengh+len(x)], color = (0.5,0.4,0.9,0.3),width=0.5)
        plt.bar(y_pos, cm_send[lengh:lengh+len(x)], color = (0.4,0.7,0.8,0.9),width=0.5)
        plt.ylim(0,1300000)
        plt.xlabel('Dissimilar data (%)')
        plt.xticks(y_pos,x )
        plt.ylabel('times' )
        plt.subplot(122)
        plt.title('Data Transmition from CH to BS \nwhen Dissimilar data = 1%')
        plt.bar(y_pos, all_ch[lengh:lengh+len(x)], color = (0.7,0.3,0.6,0.6), width=0.5)
        plt.bar(y_pos, ch_send[lengh:lengh+len(x)], color = (0.1,0.3,0.6,0.6), width=0.5)
        plt.xticks(y_pos,x )
        plt.ylim(0,100000)
        plt.xlabel('Dissimilar data (%)')
        plt.ylabel('times' )
        
        plt.show()
        count += 1
            

read_energy()
