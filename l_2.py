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
    return cch


def distance_candidate(cch, pkt_control, elec_tran, elec_rec, fs, mpf, d_threshold):
    cluster_member = []
    # print("cch : "+ str(len(cch)))
    for main in cch:
        distance = 0
        for other in cch:
            distance = math.sqrt((main[0] - other[0])**2 + (main[1] - other[1])**2)
            # print(distance)
            if main[0] != other[0] and main[1] != other[1]:
                if distance < d_threshold:  # nodes (tranfer nodes)
                    main[2] = main[2] - ((elec_tran+(fs*(distance**2)))*pkt_control)
                elif distance >= d_threshold:  # nodes (tranfer nodes)
                    main[2] = main[2] - ((elec_tran+(mpf*(distance**4)))*pkt_control)
                other[2] = other[2]-(elec_rec*pkt_control)
            if distance > 60 and other not in cluster_member:
                cluster_member.append(other)
        # print("*********************************")
    return cluster_member


def plot_graph(cluster_member, node_member, cch, station):
    # split 2d list to 1d *list* [use with graph only]
    node_x, node_y, energy_node = zip(*node_member)
    # PLOT
    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='datalim')
    for plot in cluster_member:
        plt.plot(plot[0], plot[1], '.', color='red', alpha=0.7)
        ax.add_patch(plt.Circle((plot[0], plot[1]), 30, alpha=0.17))
        # ax.annotate(text, (plot[0][0], plot[0][1]))
    plt.plot(node_x[0:], node_y[0:], '.', color='green', alpha=0.7)
    ax.plot()   # Causes an auto-scale update.
    plt.show()


def start():
    # Change Variables Here!!
    width = int(100) # meter
    height = int(100) # meter
    density = float(0.0125)
    t_predefine =  float(0.1)
    num_base = int(1)
    pos_base = "0,0"
    set_energy = int(3) # set energy = 1 Joule
    pkt_control = 200 # bit
    pkt_data = 4000  # bit
    elec_tran = 50 * (10 ** (-9))  # 50 nanoj
    elec_rec = 50 * (10 ** (-9))  # 50 nanoj
    fs = 10 * (10 ** (-12))  # 10 picoj
    mpf = 0.013 * (10 ** (-12))  # 0.013 picoj
    d_threshold = 87  # **********************

    station = \
        base_station(num_base, pos_base)

    node_member, len_nodes = \
        random_nodes(width, height, station, set_energy, density)

    cch = \
        random_cch(node_member, t_predefine, len_nodes)

    cluster_member = \
        distance_candidate(cch, pkt_control, elec_tran, elec_rec, fs, mpf, d_threshold)

    plot_graph(cluster_member, node_member, cch, station)

    # print("t=",t_predefine, "cch=",candidate , 'node=',len_nodes)


start()