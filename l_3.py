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
            node_member.append([count, random_x, random_y, set_energy])
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
    return cch, node_member


def distance_candidate(node_member, cch, pkt_control, elec_tran,\
                       elec_rec, fs, mpf, d_threshold, r1):
    cluster_member = []
    cch.sort()
    print(cch)
    print("cch : "+ str(len(cch)))
    for main in cch:
        check_dis = []
        most_energy =  main # deafult is Receiver
        for other in cch:
            distance = math.sqrt((main[1] - other[1])**2 + (main[2] - other[2])**2)
            check_dis.append([other[0],distance])
            # Send pkt control
            if  distance < d_threshold:
                main[3] = main[3] - ((elec_tran+(fs*(distance**2)))*pkt_control)
            elif distance >= d_threshold :
                main[3] = main[3] - ((elec_tran+(mpf*(distance**4)))*pkt_control)
            # Receive pkt control
            other[3] = other[3] - (elec_rec*pkt_control)

        for i in range(len(check_dis)):
            print(check_dis[i])
        print(str(most_energy) + "  BEFORE")
        print("--")

        for i in range(len(check_dis)):
            # if check_dis[i][1] < 60 and check_dis[i][0] != most_energy[0]:
            #     print(str(most_energy[3]) + " & " + str(cch[i][3]))
            if check_dis[i][1] < 60 and \
               check_dis[i][0] != most_energy[0] and \
               cch[i][3] > most_energy[3]:
                most_energy = cch[i]
                
            elif check_dis[i][1] < 60 and \
                 check_dis[i][0] != most_energy[0] and \
                 cch[i][3] <= most_energy[3]:
                node_member.append(cch[i])
                cch.remove(cch[i])
        cluster_member.append(most_energy)
        cch.remove(most_energy)
        print(str(most_energy) + "  AFTER")
        print("*********************************")

        


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
    width = 100 # meter
    height = 100 # meter
    density = float(0.0125)
    t_predefine =  float(0.1)
    num_base = 1
    pos_base = "0,0"
    set_energy = 3 # set energy = 1 Joule
    pkt_control = 200 # bit
    pkt_data = 4000  # bit
    elec_tran = 50 * (10 ** (-9))  # 50 nanoj
    elec_rec = 50 * (10 ** (-9))  # 50 nanoj
    fs = 10 * (10 ** (-12))  # 10 picoj
    mpf = 0.013 * (10 ** (-12))  # 0.013 picoj
    d_threshold = 87  # **********************
    r1 = 30 # meter

    station = \
        base_station(num_base, pos_base)

    node_member, len_nodes = \
        random_nodes(width, height, station, set_energy, density)

    cch, node_member = \
        random_cch(node_member, t_predefine, len_nodes)


    distance_candidate(node_member, cch, pkt_control, elec_tran, elec_rec, fs, mpf, d_threshold, r1)

    # plot_graph(cluster_member, node_member, cch, station)


start()
