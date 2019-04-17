import random as rd
import math
import matplotlib.pyplot as plt
import csv
import operator


def pull_data():
    count = 1
    at1, at2, at3, at4, at5, at6 = [],[],[],[],[],[]
    at7, at8, at9, at10, at11, at12 = [],[],[],[],[],[]
    at13, at14, at15, at16, at17, at18, at19 = [],[],[],[],[],[],[]
    with open('place.csv', 'r', newline='') as csvnew:
        read = csv.reader(csvnew)
        for line in read:
            eval('at%d'% (count)).append(line)
            count += 1
    
    
    
    # at20 = []
    


    at_gap = [ [] for _ in range(19)]
    
    # 4608
    for num in range(1,20):
        cache2 = 0
        count2 = 0
        while cache2 != len(eval('at%d'% (num))[0]) - 1:
            old = float(eval('at%d'% (num))[0][cache2])
            new = float(eval('at%d'% (num))[0][cache2+1])
            diff = abs(((old - new) / old)*100)
            # print(diff)
            cache2 += 1
            if diff > 1:
                # print(diff)
                count2 += 1 
        at_gap[num-1].append(count2)
        print("-------------------------------")
    print(at_gap)

    # for cm in range(len(cm_original)):
    #     place = rd.randint(1, 19)
    #     print(eval('at%d'% (place)))
    #     print(" ")
    #     print(eval('at%d'% (place))[0][:6])
    #     print(" ")
        # cm_original[cm].append(eval('at%d'% (place))[0][:6])
    
pull_data()