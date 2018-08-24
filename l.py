import random as rd
import math
import matplotlib.pyplot as plt

def variable(width, height, density, t_predefine):
    """variables"""
    node_member, candidate, station, data,  = [], [], [],[]
    len_nodes = math.ceil(density * (width * height))
    candidate = math.ceil(t_predefine*  len_nodes)
    print("t=",t_predefine, "cch=",candidate , 'node=',len_nodes)
    return node_member, candidate, station, data, len_nodes

def base_station(num_base, station):
    """input base station point"""
    for item in range(num_base):
        station.append(map(int, "0,0".split(',')))
    # split 2d list to 1d list
    base_x, base_y = zip(*station)
    return station, base_x, base_y

def random_node(node_member, len_nodes, width, height, station):
    """random Node"""
    count = 0
    while len(node_member) != len_nodes:
        random_x, random_y = rd.randint(0, width), rd.randint(0, height)
        if [random_x, random_y] not in node_member and \
           [random_x, random_y] not in station:
            node_member.append([random_x, random_y, 3])
        count += 1
    # split 2d list to 1d list
    node_x, node_y, energy_node = zip(*node_member)
    return node_member, node_x, node_y, energy_node

def random_candidate(candidate, node_member):
    """random Cluster from amount Node"""
    count = 0
    candidate_member = []
    while len(candidate_member) != candidate:
        cluster = node_member[rd.randint(0, len(node_member) - 1)]
        candidate_member.append(cluster)
        node_member.remove(cluster)
        count += 1
    # split 2d list to 1d list
    cluster_x, cluster_y, energy = zip(*candidate_member)
    return cluster_x, cluster_y, candidate_member

def distance_candidate(candidate, candidate_member, node_member):
    d_threshold = 87  
    pkt_control = 200
    elec_tran = 50 * (10 ** (-9))  # 50 nanoj
    elec_rec = 50 * (10 ** (-9))  # พลังงานตอนรับ 50 nanoj
    fs = 10 * (10 ** (-12))  # 10 picoj
    mpf = 0.013 * (10 ** (-12))  # 0.013 picoj
    fig, ax = plt.subplots()
    
    ax.set_aspect('equal', adjustable='datalim')
    cluster_member=[]
    for i in candidate_member:
        distance = 0
        for item in candidate_member:
            distance = math.sqrt((i[0] - item[0]) ** 2 +\
                                 (i[1] - item[1]) ** 2)
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

def start(width, height ,density, t_predefine, num_base):
    
    node_member, candidate, station, data, len_nodes\
                 = variable(width, height,density, t_predefine,)
    
    station, base_x, base_y \
             = base_station(num_base, station)
    
    random_node(node_member, len_nodes, width, height, station)
    
    cluster_x, cluster_y, candidate_member = \
               random_candidate( candidate, node_member)
    
    distance_candidate(candidate, candidate_member, node_member)
    
start(int(100), int(100),float(0.025), float(0.1) ,int(1))
