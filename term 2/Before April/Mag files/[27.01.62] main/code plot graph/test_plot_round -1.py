import csv
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np
 
def count_lap():
    count_1, dyn_1= [], []
    
    with open('count lap fix 0.1.csv', 'r') as csvnew:
        read = csv.reader(csvnew)
        for line in read:
            count_1.append(list(map(float, line))[1])
    with open('count lap dynamic 0.1.csv', 'r') as csvnew:
        read = csv.reader(csvnew)
        for line in read:
            dyn_1.append(list(map(float, line))[1])
    
    print(count_1)
    print(dyn_1)
    return count_1, dyn_1

def plot(count_1, dyn_1):
    fig = 2
    width = 0.25
    ind = np.arange(fig)
    
    lap_min = [min(count_1),min(dyn_1)]
    
    lap_mean = [mean(count_1),mean(dyn_1)]
    
    lap_max = [max(count_1),max(dyn_1)]
    
    
    bar_1 = plt.bar(ind, lap_max, width, label =' Maximum round')
    plt.plot()
    bar_2 = plt.bar(ind + width, lap_mean, width,  label =' Average round')
    bar_3 = plt.bar(ind + width + width, lap_min, width, label =' Minimum round')
    plt.xticks(ind + width , ('fix 0.1','dyn 0.1'), size=8)
    plt.ylabel('Rounds')
    plt.xlabel('Fix T_Value and Dynamic T_Value')
    plt.title("Rounds in Difference T_Predefine Value")
    for rect in bar_1 + bar_3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom', size=8)
    for rect_f in bar_2:
        height = rect_f.get_height()
        plt.text(rect_f.get_x() + rect_f.get_width()/2.0, height, '%.2f' % float(height), ha='center', va='bottom', size=8)

    plt.legend()
    plt.tight_layout()
    plt.show()

    x = [0.1]
    xi = [ i for i in x]
    
    
    
    plt.subplot(121)
    plt.ylim(0,1000)
    line1 = plt.plot(xi, lap_max[:1], marker='o', label='Maximum T Fix')
    line2 = plt.plot(xi, lap_mean[:1], marker='o', label='Average T Fix')
    line3 = plt.plot(xi, lap_min[:1], marker='o', label='Minimum T Fix')
    plt.ylabel('Rounds')
    plt.xlabel('Fix T_Value')
    plt.title("Rounds in Different T_Predefine Value")
    plt.legend()

    plt.subplot(122)
    plt.ylim(0,1000)
    line1 = plt.plot(xi, lap_max[1:], marker='o', label='Maximum T Dynamic')
    line2 = plt.plot(xi, lap_mean[1:], marker='o', label='Average T Dynamic')
    line3 = plt.plot(xi, lap_min[1:], marker='o', label='Minimum T Dynamic')
    plt.legend()
    plt.ylabel('Rounds')
    plt.xlabel('Dynamic T_Value')
    plt.show()

    plt.title("Average Rounds in Different T_Predefine Value")
    plt.ylim(0,1000)
    plt.plot(xi, lap_mean[:1], marker='o', label='Fix Average Rounds ')
    plt.plot(xi, lap_mean[1:], marker='o', label='Dynamic Average Rounds ')
    plt.legend()
    plt.ylabel('Rounds')
    plt.xlabel('T_Value')
    plt.show()
    
def run():
    count_1, dyn_1 = count_lap()
    plot(count_1, dyn_1)
run()
