import csv
import matplotlib.pyplot as plt
from math import log

def plot_data():
    for i in range(2,10):
        t_predefine = i/10
        data = []
        with open('data t '+str(t_predefine) +' and r0.csv', 'r') as csvnew:
            read = csv.reader(csvnew)
            for line1 in read:
                data.append(list(map(float, line1)))
        testList2 = [(elem2, elem1) for elem1, elem2 in data ]
        plt.plot(*zip(*testList2))
        plt.show()
##    with open('data t dynamic and r0.csv', 'r') as csvnew:
##            read = csv.reader(csvnew)
##            for line1 in read:
##                data.append(list(map(float, line1)))
##        testList2 = [(elem1, log(elem2)) for elem1, elem2 in data]
##        plt.scatter(*zip(*testList2))
##        plt.plot(*zip(*testList2))
##        plt.show()
plot_data()
