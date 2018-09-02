import random as rd
import math
import matplotlib.pyplot as plt


def base_station(num_base, pos_base):
    """input base station point"""
    # Set POS base station here
    station = []
    for _ in range(num_base):
        station.append(map(int, pos_base.split(',')))
    return station


def random_nodes(width, height, station, set_energy, density):
    """random Nodes"""
    node_member = []
    len_nodes = math.ceil(density * (width * height)) 
    # Random nodes
    count = 0
    while len(node_member) != len_nodes:
        random_x, random_y = rd.randint(0, width), rd.randint(0, height)
        if [random_x, random_y] not in node_member and \
           [random_x, random_y] not in station:
            node_member.append([random_x, random_y, set_energy])
        count += 1
    print("amount nodes : " + str(len_nodes))
    print("****************************************")
    return node_member, len_nodes


def random_cch(node_member, t_predefine, len_nodes):
    """random Cluster from amount Node"""
    cch = []
    num_candidate = math.ceil(t_predefine*len_nodes)
    # random candidate cluster
    count = 0
    while len(cch) != num_candidate:
        c_cluster = node_member[rd.randint(0, len(node_member) - 1)]
        cch.append(c_cluster)
        node_member.remove(c_cluster)
        count += 1
    return cch, node_member


def distance_candidate(node_member, cch, pkt_control, elec_tran,\
                       elec_rec, fs, mpf, d_threshold, r1):
    # print("nodes BEFORE : "+str(len(node_member)))
    # print("cch : "+str(len(cch)))
    
    # Calculate all energy use to send pkt control
    for main in range(len(cch)):
        for other in range(len(cch)):
            distance = math.sqrt((cch[main][0] - cch[other][0])**2 + \
                                 (cch[main][1] - cch[other][1])**2)
            # Send pkt control
            if  distance < d_threshold:
                cch[main][2] = cch[main][2] - ((elec_tran+(fs*(distance**2)))*pkt_control)
            elif distance >= d_threshold :
                cch[main][2] = cch[main][2] - ((elec_tran+(mpf*(distance**4)))*pkt_control)
            # Receive pkt control
            cch[other][2] = cch[other][2] - (elec_rec*pkt_control)
    
    cluster_member = []
    dont_check = []
    # Choose who should be cluster member
    for main in range(len(cch)):
        log_dis = []
        main_cch =  cch[main]
        
        for other in range(len(cch)):
            distance = math.sqrt((cch[main][0] - cch[other][0])**2 + \
                                 (cch[main][1] - cch[other][1])**2)
            log_dis.append(distance)
        
        for c in range(len(log_dis)):
            if cch[c][:2] not in dont_check and log_dis[c] != 0:
                if log_dis[c] <= (r1*2):
                    if cch[c][2] > main_cch[2]:
                        dont_check.append(main_cch[:2])
                        main_cch = cch[c]
                    else:
                        dont_check.append(cch[c][:2])
        if main_cch not in cluster_member and main_cch[:2] not in dont_check:
            cluster_member.append(main_cch)
            dont_check.append(main_cch[:2])
    # append no use cch into node_member
    for b in cch:
        if b[:2] in dont_check and b not in cluster_member:
            node_member.append(b)
    # print("nodes AFTER : "+str(len(node_member)))
    # print("Cluster member : "+str(len(cluster_member)))
    return cluster_member, node_member
    

def plot_graph(cluster_member, node_member, cch, station, r2):
    # split 2d list to 1d *list* [use with graph only]
    node_x, node_y, energy_node = zip(*node_member)
    # PLOT
    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='datalim')
    plt.plot(node_x[0:], node_y[0:], '.', color='green', alpha=0.7)
    for plot in cluster_member:
        plt.plot(plot[0], plot[1], '.', color='red', alpha=0.7)
        ax.add_patch(plt.Circle((plot[0], plot[1]), r2, alpha=0.17))
        # ax.annotate(text, (plot[0][0], plot[0][1]))
    ax.plot()   # Causes an auto-scale update.
    plt.show()


def start():
    # Change Variables Here!!
    width = 100 # meter
    height = 100 # meter
    density = float(0.0125)
    t_predefine =  float(0.1)
    num_base = 1
    pos_base = "0,0"
    set_energy = 2 # set energy = 1 Joule
    pkt_control = 200 # bit
    pkt_data = 4000  # bit
    elec_tran = 50 * (10 ** (-9))  # 50 nanoj
    elec_rec = 50 * (10 ** (-9))  # 50 nanoj
    fs = 10 * (10 ** (-12))  # 10 picoj
    mpf = 0.012 * (10 ** (-12))  # 0.012 picoj
    d_threshold = 87  # **********************
    r1 = 30 # meter
    r2 = 80 # meter

    station = \
        base_station(num_base, pos_base)

    node_member, len_nodes = \
        random_nodes(width, height, station, set_energy, density)

    cch, node_member = \
        random_cch(node_member, t_predefine, len_nodes)


    cluster_member, node_member = \
        distance_candidate(node_member, cch, pkt_control, elec_tran, elec_rec, fs, mpf, d_threshold, r1)

    plot_graph(cluster_member, node_member, cch, station, r2)


start()