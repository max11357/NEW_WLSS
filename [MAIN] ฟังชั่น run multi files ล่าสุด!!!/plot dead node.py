import csv
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np

def run():
    x, y = read_fix()
    plot(x, y)
 
def plot(x, y):
    plt.plot(x, y ,'ro')
    plt.axis([0, 100, 0, 100])
    plt.show()
   
def read_fix():
    point = []
    with open('dead point dmn '+str(0.1)+'.csv', 'r') as csvnew:
        read = csv.reader(csvnew)
        for line in read:
            point.append(line[:2])
    x, y = [], []
    for i in point:
        x.append(float(i[0]))
        y.append(float(i[1]))

    return x, y
run()
    
