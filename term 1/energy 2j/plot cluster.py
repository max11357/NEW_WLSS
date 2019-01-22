import csv
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np
 
def count_lap():
    count_1, count_2, count_3, count_4, count_5 = [], [], [], [],[]
    count_6, count_7, count_8, count_9 = [],[],[],[]
    dyn_1, dyn_2, dyn_3, dyn_4, dyn_5, = [],[],[],[],[]
    dyn_6, dyn_7, dyn_8, dyn_9 = [],[],[],[]
    count = []
    for i in range(1,10):
        f = i/10
        with open('data cluster fix'+str(f)+'.csv', 'r') as csvnew:
            read = csv.reader(csvnew)
            for line in read:
                if f == 0.1:
                    count_1.append(list(map(float, line[0:2])))
                elif f == 0.2:
                    count_2.append(list(map(float, line[0:2])))
                elif f == 0.3:
                    count_3.append(list(map(float, line[0:2])))
                elif f == 0.4:
                    count_4.append(list(map(float, line[0:2])))
                elif f == 0.5:
                    count_5.append(list(map(float, line[0:2])))
                elif f == 0.6:
                    count_6.append(list(map(float, line[0:2])))
                elif f == 0.7:
                    count_7.append(list(map(float, line[0:2])))
                elif f == 0.8:
                    count_8.append(list(map(float, line[0:2])))
                elif f == 0.9:
                    count_9.append(list(map(float, line[0:2])))
        with open('data cluster dynamic '+str(f)+'.csv', 'r') as csvnew:
            read = csv.reader(csvnew)
            for line in read:
                if f == 0.1:
                    dyn_1.append(list(map(float, line[0:2])))
                elif f == 0.2:
                    dyn_2.append(list(map(float, line[0:2])))
                elif f == 0.3:
                    dyn_3.append(list(map(float, line[0:2])))
                elif f == 0.4:
                    dyn_4.append(list(map(float, line[0:2])))
                elif f == 0.5:
                    dyn_5.append(list(map(float, line[0:2])))
                elif f == 0.6:
                    dyn_6.append(list(map(float, line[0:2])))
                elif f == 0.7:
                    dyn_7.append(list(map(float, line[0:2])))
                elif f == 0.8:
                    dyn_8.append(list(map(float, line[0:2])))
                elif f == 0.9:
                    dyn_9.append(list(map(float, line[0:2])))
    count_1.sort()
    count_2.sort()
    count_3.sort()
    count_4.sort()
    count_5.sort()
    count_6.sort()
    count_7.sort()
    count_8.sort()
    count_9.sort()
    count_1.append(['','',''])
    count_2.append(['','',''])
    count_3.append(['','',''])
    count_4.append(['','',''])
    count_5.append(['','',''])
    count_6.append(['','',''])
    count_7.append(['','',''])
    count_8.append(['','',''])
    count_9.append(['','',''])
    dyn_1.sort()
    dyn_2.sort()
    dyn_3.sort()
    dyn_4.sort()
    dyn_5.sort()
    dyn_6.sort()
    dyn_7.sort()
    dyn_8.sort()
    dyn_9.sort()
    dyn_1.append(['','',''])
    dyn_2.append(['','',''])
    dyn_3.append(['','',''])
    dyn_4.append(['','',''])
    dyn_5.append(['','',''])
    dyn_6.append(['','',''])
    dyn_7.append(['','',''])
    dyn_8.append(['','',''])
    dyn_9.append(['','',''])
    return count, count_1, count_2, count_3, count_4, count_5, count_6, count_7, count_8, count_9,\
           dyn_1, dyn_2, dyn_3, dyn_4, dyn_5, dyn_6, dyn_7, dyn_8, dyn_9

def dfix_1(count_1):
    count, r, avg_rfix1 = 0, 0, []
    for index in range(len(count_1)-1):
        if count_1[index][0] == count_1[index+1][0]:
            count += 1
            r += count_1[index][1]
        elif count_1[index][0] != count_1[index+1][0] and count != 0:
            avg_rfix1.append(r/count)
            count, r = 0, 0
    return avg_rfix1

def dfix_2(count_2):
    count, r, avg_rfix2 = 0, 0, []
    for index in range(len(count_2)-1):
        if count_2[index][0] == count_2[index+1][0]:
            count += 1
            r += count_2[index][1]
        elif count_2[index][0] != count_2[index+1][0] and count != 0:
            avg_rfix2.append(r/count)
            count, r = 0, 0
    return avg_rfix2

def dfix_3(count_3):
    count, r, avg_rfix3 = 0, 0, []
    for index in range(len(count_3)-1):
        if count_3[index][0] == count_3[index+1][0]:
            count += 1
            r += count_3[index][1]
        elif count_3[index][0] != count_3[index+1][0] and count != 0:
            avg_rfix3.append(r/count)
            count, r = 0, 0
    return avg_rfix3

def dfix_4(count_4):
    count, r, avg_rfix4 = 0, 0, []
    for index in range(len(count_4)-1):
        if count_4[index][0] == count_4[index+1][0]:
            count += 1
            r += count_4[index][1]
        elif count_4[index][0] != count_4[index+1][0] and count != 0:
            avg_rfix4.append(r/count)
            count, r = 0, 0
    return avg_rfix4

def dfix_5(count_5):
    count, r, avg_rfix5 = 0, 0, []
    for index in range(len(count_5)-1):
        if count_5[index][0] == count_5[index+1][0]:
            count += 1
            r += count_5[index][1]
        elif count_5[index][0] != count_5[index+1][0] and count != 0:
            avg_rfix5.append(r/count)
            count, r = 0, 0
    return avg_rfix5

def dfix_6(count_6):
    count, r, avg_rfix6 = 0, 0, []
    for index in range(len(count_6)-1):
        if count_6[index][0] == count_6[index+1][0]:
            count += 1
            r += count_6[index][1]
        elif count_6[index][0] != count_6[index+1][0] and count != 0:
            avg_rfix6.append(r/count)
            count, r = 0, 0
    return avg_rfix6

def dfix_7(count_7):
    count, r, avg_rfix7 = 0, 0, []
    for index in range(len(count_7)-1):
        if count_7[index][0] == count_7[index+1][0]:
            count += 1
            r += count_7[index][1]
        elif count_7[index][0] != count_7[index+1][0] and count != 0:
            avg_rfix7.append(r/count)
            count, r = 0, 0
    return avg_rfix7

def dfix_8(count_8):
    count, r, avg_rfix8 = 0, 0, []
    for index in range(len(count_8)-1):
        if count_8[index][0] == count_8[index+1][0]:
            count += 1
            r += count_8[index][1]
        elif count_8[index][0] != count_8[index+1][0] and count != 0:
            avg_rfix8.append(r/count)
            count, r = 0, 0
    return avg_rfix8

def dfix_9(count_9):
    count, r, avg_rfix9 = 0, 0, []
    for index in range(len(count_9)-1):
        if count_9[index][0] == count_9[index+1][0]:
            count += 1
            r += count_9[index][1]
        elif count_9[index][0] != count_9[index+1][0] and count != 0:
            avg_rfix9.append(r/count)
            count, r = 0, 0
    return avg_rfix9

def dynamic_1(dyn_1):
    count, r, avg_dyn1 = 0, 0, []
    for index in range(len(dyn_1)-1):
        if dyn_1[index][0] == dyn_1[index+1][0]:
            count += 1
            r += dyn_1[index][1]
        elif dyn_1[index][0] != dyn_1[index+1][0] and count != 0:
            avg_dyn1.append(r/count)
            count, r = 0, 0
    return avg_dyn1

def dynamic_2(dyn_2):
    count, r, avg_dyn2 = 0, 0, []
    for index in range(len(dyn_2)-1):
        if dyn_2[index][0] == dyn_2[index+1][0]:
            count += 1
            r += dyn_2[index][1]
        elif dyn_2[index][0] != dyn_2[index+1][0] and count != 0:
            avg_dyn2.append(r/count)
            count, r = 0, 0
    return avg_dyn2

def dynamic_3(dyn_3):
    count, r, avg_dyn3 = 0, 0, []
    for index in range(len(dyn_3)-1):
        if dyn_3[index][0] == dyn_3[index+1][0]:
            count += 1
            r += dyn_3[index][1]
        elif dyn_3[index][0] != dyn_3[index+1][0] and count != 0:
            avg_dyn3.append(r/count)
            count, r = 0, 0
    return avg_dyn3

def dynamic_4(dyn_4):
    count, r, avg_dyn4 = 0, 0, []
    for index in range(len(dyn_4)-1):
        if dyn_4[index][0] == dyn_4[index+1][0]:
            count += 1
            r += dyn_4[index][1]
        elif dyn_4[index][0] != dyn_4[index+1][0] and count != 0:
            avg_dyn4.append(r/count)
            count, r = 0, 0
    return avg_dyn4

def dynamic_5(dyn_5):
    count, r, avg_dyn5 = 0, 0, []
    for index in range(len(dyn_5)-1):
        if dyn_5[index][0] == dyn_5[index+1][0]:
            count += 1
            r += dyn_5[index][1]
        elif dyn_5[index][0] != dyn_5[index+1][0] and count != 0:
            avg_dyn5.append(r/count)
            count, r = 0, 0
    return avg_dyn5

def dynamic_6(dyn_6):
    count, r, avg_dyn6 = 0, 0, []
    for index in range(len(dyn_6)-1):
        if dyn_6[index][0] == dyn_6[index+1][0]:
            count += 1
            r += dyn_6[index][1]
        elif dyn_6[index][0] != dyn_6[index+1][0] and count != 0:
            avg_dyn6.append(r/count)
            count, r = 0, 0
    return avg_dyn6

def dynamic_7(dyn_7):
    count, r, avg_dyn7 = 0, 0, []
    for index in range(len(dyn_7)-1):
        if dyn_7[index][0] == dyn_7[index+1][0]:
            count += 1
            r += dyn_7[index][1]
        elif dyn_7[index][0] != dyn_7[index+1][0] and count != 0:
            avg_dyn7.append(r/count)
            count, r = 0, 0
    return avg_dyn7

def dynamic_8(dyn_8):
    count, r, avg_dyn8 = 0, 0, []
    for index in range(len(dyn_8)-1):
        if dyn_8[index][0] == dyn_8[index+1][0]:
            count += 1
            r += dyn_8[index][1]
        elif dyn_8[index][0] != dyn_8[index+1][0] and count != 0:
            avg_dyn8.append(r/count)
            count, r = 0, 0
    return avg_dyn8

def dynamic_9(dyn_9):
    count, r, avg_dyn9 = 0, 0, []
    for index in range(len(dyn_9)-1):
        if dyn_9[index][0] == dyn_9[index+1][0]:
            count += 1
            r += dyn_9[index][1]
        elif dyn_9[index][0] != dyn_9[index+1][0] and count != 0:
            avg_dyn9.append(r/count)
            count, r = 0, 0
    return avg_dyn9



def plot(avg_rfix1, avg_rfix2, avg_rfix3, avg_rfix4, avg_rfix5,\
         avg_rfix6, avg_rfix7, avg_rfix8, avg_rfix9,\
         avg_dyn1, avg_dyn2, avg_dyn3, avg_dyn4, avg_dyn5,\
         avg_dyn6, avg_dyn7, avg_dyn8, avg_dyn9):

##  all cluster till final round
    plt.plot(avg_rfix1, label =' fix t predefine at 0.1')
    plt.plot(avg_rfix2,label =' fix t predefine at 0.2')
    plt.plot(avg_rfix3, label =' fix t predefine at 0.3')
    plt.plot(avg_rfix4, label =' fix t predefine at 0.4')
    plt.plot(avg_rfix5, label =' fix t predefine at 0.5')
    plt.plot(avg_rfix6, label =' fix t predefine at 0.6')
    plt.plot(avg_rfix7, label =' fix t predefine at 0.7')
    plt.plot(avg_rfix8, label =' fix t predefine at 0.8')
    plt.plot(avg_rfix9, label =' fix t predefine at 0.9')
    plt.xlabel('round')
    plt.ylabel('number of cluster')
    plt.title("number of cluster in difference t_predefine value")
    plt.legend()
    plt.show()
    # plt.plot(avg_dyn1, label =' dynamic t predefine at 0.1')
    # plt.plot(avg_dyn2, label =' dynamic t predefine at 0.2')
    # plt.plot(avg_dyn3, label =' dynamic t predefine at 0.3')
    # plt.plot(avg_dyn4, label =' dynamic t predefine at 0.4')
    # plt.plot(avg_dyn5, label =' dynamic t predefine at 0.5')
    # plt.plot(avg_dyn6, label =' dynamic t predefine at 0.6')
    # plt.plot(avg_dyn7, label =' dynamic t predefine at 0.7')
    # plt.plot(avg_dyn8, label =' dynamic t predefine at 0.8')
    # plt.plot(avg_dyn9, label =' dynamic t predefine at 0.9')
    # plt.xlabel('round')
    # plt.ylabel('number of cluster')
    # plt.title("number of cluster in difference t_predefine value")
    # plt.legend()
    # plt.show()
#### just first ten round
##    plt.plot(avg_rfix1[:10], label =' fix t predefine at 0.1')
##    plt.plot(avg_rfix2[:10], label =' fix t predefine at 0.2')
##    plt.plot(avg_rfix3[:10], label =' fix t predefine at 0.3')
##    plt.plot(avg_rfix4[:10], label =' fix t predefine at 0.4')
##    plt.plot(avg_rfix5[:10], label =' fix t predefine at 0.5')
##    plt.plot(avg_rfix6[:10], label =' fix t predefine at 0.6')
##    plt.plot(avg_rfix7[:10], label =' fix t predefine at 0.7')
##    plt.plot(avg_rfix8[:10], label =' fix t predefine at 0.8')
##    plt.plot(avg_rfix9[:10], label =' fix t predefine at 0.9')
##    plt.plot(avg_dyn1[:10], label =' dynamic t predefine at 0.1')
##    plt.plot(avg_dyn2[:10], label =' dynamic t predefine at 0.2')
##    plt.plot(avg_dyn3[:10], label =' dynamic t predefine at 0.3')
##    plt.plot(avg_dyn4[:10], label =' dynamic t predefine at 0.4')
##    plt.plot(avg_dyn5[:10], label =' dynamic t predefine at 0.5')
##    plt.plot(avg_dyn6[:10], label =' dynamic t predefine at 0.6')
##    plt.plot(avg_dyn7[:10], label =' dynamic t predefine at 0.7')
##    plt.plot(avg_dyn8[:10], label =' dynamic t predefine at 0.8')
##    plt.plot(avg_dyn9[:10], label =' dynamic t predefine at 0.9')
##    plt.xlabel('')
##    plt.ylabel('number of cluster')
##    plt.title("number of cluster in difference t_predefine value in first 10 round")
##    plt.tight_layout()
##    plt.legend()
##    plt.show()
######  last 50 round
##    plt.plot(avg_rfix1[len(avg_rfix9)-30:], label =' fix t predefine at 0.1')
##    plt.plot(avg_rfix2[len(avg_rfix9)-30:], label =' fix t predefine at 0.2')
##    plt.plot(avg_rfix3[len(avg_rfix9)-30:], label =' fix t predefine at 0.3')
##    plt.plot(avg_rfix4[len(avg_rfix9)-30:], label =' fix t predefine at 0.4')
##    plt.plot(avg_rfix5[len(avg_rfix9)-30:], label =' fix t predefine at 0.5')
##    plt.plot(avg_rfix6[len(avg_rfix9)-30:], label =' fix t predefine at 0.6')
##    plt.plot(avg_rfix7[len(avg_rfix9)-30:], label =' fix t predefine at 0.7')
##    plt.plot(avg_rfix8[len(avg_rfix9)-30:], label =' fix t predefine at 0.8')
##    plt.plot(avg_rfix9[len(avg_rfix9)-30:], label =' fix t predefine at 0.9')
##    plt.plot(avg_dyn1[len(avg_rfix9)-30:], label =' dynamic t predefine at 0.1')
##    plt.plot(avg_dyn2[len(avg_rfix9)-30:], label =' dynamic t predefine at 0.2')
##    plt.plot(avg_dyn3[len(avg_rfix9)-30:], label =' dynamic t predefine at 0.3')
##    plt.plot(avg_dyn4[len(avg_rfix9)-30:], label =' dynamic t predefine at 0.4')
##    plt.plot(avg_dyn5[len(avg_rfix9)-30:], label =' dynamic t predefine at 0.5')
##    plt.plot(avg_dyn6[len(avg_rfix9)-30:], label =' dynamic t predefine at 0.6')
##    plt.plot(avg_dyn7[len(avg_rfix9)-30:], label =' dynamic t predefine at 0.7')
##    plt.plot(avg_dyn8[len(avg_rfix9)-30:], label =' dynamic t predefine at 0.8')
##    plt.plot(avg_dyn9[len(avg_rfix9)-30:], label =' dynamic t predefine at 0.9')
##    plt.xlabel('')
##    plt.ylabel('number of cluster')
##    plt.title("number of cluster in difference t_predefine value in first 10 round")
##    plt.tight_layout()
##    plt.legend()
##    plt.show()
##    plt.plot(avg_rfix9[len(avg_rfix9)-30:])
##    plt.show()
    

    
    fig = 18
    width = 0.25
    ind = np.arange(fig)
    first_round = [avg_rfix1[0],avg_rfix2[0],avg_rfix3[0],avg_rfix4[0],
               avg_rfix5[0],avg_rfix6[0],avg_rfix7[0],avg_rfix8[0],avg_rfix9[0],\
                   avg_dyn1[0], avg_dyn2[0], avg_dyn3[0], \
                   avg_dyn4[0], avg_dyn5[0], avg_dyn6[0],\
                   avg_dyn7[0], avg_dyn8[0], avg_dyn8[0]]

    max_round = [max(avg_rfix1),max(avg_rfix2),max(avg_rfix3),max(avg_rfix4),
               max(avg_rfix5),max(avg_rfix6),max(avg_rfix7),max(avg_rfix8),\
                   max(avg_rfix9),\
                 max(avg_dyn1), max(avg_dyn2), max(avg_dyn3),\
                 max(avg_dyn4), max(avg_dyn5), max(avg_dyn6),\
                 max(avg_dyn7), max(avg_dyn8), max(avg_dyn9)]

    min_round = [min(avg_rfix1),min(avg_rfix2),min(avg_rfix3),min(avg_rfix4),
               min(avg_rfix5),min(avg_rfix6),min(avg_rfix7),min(avg_rfix8),min(avg_rfix9),\
                 min(avg_dyn1), min(avg_dyn2), min(avg_dyn3),\
                 min(avg_dyn4), min(avg_dyn5), min(avg_dyn6),\
                 min(avg_dyn7), min(avg_dyn8), min(avg_dyn9)]

    mean_round = [mean(avg_rfix1),mean(avg_rfix2),mean(avg_rfix3),mean(avg_rfix4),
               mean(avg_rfix5),mean(avg_rfix6),mean(avg_rfix7),mean(avg_rfix8),mean(avg_rfix9),\
                  mean(avg_dyn1), mean(avg_dyn2), mean(avg_dyn3),\
                 mean(avg_dyn4), mean(avg_dyn5), mean(avg_dyn6),\
                 mean(avg_dyn7), mean(avg_dyn8), mean(avg_dyn9)]

    bar_1 = plt.bar(ind, max_round, width,  label =' maximum round')
    bar_3 = plt.bar(ind + width, mean_round, width, label =' average round')
    bar_4 = plt.bar(ind + width + width, min_round, width, label =' minimum round')
    plt.xticks(ind + width , ('fix 0.1', 'fix 0.2', 'fix 0.3', 'fix 0.4', 'fix 0.5', \
                                 'fix 0.6', 'fix 0.7', 'fix 0.8', 'fix 0.9',\
                                 'dyn 0.1', 'dyn 0.2', 'dyn 0.3', 'dyn 0.4', 'dyn 0.5', \
                                 'dyn 0.6', 'dyn 0.7', 'dyn 0.8', 'dyn 0.9'))
    for rect in bar_1+bar_3+bar_4:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')

    plt.xlabel('')
    plt.ylabel('number of cluster')
    plt.title("number of cluster in difference t_predefine value")
    plt.ylim(0,15)
    plt.tight_layout()
    plt.legend()
    plt.show()


def run():
    count, count_1, count_2, count_3, count_4, count_5, count_6, count_7, count_8, count_9,\
           dyn_1, dyn_2, dyn_3, dyn_4, dyn_5, dyn_6, dyn_7, dyn_8, dyn_9 = count_lap()
    avg_rfix1 = dfix_1(count_1)
    avg_rfix2 = dfix_2(count_2)
    avg_rfix3 = dfix_3(count_3)
    avg_rfix4 = dfix_4(count_4)
    avg_rfix5 = dfix_5(count_5)
    avg_rfix6 = dfix_6(count_6)
    avg_rfix7 = dfix_7(count_7)
    avg_rfix8 = dfix_8(count_8)
    avg_rfix9 = dfix_9(count_9)
    avg_dyn1 = dynamic_1(dyn_1)
    avg_dyn2 = dynamic_2(dyn_2)
    avg_dyn3 = dynamic_3(dyn_3)
    avg_dyn4 = dynamic_4(dyn_4)
    avg_dyn5 = dynamic_5(dyn_5)
    avg_dyn6 = dynamic_6(dyn_6)
    avg_dyn7 = dynamic_7(dyn_7)
    avg_dyn8 = dynamic_8(dyn_8)
    avg_dyn9 = dynamic_9(dyn_9)
    plot(avg_rfix1, avg_rfix3, avg_rfix3, avg_rfix4, avg_rfix5,\
         avg_rfix6, avg_rfix7, avg_rfix8, avg_rfix9,\
         avg_dyn1, avg_dyn2, avg_dyn3, avg_dyn4, avg_dyn5,\
         avg_dyn6, avg_dyn7, avg_dyn8, avg_dyn9)

run()     
