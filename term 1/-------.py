import csv
import matplotlib.pyplot as plt
from math import log
import pandas as pd

def dynamic():
    dynamic = []
    with open('data t dynamic and r0.csv', 'r') as csvnew:
        read = csv.reader(csvnew)
        for line in read:
            dynamic.append(list(map(float, line)))
    dynamic.append([' ',' ',' '])
    return dynamic

def data_dynamic(t_dynamic):
    count, dis_sum, t_count, t_sum = 0, 0, 0, 0
    dis_dynamic, t_dy, t_val = [], [],[]
    for i in range(len(t_dynamic)-1):
        if t_dynamic[i][0] == t_dynamic[i+1][0]:
            count += 1
            t_count += 1
            dis_sum += t_dynamic[i][0]
            t_sum += t_dynamic[i][1]
            t_val.append(t_dynamic[i][0])
        elif t_dynamic[i][0] != t_dynamic[i+1][0]:
            dis_dynamic.append(dis_sum/count)
            t_dy.append([i, t_sum/t_count])
            count, dis_sum = 0, 0
            t_count, t_sum = 0, 0
    return dis_dynamic, t_dy, t_val
    
    
def plot( dis_dynamic, t_dy, t_val):
    
    plt.plot(dis_dynamic,label='dynamic  ' )
    plt.xlabel('round')
    plt.ylabel('average distance')
    plt.title("average fix and dynamix predefine")
    keep_len = 250
    plt.xlim(0,keep_len)
    plt.legend()
    plt.savefig('dis_dynamic.png')
    plt.show()

    t_val, avg_t = zip(*t_dy)
    plt.plot(avg_t,label='dynamic averge is' +str("%.3f"%float(sum(avg_t)/len(avg_t))))
    plt.xlabel('round')
    plt.ylabel('t_predefine')
    plt.title("average  dynamix predefine")
    plt.xlim(0,keep_len)
    plt.legend()
    plt.savefig('t_dynamic.png')
    plt.show()
    
    a, avg_t = zip(*t_dy)
    plt.plot(avg_t,label='dynamic averge is')
    plt.xlabel('round')
    plt.ylabel('t_predefine')
    plt.title("average  dynamix predefine")
    plt.xlim(0,keep_len)
    plt.legend()
    plt.savefig('t_dynamic.png')
    plt.show()
    plot_t = []
    for i in range(200):
        plot_t.append(t_val[i])

def read():
    t_dynamic = dynamic()
    dis_dynamic, t_dy, t_val = data_dynamic(t_dynamic)
    plot( dis_dynamic, t_dy, t_val)
read()
