from multiprocessing import pool
import random as rd
import math
import matplotlib.pyplot as plt
import csv
import time
import gc

def e_data_cluster(cluster_member, node_member, node_select, pkt_data, elec_tran,\
                    elec_rec, fs, mpf, d_threshold, dead):
    if dead == 0:
        # Cluster receive all pkt data from nodes_member
        for node in range(len(node_member)):
            if node_select[node][0] != -1 or node_select[node][1] != -1:
                # Send pkt data [node-->cluster]
                if  node_select[node][1] < d_threshold:
                    waste = ((elec_tran + (fs*(node_select[node][1]**2)))*pkt_data)
                    if node_member[node][2] - waste  > 0:
                        node_member[node][2] = node_member[node][2] - waste
                    else:
                        dead = 1
                elif node_select[node][1] >= d_threshold :
                    waste = ((elec_tran + (mpf*(node_select[node][1]**4)))*pkt_data)
                    if node_member[node][2] - waste  > 0:
                        node_member[node][2] = node_member[node][2] - waste
                    else:
                        dead = 1
                # Receive pkt data
                cluster_member[int(node_select[node][0])][2] = cluster_member[int(node_select[node][0])][2] - (elec_rec*pkt_data)

    
    return cluster_member, node_member, dead


def e_cluster_bs(cluster_member, station_member, pkt_data, elec_tran, elec_rec, fs, mpf, \
                  d_threshold, dead):
    if dead == 0:
        base_x, base_y = zip(*station_member)
        for cluster in cluster_member:
            distance = math.sqrt((int(base_x[0] - cluster[0])**2 +
                                (int(base_y[0] - cluster[1])**2)))
            # Send pkt data [clsuter-->bs]
            if  distance < d_threshold:
                waste = ((elec_tran + (fs*(distance**2)))*pkt_data)
                if cluster[2] - waste  > 0:
                    cluster[2] = cluster[2] - waste
                else:
                    dead = 1
            elif distance >= d_threshold :
                waste = ((elec_tran + (mpf*(distance**4)))*pkt_data)
                if cluster[2] - waste  > 0:
                    cluster[2] = cluster[2] - waste
                else:
                    dead = 1
    return cluster_member, station_member, dead


def plot_graph(cluster_member, node_member, station_member, r1, r2):
    # split 2d list to 1d *list* [use with graph only]
    node_x, node_y, energy_node, t_value = zip(*node_member)
    # PLOT
    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='datalim')
    # PLOT NODES DOT 
    plt.plot(node_x[0:], node_y[0:], '.', color='green', alpha=0.7)
    # PLOT CLUSTER DOT 
    for plot in cluster_member:
        plt.plot(plot[0], plot[1], '.', color='red', alpha=0.7)
        ax.add_patch(plt.Circle((plot[0], plot[1]), r1, alpha=0.17))
        ax.add_patch(plt.Circle((plot[0], plot[1]), r2, alpha=0.17, color="pink"))
        # ax.annotate(text, (plot[0][0], plot[0][1]))
    ax.plot()   # Causes an auto-scale update.
    plt.savefig("area.png")
    plt.close()
    plt.xlabel('distance')
    plt.title('distance between cluster and nodes sensor')
    # plt.hist(data_distance ,bins = [0,5,10,15,20,25,30,35,40,45,50])
    plt.savefig("distance.png")


def start(pkt_control, pkt_data, d_threshold, r1, r2):
    
    count_lap = 0
    ###############
    # Change Variables Here!!
    elec_tran = 50 * (10 ** (-9))  # 50 nanoj
    elec_rec = 50 * (10 ** (-9))  # 50 nanoj
    fs = 10 * (10 ** (-12))  # 10 picoj
    mpf = 0.012 * (10 ** (-12))  # 0.012 picoj

    

    station_member, node_member, cluster_member, node_select = [], [], [], []
    
    with open("station_member_sample.csv", 'r') as csvnew:
        read = csv.reader(csvnew)
        for line1 in read:
            station_member.append(list(map(int, line1)))
    with open("node_member_sample.csv", 'r') as csvnew:
        read = csv.reader(csvnew)
        for line2 in read:
            node_member.append(list(map(float, line2)))
    with open("cluster_member_sample.csv", 'r') as csvnew:
        read = csv.reader(csvnew)
        for line3 in read:
            cluster_member.append(list(map(float, line3)))
    with open("node_select_sample.csv", 'r') as csvnew:
        read = csv.reader(csvnew)
        for line4 in read:
            node_select.append(list(map(float, line4)))
    with open("lux_values_sample.csv", 'r') as lux_r:
        read = csv.reader(lux_r)
        for value in read:
            len_nodes = int(value[0])
            count_lap = int(value[1])
            dead = int(value[2])
            
    
            
    while dead == 0:
        
        c_data = []
        n_data = []
        for i in range(len(cluster_member)):
            c_data.append([count_lap, i, cluster_member[i]])
        for j in range(len(node_member)):
            n_data.append([count_lap, node_select[j][0], node_member[j]])
        with open('data 5-5 using way.csv', 'a', newline='') as csvnew:
            write = csv.writer(csvnew)
            for line1 in c_data:
                write.writerow(line1)
        with open('data 5-5 using way.csv', 'a', newline='') as csvnew:
            write = csv.writer(csvnew)
            for line2 in n_data:
                write.writerow(line2)
        

        cluster_member, node_member, dead = \
            e_data_cluster(cluster_member, node_member, node_select, \
            pkt_data, elec_tran, elec_rec, fs, mpf, d_threshold, dead)


        cluster_member, station_member, dead = \
            e_cluster_bs(cluster_member, station_member, pkt_data, \
            elec_tran, elec_rec, fs, mpf, d_threshold, dead)

        
        # plot_graph(cluster_member, node_member, station_member, \
        #     r1, r2)
        
        count_lap += 1
        if dead == 1:
            print("LAP : "+ str(count_lap))
            break         


