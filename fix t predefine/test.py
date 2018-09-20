import csv
import matplotlib.pyplot as plt

from math import log


def plot_data():
##    for i in range(2,10):
##        t_predefine = i/10
##        data = []
##        with open('data t '+str(t_predefine) +' and r0.csv', 'r') as csvnew:
##            read = csv.reader(csvnew)
##            for line1 in read:
##                data.append(list(map(float, line1)))
##        testList2 = [(float(elem1), float(elem2)) for elem1, elem2 in data ]
##        x,y = zip(*testList2)
##        plt.plot(x,label=str(t_predefine)+" "+ str(len(x)))
##        plt.xlabel('round')
##        plt.ylabel('max distance')
##        plt.title("fix predefine")
##        plt.legend()
    data = []
    with open('data t dynamic and r0.csv', 'r') as csvnew:
        read = csv.reader(csvnew)
        for line1 in read:
            data.append(list(map(float, line1)))
    testList2 = [(float(elem1), float(elem2)) for elem1, elem2 in data ]
    x,y = zip(*testList2)
    plt.plot(x,label='dynamic '+ str(len(x)))
    plt.xlabel('round')
    plt.ylabel('max distance')
    plt.title("fix predefine")
    plt.legend()
    plt.show()
plot_data()
