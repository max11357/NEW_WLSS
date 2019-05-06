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
    
    # # 4608
    for per in [2,4,6]:
        for num in range(1,20):
            cache2 = 0
            count2 = 0
            while cache2 < 4608 - 1:
                old = float(eval('at%d'% (num))[0][cache2])
                new = float(eval('at%d'% (num))[0][cache2+1])
                diff = abs(old - new) / ((old+new)/2)*100
                # print(diff)
                cache2 += 1
                if diff > per:
                    # print(diff)
                    count2 += 1 
            eval('at_gap4608_%d'% (per))[num-1].append([num, count2, (count2/4608)*100])

    # 4608/2 = 2304
    for per in [2,4,6]:
        for num in range(1,20):
            cache2 = 0
            count2 = 0
            while cache2 < 2304 - 1:
                old = float(eval('at%d'% (num))[0][cache2])
                new = float(eval('at%d'% (num))[0][cache2+1])
                diff = abs(old - new) / ((old+new)/2)*100
                # print(diff)
                cache2 += 1
                if diff > per:
                    # print(diff)
                    count2 += 1 
            eval('at_gap2304_%d'% (per))[num-1].append([num, count2, (count2/2304)*100])

    # 4608/4 = 1152
    for per in [2,4,6]:
        for num in range(1,20):
            cache2 = 0
            count2 = 0
            while cache2 < 1152 - 1:
                old = float(eval('at%d'% (num))[0][cache2])
                new = float(eval('at%d'% (num))[0][cache2+1])
                diff = abs(old - new) / ((old+new)/2)*100
                # print(diff)
                cache2 += 1
                if diff > per:
                    # print(diff)
                    count2 += 1 
            eval('at_gap1152_%d'% (per))[num-1].append([num, count2, (count2/1152)*100])

    with open('atN.txt', 'w') as f:
        f.write("data:4608 gap:2% ****\n")
        for item1 in at_gap4608_2:
            f.write("at")
            f.write("%s" % item1[0][0])
            f.write(",")
            f.write(" %d" % item1[0][1])
            f.write(",")
            f.write(" %.2f" % item1[0][2])
            f.write(" %\n")
        f.write("data:2304 gap:2% ****\n")
        for item2 in at_gap2304_2:
            f.write("at")
            f.write("%s" % item2[0][0])
            f.write(",")
            f.write(" %d" % item2[0][1])
            f.write(",")
            f.write(" %.2f" % item2[0][2])
            f.write(" %\n")
        f.write("data:1152 gap:2% ****\n")
        for item3 in at_gap1152_2:
            f.write("at")
            f.write("%s" % item3[0][0])
            f.write(",")
            f.write(" %d" % item3[0][1])
            f.write(",")
            f.write(" %.2f" % item3[0][2])
            f.write(" %\n")
        f.write("-------------------------------------- \n")
        
        f.write("data:4608 gap:4% ****\n")
        for item4 in at_gap4608_4:
            f.write("at")
            f.write("%s" % item4[0][0])
            f.write(",")
            f.write(" %d" % item4[0][1])
            f.write(",")
            f.write(" %.2f" % item4[0][2])
            f.write(" %\n")
        f.write("data:2304 gap:4% ****\n")
        for item5 in at_gap2304_4:
            f.write("at")
            f.write("%s" % item5[0][0])
            f.write(",")
            f.write(" %d" % item5[0][1])
            f.write(",")
            f.write(" %.2f" % item5[0][2])
            f.write(" %\n")
        f.write("data:1152 gap:4% ****\n")
        for item6 in at_gap1152_4:
            f.write("at")
            f.write("%s" % item6[0][0])
            f.write(",")
            f.write(" %d" % item6[0][1])
            f.write(",")
            f.write(" %.2f" % item6[0][2])
            f.write(" %\n")
        f.write("-------------------------------------- \n")

        f.write("data:4608 gap:6% ****\n")
        for item7 in at_gap4608_6:
            f.write("at")
            f.write("%s" % item7[0][0])
            f.write(",")
            f.write(" %d" % item7[0][1])
            f.write(",")
            f.write(" %.2f" % item7[0][2])
            f.write(" %\n")
        f.write("data:2304 gap:6% ****\n")
        for item8 in at_gap2304_6:
            f.write("at")
            f.write("%s" % item8[0][0])
            f.write(",")
            f.write(" %d" % item8[0][1])
            f.write(",")
            f.write(" %.2f" % item8[0][2])
            f.write(" %\n")
        f.write("data:1152 gap:6% ****\n")
        for item9 in at_gap1152_6:
            f.write("at")
            f.write("%s" % item9[0][0])
            f.write(",")
            f.write(" %d" % item9[0][1])
            f.write(",")
            f.write(" %.2f" % item9[0][2])
            f.write(" %\n")
        f.write("-------------------------------------- \n")
        
        # ------------------------------------------------------------------------------------------------- #

        #  874       4372     8820      11993     8223      12165     10123
        ss_temp6, ss_temp5, ss_temp4, ss_temp3, ss_temp2, ss_temp1, ss_temp12 = [], [], [], [], [], [], []
        # ss_light6, ss_light5, ss_light4, ss_light3, ss_light2, ss_light1, ss_light12 = [], [], [], [], [], [], []
        # ss_humid6, ss_humid5, ss_humid4, ss_humid3, ss_humid2, ss_humid1, ss_humid12 = [], [], [], [], [], [], []

        # with open('Sensor_temp_light_humidity.csv', 'r', newline='') as csvnew:
        #     read = csv.reader(csvnew)
        #     for line in read:
        #         if line[0] != '๏ปฟtimestamp' and line[0][1] == '/':
        #             # print(int(line[0][0]))
        #             eval('ss_temp%d' % (int(line[0][0]))).append(line[1])
        #         elif line[0] != '๏ปฟtimestamp' and line[0][1] != '/':
        #             # print(int(line[0][:2]))
        #             eval('ss_temp%d' % (int(line[0][:2]))).append(line[1])
        
        # max
        ss_temp_2 = [ [] for _ in range(7)]
        ss_temp_4 = [ [] for _ in range(7)]
        ss_temp_6 = [ [] for _ in range(7)]
        print("MAX ###################")
        for per in [2,4,6]:
            for num, value in {0:6, 1:5, 2:4, 3:3, 4:2, 5:1, 6:12}.items():
                cache2 = 0
                count2 = 0
                while cache2 != len(eval('ss_temp%d' % (value))) - 1:
                    old = float(eval('ss_temp%d'% (value))[cache2])
                    new = float(eval('ss_temp%d'% (value))[cache2+1])
                    diff = abs(old - new) / ((old+new)/2)*100
                    # print(diff)
                    cache2 += 1
                    if diff > per:
                        # print(diff)
                        count2 += 1 
                eval('ss_temp_%d'% (per))[num].append([value, (count2/len(eval('ss_temp%d'% (value))))*100])
            print(per, "*****")
            for i in eval('ss_temp_%d'% (per)):
                print(i)
        print("____________________________________________")

        # 800
        ss_temp800_2 = [ [] for _ in range(7)]
        ss_temp800_4 = [ [] for _ in range(7)]
        ss_temp800_6 = [ [] for _ in range(7)]
        print(800,"###################")
        for per in [2,4,6]:
            for num, value in {0:6, 1:5, 2:4, 3:3, 4:2, 5:1, 6:12}.items():
                cache2 = 0
                count2 = 0
                while cache2 != 800 - 1:
                    old = float(eval('ss_temp%d'% (value))[cache2])
                    new = float(eval('ss_temp%d'% (value))[cache2+1])
                    diff = abs(old - new) / ((old+new)/2)*100
                    # print(diff)
                    cache2 += 1
                    if diff > per:
                        # print(diff)
                        count2 += 1 
                eval('ss_temp800_%d'% (per))[num].append([value, (count2/800)*100])
            print(per, "*****")
            for i in eval('ss_temp800_%d'% (per)):
                print(i)
        print("____________________________________________")

        # 4000
        ss_temp4000_2 = [ [] for _ in range(6)]
        ss_temp4000_4 = [ [] for _ in range(6)]
        ss_temp4000_6 = [ [] for _ in range(6)]
        print(4000,"##################")
        for per in [2,4,6]:
            for num, value in {0:5, 1:4, 2:3, 3:2, 4:1, 5:12}.items():
                cache2 = 0
                count2 = 0
                while cache2 != 4000 - 1:
                    old = float(eval('ss_temp%d'% (value))[cache2])
                    new = float(eval('ss_temp%d'% (value))[cache2+1])
                    diff = abs(old - new) / ((old+new)/2)*100
                    # print(diff)
                    cache2 += 1
                    if diff > per:
                        # print(diff)
                        count2 += 1 
                eval('ss_temp4000_%d'% (per))[num].append([value, (count2/4000)*100])
            print(per, "*****")
            for i in eval('ss_temp4000_%d'% (per)):
                print(i)
        print("____________________________________________")

        # 8000
        ss_temp8000_2 = [ [] for _ in range(5)]
        ss_temp8000_4 = [ [] for _ in range(5)]
        ss_temp8000_6 = [ [] for _ in range(5)]
        print(8000,"##################")
        for per in [2,4,6]:
            for num, value in {0:4, 1:3, 2:2, 3:1, 4:12}.items():
                cache2 = 0
                count2 = 0
                while cache2 != 8000 - 1:
                    old = float(eval('ss_temp%d'% (value))[cache2])
                    new = float(eval('ss_temp%d'% (value))[cache2+1])
                    diff = abs(old - new) / ((old+new)/2)*100
                    # print(diff)
                    cache2 += 1
                    if diff > per:
                        # print(diff)
                        count2 += 1 
                eval('ss_temp8000_%d'% (per))[num].append([value, (count2/8000)*100])
            print(per, "*****")
            for i in eval('ss_temp8000_%d'% (per)):
                print(i)
        print("____________________________________________")
        
        # 10000
        ss_temp10000_2 = [ [] for _ in range(3)]
        ss_temp10000_4 = [ [] for _ in range(3)]
        ss_temp10000_6 = [ [] for _ in range(3)]
        print(10000,"##################")
        for per in [2,4,6]:
            for num, value in {0:3, 1:1, 2:12}.items():
                cache2 = 0
                count2 = 0
                while cache2 != 10000 - 1:
                    old = float(eval('ss_temp%d'% (value))[cache2])
                    new = float(eval('ss_temp%d'% (value))[cache2+1])
                    diff = abs(old - new) / ((old+new)/2)*100
                    # print(diff)
                    cache2 += 1
                    if diff > per:
                        # print(diff)
                        count2 += 1 
                eval('ss_temp10000_%d'% (per))[num].append([value, (count2/10000)*100])
            print(per, "*****")
            for i in eval('ss_temp10000_%d'% (per)):
                print(i)
        print("____________________________________________")

pull_data()
