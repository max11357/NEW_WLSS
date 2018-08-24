import random as rd
import math
import matplotlib.pyplot as plt

def base_station(num_base, pos_base):
    """input base station point"""
    # Set POS base station here
    station = []
    for _ in range(num_base):
        station.append(map(int, pos_base.split(',')))
    # split 2d list to 1d *list* [use with graph only]
    base_x, base_y = zip(*station)
    return station, base_x, base_y

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
    # split 2d list to 1d *list* [use with graph only]
    node_x, node_y, energy_node = zip(*node_member)
    return node_member, node_x, node_y, energy_node, len_nodes

def random_cluster(node_member, t_predefine, len_nodes):
    """random Cluster from amount Node"""
    cluster_member = []
    num_candidate = math.ceil(t_predefine*len_nodes)
    # random candidate cluster
    count = 0
    while len(cluster_member) != num_candidate:
        cluster = node_member[rd.randint(0, len(node_member) - 1)]
        cluster_member.append(cluster)
        node_member.remove(cluster)
        count += 1
    # split 2d list to 1d *list* [use with graph only] 
    # [:2] ----> didn't use energy here
    cluster_x, cluster_y = zip(*cluster_member[:2])
    return cluster_x, cluster_y, cluster_member, num_candidate

def distance_candidate(num_candidate, cluster_member, node_member, pkt_control, elec_tran, elec_rec, fs, mpf):
    d_threshold = 87  # ********************** หาจากค่าเฉลี่ย ระยะทางทั้งหมด
    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='datalim')
    cluster_member=[]
    for i in cluster_member:
        distance = 0
        for item in cluster_member:
            distance = math.sqrt((i[0] - item[0])**2 + (i[1] - item[1])**2)
            if i[0] != item[0] and  i[1] != item[1]:
                if  distance < d_threshold :#nodes (tranfer nodes)
                    i[2] = i[2]-((elec_tran+(fs*(distance**2)))*pkt_control)
                elif distance >= d_threshold : #nodes (tranfer nodes)
                    i[2] = i[2]-((elec_tran+(mpf*(distance**4)))*pkt_control)
                item[2] = item[2]-(elec_rec*pkt_control)
            if distance > 60 and item not in cluster_member:
                cluster_member.append(item)
    for plot in cluster_member:
        plt.plot(plot[0], plot[1], '.',color='red', alpha=0.7)
        ax.add_patch(plt.Circle((plot[0], plot[1]), 30, alpha=0.17))
##        ax.annotate(text, (plot[0][0], plot[0][1]))
    node_x, node_y, energy_node = zip(*node_member)
    plt.plot(node_x[0:], node_y[0:], '.',color='green', alpha=0.7)
    ax.plot()   #Causes an autoscale update.
    plt.show()

def start():

    #Change Variables Here!!
    width = int(100) # meter
    height = int(100) # meter
    density = float(0.025) 
    t_predefine =  float(0.1)
    num_base = int(1)
    pos_base = "0,0"
    set_energy = int(3) # set energy = 1 Joule
    pkt_control = 200 # bit
    pkt_data = 1500000  # bit
    elec_tran = 50 * (10 ** (-9))  # 50 nanoj
    elec_rec = 50 * (10 ** (-9))  # 50 nanoj
    fs = 10 * (10 ** (-12))  # 10 picoj
    mpf = 0.013 * (10 ** (-12))  # 0.013 picoj


    station, base_x, base_y = \
    base_station(num_base, pos_base)

    node_member, node_x, node_y, energy_node, len_nodes = \
    random_nodes(width, height, station, set_energy, density)

    cluster_x, cluster_y, cluster_member, num_candidate = \
    random_cluster(node_member, t_predefine, len_nodes)



    #print("t=",t_predefine, "cch=",candidate , 'node=',len_nodes)

start()