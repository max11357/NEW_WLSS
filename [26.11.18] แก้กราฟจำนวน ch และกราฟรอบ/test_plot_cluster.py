import csv
from statistics import mean
import matplotlib.pyplot as plt


def count_lap():
    fix_1, fix_2, fix_3, fix_4, fix_5, fix_6, fix_7, fix_8, fix_9 = [], [], [], [], [], [], [], [], []
    dyn_1, dyn_2, dyn_3, dyn_4, dyn_5, dyn_6, dyn_7, dyn_8, dyn_9 = [], [], [], [], [], [], [], [], []
    for i in range(1,10):
        f = i/10
        with open('data cluster fix '+str(f)+'.csv', 'r', newline='') as csvnew:
            read = csv.reader(csvnew)
            for line in read:
                if f == 0.1:
                    fix_1.append(line)
                elif f == 0.2:
                    fix_2.append(line)
                elif f == 0.3:
                    fix_3.append(line)
                elif f == 0.4:
                    fix_4.append(line)
                elif f == 0.5:
                    fix_5.append(line)
                elif f == 0.6:
                    fix_6.append(line)
                elif f == 0.7:
                    fix_7.append(line)
                elif f == 0.8:
                    fix_8.append(line)
                elif f == 0.9:
                    fix_9.append(line)
        with open('data cluster dynamic '+str(f)+'.csv', 'r', newline='') as csvnew:
            read = csv.reader(csvnew)
            for line in read:
                if f == 0.1:
                    dyn_1.append(line)
                elif f == 0.2:
                    dyn_2.append(line)
                elif f == 0.3:
                    dyn_3.append(line)
                elif f == 0.4:
                    dyn_4.append(line)
                elif f == 0.5:
                    dyn_5.append(line)
                elif f == 0.6:
                    dyn_6.append(line)
                elif f == 0.7:
                    dyn_7.append(line)
                elif f == 0.8:
                    dyn_8.append(line)
                elif f == 0.9:
                    dyn_9.append(line)
    
    return fix_1, fix_2, fix_3, fix_4, fix_5, fix_6, fix_7, fix_8, fix_9, \
           dyn_1, dyn_2, dyn_3, dyn_4, dyn_5, dyn_6, dyn_7, dyn_8, dyn_9
    

def append_data_n_plot(len_cluster, f_d, num, max_list, mean_list, min_list):
    n = 100
    lists = [[] for _ in range(n)]
    at_list = 0
    check = 0
    for lc in range(len(len_cluster)):
        if int(len_cluster[lc][0]) == 1:
            if check == 0:
                check = 1
                lists[at_list].append(int(len_cluster[lc][1]))
            else:
                at_list += 1
                lists[at_list].append(int(len_cluster[lc][1]))
        elif int(len_cluster[lc][0]) != 1:
            if check == 1:
                lists[at_list].append(int(len_cluster[lc][1]))
    max_f = []
    mean_f = []
    min_f = []
    for i in range(len(lists)):
        max_f.append(max(lists[i]))
        mean_f.append(mean(lists[i]))
        min_f.append(min(lists[i]))

    plt.xlabel('Simulation')   
    plt.ylabel('Amount of Cluster')
    plt.title("Amount of Cluster in Difference Simulation at "+f_d+" 0."+str(num))
    plt.axis([1, 100, 0, max(max_f)+max(max_f)/4])
    X = range(1,101)
    plt.plot(X, max_f, color="red", label ='Maximum Cluster is '\
             +str("%.2f"%float(sum(max_f)/len(max_f))))
    max_list.append(float("%.2f"%float(sum(max_f)/len(max_f))))
    plt.plot(X, mean_f, color="green", label ='Average Cluster is '\
             +str("%.2f"%float(sum(mean_f)/len(mean_f))))
    mean_list.append(float("%.2f"%float(sum(mean_f)/len(mean_f))))
    plt.plot(X, min_f, color="blue", label ='Minimum Cluster is '\
             +str("%.2f"%float(sum(min_f)/len(min_f))))
    min_list.append(float("%.2f"%float(sum(min_f)/len(min_f))))
    plt.legend()
    plt.show()

    return max_list, mean_list, min_list

def run():
    
    fix_1, fix_2, fix_3, fix_4, fix_5, fix_6, fix_7, fix_8, fix_9, \
    dyn_1, dyn_2, dyn_3, dyn_4, dyn_5, dyn_6, dyn_7, dyn_8, dyn_9 = count_lap()
    
    fix = [fix_1, fix_2, fix_3, fix_4, fix_5, fix_6, fix_7, fix_8, fix_9]
    dyn = [dyn_1, dyn_2, dyn_3, dyn_4, dyn_5, dyn_6, dyn_7, dyn_8, dyn_9]
    max_list, mean_list, min_list = [],[],[]
    
    for i in range(len(fix)):
        append_data_n_plot(fix[i], 'fix', i+1, max_list, mean_list, min_list)
    for i in range(len(dyn)):
        append_data_n_plot(dyn[i], 'dnm', i+1, max_list, mean_list, min_list)
    x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    xi = [ i for i in x]

    plt.subplot(121)
    line1 = plt.plot(xi, min_list[0:9], marker='o', label='Minimum Cluster')
    line2 = plt.plot(xi, mean_list[0:9], marker='o', label='Average Cluster is')
    line3 = plt.plot(xi, max_list[0:9], marker='o',label='Maximum Cluster')
    plt.ylim(0,15)
    plt.legend()
    
    plt.subplot(122)
    line1 = plt.plot(xi, min_list[9:], marker='o', label='Minimum Cluster')
    line2 = plt.plot(xi, mean_list[9:], marker='o', label='Average Cluster is')
    line3 = plt.plot(xi, max_list[9:], marker='o',label='Maximum Cluster')
    plt.ylim(0,15)
    plt.legend()
    plt.show()

    plt.ylim(5,10)
    plt.plot(xi, mean_list[:9], marker='o', label='Fix Average Cluster ')
    plt.plot(xi, mean_list[9:], marker='o', label='Dynamic Average Cluster ')
    plt.legend()
    plt.show()
    
run()
