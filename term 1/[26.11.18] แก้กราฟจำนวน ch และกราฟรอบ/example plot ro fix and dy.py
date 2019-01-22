import matplotlib.pyplot as plt
import numpy as np

def plot():
    a = [10.34, 9.92, 7.99, 6.57, 5.60, 4.75, 4.31, 3.62, 3.21]
    b = [10.54, 10.62, 10.69, 10.42, 10.81, 10.8, 10.72, 10.58, 10.52]
    x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    xi = [ i for i in x]
        
    line_1 = plt.plot(xi, a, marker='o',label='T fix')
    line_2 = plt.plot(xi, b, marker='o', label='T dynamic')
    plt.legend()
    plt.ylabel('percent of operation cluster size \n between 29-31 meter  ' )
    plt.xlabel('T')
    plt.show()
plot()
