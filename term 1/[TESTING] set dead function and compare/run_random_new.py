from multiprocessing import pool
import random as rd
import math
import matplotlib.pyplot as plt
import csv
import time
import gc


def base_station(num_base, pos_base):
    """input base station point"""
    # Set POS base station here
    station_member_old = []
    for _ in range(num_base):
        station_member_old.append(list(map(int, pos_base.split(','))))
    # append data to csv. file
    with open('station_member_sample.csv', 'w', newline='') as csvnew:
        write = csv.writer(csvnew)
        for line in station_member_old:
            write.writerow(line)
    

    return station_member_old


def random_nodes(width, height, station_member_old, set_energy, density, t_predefine):
    """random Nodes"""
    # Random nodes
    node_member_old = []
    len_nodes = math.ceil(density * (width * height)) 
    count = 0
    while len(node_member_old) != len_nodes:
        random_x, random_y = rd.randint(0, width), rd.randint(0, height)
        if [random_x, random_y, set_energy, t_predefine] not in node_member_old and \
           [random_x, random_y, set_energy, t_predefine] not in station_member_old:
            node_member_old.append([random_x, random_y, set_energy, t_predefine])
        count += 1
    # append data to csv. file
    with open('node_member_sample.csv', 'w', newline='') as csvnew:
        write = csv.writer(csvnew)
        for line1 in node_member_old:
            write.writerow(line1)

    return node_member_old, len_nodes


def random_cch(node_member_old, len_nodes):
    """random cch from amount Node"""
    cch = []
    # random candidate cluster
    for node in node_member_old:
        prob_v = round(rd.uniform(0, 1), 1)
        if prob_v <= node[3]:
            cch.append(node)
    node_member = [i for i in node_member_old if i not in cch]
    
    if len(cch) == 0:
        random_cch(node_member, len_nodes)

    return cch, node_member


def e_distance_candidate(cch, pkt_control, elec_tran, elec_rec, fs, mpf, d_threshold, dead, r1):
    
    if dead == 0:
        # Calculate all energy use to send/Receive pkt control
        for main in range(len(cch)):
            for other in range(len(cch)):
                distance = math.sqrt((cch[main][0] - cch[other][0])**2 + \
                                (cch[main][1] - cch[other][1])**2)
                e_rx = elec_rec*pkt_control
                # Receive pkt control
                if distance <= r1:
                    if cch[other][2] - e_rx > 0:
                        cch[other][2] = cch[other][2] - e_rx
                    else:
                        dead = 0
            # Send pkt control
            if  r1 < d_threshold:
                e_tx = (elec_tran + (fs*(r1**2)))*pkt_control
                if cch[main][2] - e_tx > 0:
                    cch[main][2] = cch[main][2] - e_tx
                else:
                    dead = 1
            elif r1 >= d_threshold:
                e_tx = (elec_tran + (mpf*(r1**4)))*pkt_control
                if cch[main][2] - e_tx  > 0:
                    cch[main][2] = cch[main][2] - e_tx
                else:
                    dead = 1

    return dead, cch


def distance_candidate(cch, r1, node_member, dead):
    cluster_member = []
    dont_check = []
    cch_last = []
    if dead == 0:
        # sort by energy [from most to least]
        for lap in range(len(cch)-1,0,-1):
            for j in range(lap):
                if cch[j][2] < cch[j+1][2]:
                    temp = cch[j]
                    cch[j] = cch[j+1]
                    cch[j+1] = temp
        # Choose who should be cluster member
        for main in range(len(cch)):
            log_dis = []
            dont_check_in = []
            check = 0
            for other in range(len(cch)):
                distance = math.sqrt((cch[main][0] - cch[other][0])**2 + \
                                    (cch[main][1] - cch[other][1])**2)
                log_dis.append(distance)
            for c in range(len(log_dis)):
                if log_dis[c] <= r1 and log_dis[c] != 0:
                    if cch[main][2] >= cch[c][2]:
                        dont_check.append(cch[c][:2])
                        dont_check_in.append(cch[c][:2])
                    elif  cch[main][2] < cch[c][2] and cch[c][:2] not in dont_check:
                        check = 1
                        break
            if check == 1 and len(dont_check_in) > 0:
                for i in dont_check_in:
                    dont_check.remove(i)
            if cch[main] not in cluster_member and check == 0 :
                cluster_member.append(cch[main])
        # append no use cch into node_member
        for b in cch:
            if b not in cluster_member:
                node_member.append(b)
        cch_last = [i for i in cch if i not in node_member and i not in cluster_member]
    
    return cch_last, cluster_member, node_member, dead


def e_let_node_selected(cluster_member, node_member, pkt_control, elec_tran, elec_rec, fs, mpf, d_threshold, dead, r2):
    if dead == 0:
        # Calculate all energy use to send/Receive pkt control
        for cluster in range(len(cluster_member)):
            # Send pkt control
            if  r2 < d_threshold:
                e_tx = ((elec_tran + (fs*(r2**2)))*pkt_control)
                if cluster_member[cluster][2] - e_tx > 0 : 
                    cluster_member[cluster][2] = cluster_member[cluster][2] - e_tx
                else:
                    dead = 1
            elif r2 >= d_threshold :
                e_tx = ((elec_tran + (mpf*(r2**4)))*pkt_control)
                if cluster_member[cluster][2] - e_tx  > 0:
                    cluster_member[cluster][2] = cluster_member[cluster][2] - e_tx
                else:
                    dead = 1
            for node in range(len(node_member)):
                distance = math.sqrt((node_member[node][0] - cluster_member[cluster][0])**2 +
                                    (node_member[node][1] - cluster_member[cluster][1])**2)
                # Receive pkt control
                e_rx = elec_rec*pkt_control
                if distance <= r2:
                    if node_member[node][2] - e_rx > 0:
                        node_member[node][2] = node_member[node][2] - e_rx
                    else:
                        dead = 1

    # append data to csv. file
    with open('cluster_member_sample.csv', 'w', newline='') as csvnew:
        write = csv.writer(csvnew)
        for line1 in cluster_member:
            write.writerow(line1)
    with open('node_member_sample.csv', 'w', newline='') as csvnew:
        write = csv.writer(csvnew)
        for line3 in node_member:
            write.writerow(line3)

    return cluster_member, node_member, dead


def let_node_selected(cluster_member, node_member, r2, dead):
    max_dis = []
    node_select = []
    log_c_select = []
    cluster_select = []
    max_dis = []
    amount_n_with_c = {}
    count_ch_member = []
    data_distance = []

    for jj in range(len(cluster_member)):
        amount_n_with_c.update({jj:0})

    if dead == 0:
        # Cluster choose who's my member
        for node in range(len(node_member)):
            shotest = -1  # shortest distance
            what_cluster = -1  # what cluster?
            check = 0
            for cluster in range(len(cluster_member)):
                distance = math.sqrt((node_member[node][0] - cluster_member[cluster][0])**2 +
                                     (node_member[node][1] - cluster_member[cluster][1])**2)
                if distance <= r2:
                    if shotest is -1:
                        shotest = distance
                        what_cluster = cluster
                        check = 1
                    elif distance < shotest:
                        shotest = distance
                        what_cluster = cluster
                        check = 1
                    data_distance.append(shotest)
                elif distance > r2 and check == 0:
                    shotest = -1
                    what_cluster = -1
            node_select.append([what_cluster, shotest])
            log_c_select.append([what_cluster, shotest])
        
        #count amount of nodes of each cluster in dict
        for ff in amount_n_with_c:
            for jj in range(len(log_c_select)):
                if ff == log_c_select[jj][0]:
                    amount_n_with_c[ff] += 1
        
        # if cluster didn't have nodes family at all
        for ss in amount_n_with_c.keys():
            if amount_n_with_c[ss] == 0:
                node_select.append([ss, 0])
                log_c_select.append([ss, 0])
                # cluster_select.append([[ss, 0]])
        
        # collect maximum range of each cluster can get from they node member
        log_c_select = sorted(log_c_select, key=lambda cluster: cluster[0])
        
        log = []
        check_c = 0
        for j in log_c_select:
            if j[0] != -1 and j[0] == check_c:
                log.append(j)
            elif j[0] != -1 and j[0] != check_c:
                cluster_select.append(log)
                log = []
                log.append(j)
                check_c += 1
        cluster_select.append(log)
        
        for k in range(len(cluster_select)):
            log_max = max(b for (a, b) in cluster_select[k])
            max_dis.append([k, log_max])
        
        cluster_select.append('')
        for index in range(len(cluster_select)-1):
            count_ch_member.append(len(cluster_select[index]))

    # append data to csv. file
    with open('node_select_sample.csv', 'w', newline='') as csvnew:
        write = csv.writer(csvnew)
        for line1 in node_select:
            write.writerow(line1)
            
    return data_distance, node_select, max_dis, log_c_select, dead, cluster_select, amount_n_with_c, count_ch_member


def e_data_cluster(cluster_member, node_member, node_select, pkt_data, elec_tran,\
                    elec_rec, fs, mpf, d_threshold, dead):
    if dead == 0:
        # Cluster receive all pkt data from nodes_member
        for node in range(len(node_member)):
            if node_select[node][0] != -1 or node_select[node][1] != -1:
                # Send pkt data [node-->cluster]
                if  node_select[node][1] < d_threshold:
                    e_tx = ((elec_tran + (fs*(node_select[node][1]**2)))*pkt_data)
                    if node_member[node][2] - e_tx  > 0:
                        node_member[node][2] = node_member[node][2] - e_tx
                    else:
                        dead = 1
                elif node_select[node][1] >= d_threshold :
                    e_tx = ((elec_tran + (mpf*(node_select[node][1]**4)))*pkt_data)
                    if node_member[node][2] - e_tx  > 0:
                        node_member[node][2] = node_member[node][2] - e_tx
                    else:
                        dead = 1
                # Receive pkt data
                e_rx = elec_rec*pkt_data
                if cluster_member[node_select[node][0]][2] - e_rx > 0:
                    cluster_member[node_select[node][0]][2] = cluster_member[node_select[node][0]][2] - e_rx
                else:
                    dead = 1

    return cluster_member, node_member, dead


def e_cluster_bs(cluster_member, station_member_old, pkt_data, elec_tran, elec_rec, fs, mpf, \
                  d_threshold, dead, count_ch_member):
    if dead == 0:
        base_x, base_y = zip(*station_member_old)
        for member in range(len(count_ch_member)):
            e_agg = (count_ch_member[member]+1)*pkt_data* elec_tran
            cluster_member[member][2] -= e_agg
        for cluster in cluster_member:
            distance = math.sqrt((int(base_x[0] - cluster[0])**2 +
                                (int(base_y[0] - cluster[1])**2)))
            # Send pkt data [clsuter-->bs]
            if  distance < d_threshold:
                e_tx = ((elec_tran + (fs*(distance**2)))*pkt_data)
                if cluster[2] - e_tx  > 0:
                    cluster[2] = cluster[2] - e_tx
                else:
                    dead = 1
            elif distance >= d_threshold :
                e_tx = ((elec_tran + (mpf*(distance**4)))*pkt_data)
                if cluster[2] - e_tx  > 0:
                    cluster[2] = cluster[2] - e_tx
                else:
                    dead = 1

    return cluster_member, station_member_old, dead


def plot_graph(cluster_member, node_member, station_member_old, r1, r2):
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


def start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, d_threshold, r1, r2):
    
    count_lap = 0
    ###############
    # Change Variables Here!!
    t_predefine =  float(0.1)
    elec_tran = 50 * (10 ** (-9))  # 50 nanoj
    elec_rec = 50 * (10 ** (-9))  # 50 nanoj
    fs = 10 * (10 ** (-12))  # 10 picoj
    mpf = 0.012 * (10 ** (-12))  # 0.012 picoj


    dead = 0

    # collect bs in .csv
    station_member_old = \
        base_station(num_base, pos_base)

    # collect node member in .csv
    node_member_old, len_nodes = \
        random_nodes(width, height, station_member_old, set_energy, density, t_predefine)
    

    cch, node_member = \
        random_cch(node_member_old, len_nodes)
    

    dead, cch = \
        e_distance_candidate(cch, pkt_control, elec_tran, \
        elec_rec, fs, mpf, d_threshold, dead, r1)
    
    
    cch_last, cluster_member, node_member, dead = \
        distance_candidate(cch, r1, node_member, dead)
    
    # collect cluster_member, node_member in .csv
    cluster_member, node_member, dead = \
        e_let_node_selected(cluster_member, node_member, pkt_control, elec_tran, elec_rec, fs, mpf, d_threshold, dead, r2)
    
    
    data_distance, node_select, max_dis, log_c_select, dead, cluster_select, amount_n_with_c, count_ch_member = \
        let_node_selected(cluster_member, node_member, r2, dead)
    

    cluster_member, node_member, dead = \
        e_data_cluster(cluster_member, node_member, node_select, \
        pkt_data, elec_tran, elec_rec, fs, mpf, d_threshold, dead)


    cluster_member, station_member_old, dead = \
        e_cluster_bs(cluster_member, station_member_old, pkt_data, \
        elec_tran, elec_rec, fs, mpf, d_threshold, dead, count_ch_member)
    
    count_lap += 1 

    # collect len nodes, count lap and dead in .csv
    lux_values = [[len_nodes, count_lap, dead]]
    with open('lux_values_sample.csv', 'w', newline='') as lux_w:
        write = csv.writer(lux_w)
        for value in lux_values:
            write.writerow(value)

         


