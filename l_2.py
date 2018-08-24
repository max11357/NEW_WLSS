import random as rd
import math
import matplotlib.pyplot as plt

def change_variable():
    """variables"""
    candidate, data  = []
    candidate = math.ceil(t_predefine*  len_nodes)
    return candidate, data

def base_station(num_base, pos_base):
    """input base station point"""
    #Set POS base station here
    station = []
    for _ in range(num_base):
        station.append(map(int, pos_base.split(',')))
    # split 2d list to 1d *list* [use with graph only]
    base_x, base_y = zip(*station)
    return station, base_x, base_y

def random_nodes(width, height, station, set_energy):
    """random Nodes"""
    node_member = []
    len_nodes = math.ceil(density * (width * height)) 
    #Random nodes
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

def start():

    #Change Variables Here!!
    width = int(100)
    height = int(100)
    density = float(0.025)
    t_predefine float(0.1)
    num_base = int(1)
    pos_base = "0,0"
    set_energy = int(3)

    station, base_x, base_y = \
    base_station(num_base, pos_base)

    node_member, node_x, node_y, energy_node, len_nodes = \
    random_nodes(width, height, station, set_energy)



    #print("t=",t_predefine, "cch=",candidate , 'node=',len_nodes)

start()