import random as rd
import math
import matplotlib.pyplot as plt
import csv

def set_t():
    "set t predefine at first of all node in area"
    t_predefine = 0.1
    return t_predefine

def base_station(num_base, pos_base):
    """input base station point"""
    # Set POS base station here
    station_member = []
    for _ in range(num_base):
        station_member.append(map(int, pos_base.split(',')))
    # append data to csv. file
    with open('station_member.csv', 'w', newline='') as csvnew:
        write = csv.writer(csvnew)
        for line in station_member:
            write.writerow(line)
    return station_member

def random_nodes(width, height, station_member, set_energy, density, t_predefine):
    """random Nodes"""
    node_member = []
    len_nodes = math.ceil(density * (width * height)) 
    # Random nodes
    count = 0
    while len(node_member) != len_nodes:
        random_x, random_y = rd.randint(0, width), rd.randint(0, height)
        if [random_x, random_y] not in node_member and \
           [random_x, random_y] not in station_member:
            node_member.append([random_x, random_y, set_energy, t_predefine])
        count += 1
    # append data to csv. file
        # append data to csv. file
    with open('node_member.csv', 'w', newline='') as csvnew:
        write = csv.writer(csvnew)
        for line1 in node_member:
            write.writerow(line1)
    with open("len_nodes.txt", "w") as text_file:
        text_file.write(str(len_nodes))
    print("amount nodes : " + str(len_nodes))
    return node_member, len_nodes

def random_cch(node_member, t_predefine, len_nodes):
    """random cch from amount Node"""
    cch = []
    for node in node_member:
        probvalue = rd.randrange(1,100)/100
        if probvalue <= t_predefine:
            cch.append(node)
            node_member.remove(node)
###################################################################################################
    if len(cch) == 0:# probvlue not work nothing in cch then random 1 number to be candidate
        candidate = rd.randrange(len(node_member))
        cch.append(node_member[candidate])
        node_member.remove(node_member[candidate])
    return cch, node_member

def distance_candidate(node_member, cch, pkt_control, elec_tran,\
                       elec_rec, fs, mpf, d_threshold, r1, dead):
    # print("nodes BEFORE : "+str(len(node_member)))
    # print("cch : "+str(len(cch)))
    cluster_member = []
    dont_check = []
    if dead == 0:
        # Calculate all energy use to send/Receive pkt control
        for main in range(len(cch)):
            for other in range(len(cch)):
                distance = math.sqrt((cch[main][0] - cch[other][0])**2 + \
                                    (cch[main][1] - cch[other][1])**2)
                # Send pkt control
                if  distance < d_threshold:
                    wast = (elec_tran+(fs*(distance**2)))*pkt_control
                    if cch[main][2]-wast > 0:
                        cch[main][2] = cch[main][2]-wast
                    else:
                        dead = 1
                elif distance >= d_threshold :
                    wast = ((elec_tran+(mpf*(distance**4)))*pkt_control)
                    if cch[main][2]-wast  > 0:
                        cch[main][2] = cch[main][2]-wast
                    else:
                        dead = 1
                # Receive pkt control
                cch[other][2] = cch[other][2] - (elec_rec*pkt_control)
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
                if log_dis[c] <= (r1*2) and log_dis[c] != 0:
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
        # print("nodes AFTER : "+str(len(node_member)))
        # print("Cluster member : "+str(len(cluster_member)))
    return cluster_member, node_member, dead

def nodes_select(cluster_member, node_member, pkt_control, elec_tran,\
                 elec_rec, fs, mpf, d_threshold, r2, data_distance, dead):
    data_distance = []
    log_select = []
    dis_r0 = []
    if dead == 0:
        # Calculate all energy use to send/Receive pkt control
        for node in range(len(node_member)):
            for cluster in range(len(cluster_member)):
                distance = math.sqrt((node_member[node][0] - cluster_member[cluster][0])**2 +
                                    (node_member[node][1] - cluster_member[cluster][1])**2)
                # Send pkt control
                if  distance < d_threshold:
                    wast = ((elec_tran+(fs*(distance**2)))*pkt_control)
                    if cluster_member[cluster][2]-wast > 0 : 
                        cluster_member[cluster][2] = cluster_member[cluster][2] - wast
                    else:
                        dead = 1
                elif distance >= d_threshold :
                    wast = ((elec_tran+(mpf*(distance**4)))*pkt_control)
                    if cluster_member[cluster][2]-wast  > 0:
                        cluster_member[cluster][2] = cluster_member[cluster][2] -wast
                    else:
                        dead = 1
                # Receive pkt control
                node_member[node][2] = node_member[node][2] - (elec_rec*pkt_control)
        # Choose who should be my cluster member
        cluster_member.sort()
        for node in range(len(node_member)):
            shotest = None  # shortest distance
            what_cluster = None  # what cluster?
            check = 0
            for cluster in range(len(cluster_member)):
                distance = math.sqrt((node_member[node][0] - cluster_member[cluster][0])**2 +
                                    (node_member[node][1] - cluster_member[cluster][1])**2)
                # print(str(node_member[node][:2])+" With : "+str(cluster)+" - "+str(distance))
                if distance <= r2:
                    if shotest is None:
                        shotest = distance
                        what_cluster = cluster
                        check = 1
                    elif distance < shotest:
                        shotest = distance
                        what_cluster = cluster
                        check = 1
                    data_distance.append(shotest)
                elif distance > r2 and check == 0:
                    shotest = None
                    what_cluster = None
            log_select.append([what_cluster, shotest])
            dis_r0.append([what_cluster, distance])
            # print("SELECT!! "+str(shotest))
            # print("**************************************")
        ##    print("******************ดูค่าพลังงาน ณ node_select ***")
        ##    print("nodes : "+str(len(node_member)))
        ##    for i in node_member:print(i)

    return log_select, cluster_member, node_member, data_distance, dead, dis_r0

def find_r0(dis_r0):
    dis_r0.sort()
    print(dis_r0)


def data_to_cluster(cluster_member, node_member, log_select, pkt_data, elec_tran,\
                 elec_rec, fs, mpf, d_threshold, station_member, dead):
    if dead == 0:
        # Cluster receive all pkt data from nodes_member
        for node in range(len(node_member)):
            if log_select[node][0] != None or log_select[node][1] != None:
                # Send pkt data [node-->cluster]
                if  log_select[node][1] < d_threshold:
                    wast = ((elec_tran+(fs*(log_select[node][1]**2)))*pkt_data)
                    if node_member[node][2]-wast  > 0:
                        node_member[node][2] = node_member[node][2] - wast
                    else:
                        dead = 1
                elif log_select[node][1] >= d_threshold :
                    wast = ((elec_tran+(mpf*(log_select[node][1]**4)))*pkt_data)
                    if node_member[node][2]-wast  > 0:
                        node_member[node][2] = node_member[node][2] - wast
                    else:
                        dead = 1
                # Receive pkt data
                cluster_member[log_select[node][0]][2] = cluster_member[log_select[node][0]][2] - (elec_rec*pkt_data)
        ##    print("******************ดูค่าพลังงาน ณ data_to_cluster ***")
        ##    print("nodes : "+str(len(node_member)))
        ##  wast energy's cluster send to base station
    if dead == 0:
        base_x, base_y = zip(*station_member)
        for cluster in cluster_member:
            distance = math.sqrt((int(base_x[0] - cluster[0])**2 +
                                (int(base_y[0] - cluster[1])**2)))

            if  distance < d_threshold:
                wast = ((elec_tran+(fs*(distance**2)))*pkt_data)
                if cluster[2]-wast  > 0:
                    cluster[2] = cluster[2] -wast
                else:
                    dead = 1
            elif distance >= d_threshold :
                wast = ((elec_tran+(mpf*(distance**4)))*pkt_data)
                if cluster[2]-wast  > 0:
                    cluster[2] = cluster[2] -wast
                else:
                    dead = 1
            # Receive pkt control
        ##    for i in node_member:print(i)

    return cluster_member, node_member, dead


def back_to_nodes(cluster_member, node_member):
    """ before next loop all cluster switch back to node_member """
    for cluster in cluster_member:
        node_member.append(cluster)
    cluster_member = []
##    print("****************** ALL back to nodes ***")
##    print("nodes : "+str(len(node_member)))

    return cluster_member, node_member


def start():
    print("Choose 0 set new input")
    print("Choose 1 loop")
    print("Choose 2 get 1 lap")
    choose = int(input("choose : "))

    # Change Variables Here!!
    width = 100 # meter
    height = 100 # meter
    density = float(0.0125)
    num_base = 1
    pos_base = "0,0"
    set_energy = 0.01 # set energy = 1 Joule
    pkt_control = 200 # bit
    pkt_data = 4000  # bit
    elec_tran = 50 * (10 ** (-9))  # 50 nanoj
    elec_rec = 50 * (10 ** (-9))  # 50 nanoj
    fs = 10 * (10 ** (-12))  # 10 picoj
    mpf = 0.012 * (10 ** (-12))  # 0.012 picoj
    d_threshold = 87  # **********************
    r1 = 30 # meter
    r2 = 30*2.1457 # meter root 2ln10

    if choose == 0:
        t_predefine = set_t()
        station_member = \
            base_station(num_base, pos_base)


        node_member, len_nodes = \
            random_nodes(width, height, station_member, set_energy, density, t_predefine)

        start()
    
    elif choose == 1:
        set_t()
        dead = 0
        count_lap = 0
        station_member, node_member, data_distance = [], [], []
        
        
        with open("station_member.csv", 'r') as csvnew:
            read = csv.reader(csvnew)
            for line1 in read:
                station_member.append(list(map(int, line1)))
        with open("node_member.csv", 'r') as csvnew:
            read = csv.reader(csvnew)
            for line2 in read:
                node_member.append(list(map(float, line2)))
        
        

        while True:
            
            with open("len_nodes.txt", "r") as text_file:
                len_nodes = int(text_file.read())

            
            t_predefine = set_t()
            cch, node_member = \
            random_cch(node_member, t_predefine, len_nodes)
            

            cluster_member, node_member ,dead= \
                distance_candidate(node_member, cch, pkt_control, elec_tran,\
                                   elec_rec, fs, mpf, d_threshold, r1,dead)
  

            log_select, cluster_member, node_member, data_distance, dead, dis_r0= \
                nodes_select(cluster_member, node_member, pkt_control, \
                             elec_tran, elec_rec, fs, mpf, d_threshold,\
                             r2, data_distance , dead)
            find_r0(dis_r0)


            cluster_member, node_member ,dead= \
                data_to_cluster(cluster_member, node_member, log_select, \
                                pkt_data, elec_tran, elec_rec, fs, mpf, \
                                d_threshold, station_member,dead)

            
            #plot_graph(cluster_member, node_member, cch, station_member, r1,r2,data_distance)


            cluster_member, node_member = \
                back_to_nodes(cluster_member, node_member)
            
            count_lap += 1
            if dead == 1:
                print("LAP : "+ str(count_lap))
                break;
    
    elif choose == 2:
        dead = 0
        count_lap = 0
        station_member, node_member, data_distance = [], [], []
        with open("station_member.csv", 'r') as csvnew:
            read = csv.reader(csvnew)
            for line1 in read:
                station_member.append(list(map(int, line1)))
        with open("node_member.csv", 'r') as csvnew:
            read = csv.reader(csvnew)
            for line2 in read:
                node_member.append(list(map(float, line2)))
        with open("len_nodes.txt", "r") as text_file:
                len_nodes = int(text_file.read())
        t_predefine = set_t()
        cch, node_member = \
            random_cch(node_member, t_predefine, len_nodes)
        

        cluster_member, node_member ,dead= \
            distance_candidate(node_member, cch, pkt_control, elec_tran,\
                                elec_rec, fs, mpf, d_threshold, r1,dead)


        log_select, cluster_member, node_member, data_distance, dead, dis_r0= \
            nodes_select(cluster_member, node_member, pkt_control, \
                            elec_tran, elec_rec, fs, mpf, d_threshold,\
                            r2, data_distance)
        find_r0(dis_r0)

        cluster_member, node_member ,dead= \
            data_to_cluster(cluster_member, node_member, log_select, \
                            pkt_data, elec_tran, elec_rec, fs, mpf, \
                            d_threshold, station_member,dead)

        
start()