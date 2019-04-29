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
    
    at_gap4608_2 = [ [] for _ in range(19)]
    at_gap4608_4 = [ [] for _ in range(19)]
    at_gap4608_6 = [ [] for _ in range(19)]
    at_gap2304_2 = [ [] for _ in range(19)]
    at_gap2304_4 = [ [] for _ in range(19)]
    at_gap2304_6 = [ [] for _ in range(19)]
    at_gap1152_2 = [ [] for _ in range(19)]
    at_gap1152_4 = [ [] for _ in range(19)]
    at_gap1152_6 = [ [] for _ in range(19)]
    
    # 4608
    for per in [2,4,6]:
        for num in range(1,20):
            cache2 = 0
            count2 = 0
            while cache2 != 4608 - 1:
                old = float(eval('at%d'% (num))[0][cache2])
                new = float(eval('at%d'% (num))[0][cache2+1])
                diff = abs(((old - new) / old)*100)
                # print(diff)
                cache2 += 1
                if diff > per:
                    # print(diff)
                    count2 += 1 
            eval('at_gap4608_%d'% (per))[num-1].append([num, (count2/len(eval('at%d'% (num))[0]))*100])
    
    # 4608/2 = 2304
    for per in [2,4,6]:
        for num in range(1,20):
            cache2 = 0
            count2 = 0
            while cache2 != 2304 - 1:
                old = float(eval('at%d'% (num))[0][cache2])
                new = float(eval('at%d'% (num))[0][cache2+1])
                diff = abs(((old - new) / old)*100)
                # print(diff)
                cache2 += 1
                if diff > per:
                    # print(diff)
                    count2 += 1 
            eval('at_gap2304_%d'% (per))[num-1].append([num, (count2/len(eval('at%d'% (num))[0]))*100])
    
    # 4608/4 = 1152
    for per in [2,4,6]:
        for num in range(1,20):
            cache2 = 0
            count2 = 0
            while cache2 != 1152 - 1:
                old = float(eval('at%d'% (num))[0][cache2])
                new = float(eval('at%d'% (num))[0][cache2+1])
                diff = abs(((old - new) / old)*100)
                # print(diff)
                cache2 += 1
                if diff > per:
                    # print(diff)
                    count2 += 1 
            eval('at_gap1152_%d'% (per))[num-1].append([num, (count2/len(eval('at%d'% (num))[0]))*100])
    
    with open('gaps.txt', 'w') as f:
        f.write("data:4608 gap:2% \n")
        for item1 in at_gap4608_2:
            f.write("at")
            f.write("%s" % item1[0][0])
            f.write(" %.2f" % item1[0][1])
            f.write(" %\n")
        f.write("data:2304 gap:2% \n")
        for item2 in at_gap2304_2:
            f.write("at")
            f.write("%s" % item2[0][0])
            f.write(" %.2f" % item2[0][1])
            f.write(" %\n")
        f.write("data:1152 gap:2% \n")
        for item3 in at_gap1152_2:
            f.write("at")
            f.write("%s" % item3[0][0])
            f.write(" %.2f" % item3[0][1])
            f.write(" %\n")
        f.write("-------------------------------------- \n")
        
        f.write("data:4608 gap:4% \n")
        for item4 in at_gap4608_2:
            f.write("at")
            f.write("%s" % item4[0][0])
            f.write(" %.2f" % item4[0][1])
            f.write(" %\n")
        f.write("data:2304 gap:4% \n")
        for item5 in at_gap2304_2:
            f.write("at")
            f.write("%s" % item5[0][0])
            f.write(" %.2f" % item5[0][1])
            f.write(" %\n")
        f.write("data:1152 gap:4% \n")
        for item6 in at_gap1152_2:
            f.write("at")
            f.write("%s" % item6[0][0])
            f.write(" %.2f" % item6[0][1])
            f.write(" %\n")
        f.write("-------------------------------------- \n")

        f.write("data:4608 gap:6% \n")
        for item7 in at_gap4608_2:
            f.write("at")
            f.write("%s" % item7[0][0])
            f.write(" %.2f" % item7[0][1])
            f.write(" %\n")
        f.write("data:2304 gap:6% \n")
        for item8 in at_gap2304_2:
            f.write("at")
            f.write("%s" % item8[0][0])
            f.write(" %.2f" % item8[0][1])
            f.write(" %\n")
        f.write("data:1152 gap:6% \n")
        for item9 in at_gap1152_2:
            f.write("at")
            f.write("%s" % item9[0][0])
            f.write(" %.2f" % item9[0][1])
            f.write(" %\n")
        f.write("-------------------------------------- \n")

    # print("data:4608 gap:2%")
    # for i in at_gap4608_2:
    #     print("at",i[0][0],"%.2f" % i[0][1], "%")
    # print("data:2304 gap:2%")
    # for i in at_gap2304_2:
    #     print("at",i[0][0],"%.2f" % i[0][1], "%")
    # print("data:1152 gap:2%")
    # for i in at_gap1152_2:
    #     print("at",i[0][0],"%.2f" % i[0][1], "%")
    
    # print("--------------------------------------")
    
    # print("data:4608 gap:2%")
    # for i in at_gap4608_4:
    #     print("at",i[0][0],"%.2f" % i[0][1], "%")
    # print("data:2304 gap:4%")
    # for i in at_gap2304_4:
    #     print("at",i[0][0],"%.2f" % i[0][1], "%")
    # print("data:1152 gap:4%")
    # for i in at_gap1152_4:
    #     print("at",i[0][0],"%.2f" % i[0][1], "%")
    # print("--------------------------------------")

    # print("data:4608 gap:6%")
    # for i in at_gap4608_6:
    #     print("at",i[0][0],"%.2f" % i[0][1], "%")
    # print("data:2304 gap:6%")
    # for i in at_gap2304_6:
    #     print("at",i[0][0],"%.2f" % i[0][1], "%")
    # print("data:1152 gap:6%")
    # for i in at_gap1152_6:
    #     print("at",i[0][0],"%.2f" % i[0][1], "%")
    # print("--------------------------------------")

    # for cm in range(len(cm_original)):
    #     place = rd.randint(1, 19)
    #     print(eval('at%d'% (place)))
    #     print(" ")
    #     print(eval('at%d'% (place))[0][:6])
    #     print(" ")
        # cm_original[cm].append(eval('at%d'% (place))[0][:6])
    
pull_data()
