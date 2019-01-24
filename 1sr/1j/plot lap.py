import csv
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np

def count_round():
    lap = []
    with open('count lap dynamic 0.1.csv', 'r') as csvnew:
        read = csv.reader(csvnew)
        for line in read:
            lap.append(list(map(float,line))[1])
    return lap

def plot(lap):
    plt.ylim(100,1000)
    line1 = plt.plot(lap, marker='o', label='super round is 1')
    plt.ylabel('Rounds')
    plt.xlabel('lap')
    plt.title('Rounds in Concept Super Round')
    plt.legend()
    plt.show()

def run():
    lap = count_round()
    plot(lap)
run()
            
