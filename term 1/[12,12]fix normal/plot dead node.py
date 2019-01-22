import csv
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np
from collections import Counter

def run():
    x, y , d, my_dict, dead= read_fix()
    plot(x, y, d, my_dict, dead)
 
def plot(x, y, d, my_dict, dead):
    plt.plot(x, y ,'ro')
    plt.axis([0, 100, 0, 100])
    plt.plot([-10], [50], 'go')
    plt.xlabel('width')
    plt.ylabel('height')
    plt.title('Dead node which Dynamic T = 0.9')
    for i, text in enumerate(dead):
        plt.text(x[i],y[i],text, fontsize=7)
##    plt.show()
    
    plt.bar(range(len(d)), list(d.values()), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
   
def read_fix():
    point, dead  = [], []
    with open('dead point dmn '+str(0.2)+'.csv', 'r') as csvnew:
        read = csv.reader(csvnew)
        for line in read:
            if len(dead)<50:
                point.append(line[:2])
                dead.append(line[4])
    my_dict = {k for k in dead}
    
    d = {text: dead.count(text) for text in dead}
    print(d)
    x, y = [], []
    for i in point:
        x.append(float(i[0]))
        y.append(float(i[1]))

    return x, y, d, my_dict, dead
run()
    
