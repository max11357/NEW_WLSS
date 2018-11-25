import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from statistics import mean

hundred_sim = {}
cache_main = []
with open('count lap fix 100 sim.csv', 'r') as csvnew:
    read = csv.reader(csvnew)
    for line in (read):
        cache_main.append(line)
    
    for j in range(len(cache_main)):
        cache = []
        s = 1
        for _ in range(int(len(cache_main[j])/2)):
            cache.append(cache_main[j][s])
            cache_map = list(map(int, cache))
            s += 2
        hundred_sim[j+1] = cache_map

min_hun = []
mean_hun = []
max_hun = []
for ik in hundred_sim:
    min_hun.append(min(hundred_sim.get(ik)))
    mean_hun.append(mean(hundred_sim.get(ik)))
    max_hun.append(max(hundred_sim.get(ik)))


plt.xlabel('Simulation')   
plt.ylabel('Round')
plt.title("Round in Difference Simulation")
plt.axis([1, 100, 0, max(max_hun)+max(max_hun)/4])


X = range(1,101)
plt.plot(X, min_hun, color="blue", label ='minimum round')
plt.plot(X, mean_hun, color="green", label ='average round')
plt.plot(X, max_hun, color="red", label ='maximum round')
plt.legend()
plt.show()

