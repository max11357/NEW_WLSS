import random as rd
import math
import matplotlib.pyplot as plt
import csv


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


def random_nodes(width, height, station_member, set_energy, density):
    """random Nodes"""
    node_member = []
    len_nodes = math.ceil(density * (width * height)) 
    # Random nodes
    count = 0
    while len(node_member) != len_nodes:
        random_x, random_y = rd.randint(0, width), rd.randint(0, height)
        if [random_x, random_y] not in node_member and \
           [random_x, random_y] not in station_member:
            node_member.append([random_x, random_y, set_energy])
        count += 1
    node_member.sort()
    # append data to csv. file
        # append data to csv. file
    with open('node_member.csv', 'w', newline='') as csvnew:
        write = csv.writer(csvnew)
        for line1 in node_member:
            write.writerow(line1)
    with open("len_nodes.txt", "w") as text_file:
        text_file.write(str(len_nodes))
    print("amount nodes : " + str(len_nodes))
    print("****************************************")
    return node_member, len_nodes


def random_cch(node_member, t_predefine, len_nodes):
    """random cch from amount Node"""
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

    return cluster_member, node_member, dead


def nodes_select(cluster_member, node_member, pkt_control, elec_tran,\
                 elec_rec, fs, mpf, d_threshold, r2, data_distance, dead):
    data_distance = []
    log_select = []
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
            
            # print("SELECT!! "+str(shotest))
            # print("**************************************")
        ##    print("******************ดูค่าพลังงาน ณ node_select ***")
        ##    print("nodes : "+str(len(node_member)))
        ##    for i in node_member:print(i)

    return log_select, cluster_member, node_member, data_distance, dead


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
        base_x, base_y = zip(*station_member)
        for cluster in cluster_member:
            distance = math.sqrt((int(base_x[0] - cluster[0])**2 +
                                (int(base_y[0] - cluster[1])**2)))

            if  distance < d_threshold:
                wast = ((elec_tran+(fs*(distance**2)))*pkt_data)
                if cluster[2]-wast  > 0:
                    cluster[2] = cluster[2] -wast
                else:
                    break
            elif distance >= d_threshold :
                wast = ((elec_tran+(fs*(distance**4)))*pkt_data)
                if cluster[2]-wast  > 0:
                    cluster[2] = cluster[2] -wast
                else:
                    break
            cluster[2] = cluster[2] - ((elec_tran+(mpf*(distance**4)))*pkt_data)
            # Receive pkt control
        ##    for i in node_member:print(i)

    return cluster_member, node_member, dead


def back_to_nodes(cluster_member, node_member):
    """ before next loop all cluster switch back to node_member """
    for cluster in cluster_member:
        node_member.append(cluster)
    node_member.sort()
    cluster_member = []
##    print("****************** ALL back to nodes ***")
##    print("nodes : "+str(len(node_member)))

    return cluster_member, node_member


    
def plot_graph(cluster_member, node_member, cch, station_member, r1, r2, data_distance):
    # split 2d list to 1d *list* [use with graph only]
    node_x, node_y, energy_node = zip(*node_member)
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
    plt.hist(data_distance ,bins = [0,5,10,15,20,25,30,35,40,45,50])
    plt.savefig("distance.png")


def start():
    print("Choose 0 set new input")
    print("Choose 1 loop")
    choose = int(input("choose : "))

    # Change Variables Here!!
    width = 100 # meter
    height = 100 # meter
    density = float(0.0125)
    t_predefine =  float(0.2)
    num_base = 1
    pos_base = "0,0"
    set_energy = 0.5 # set energy = 1 Joule
    pkt_control = 200 # bit
    pkt_data = 4000  # bit
    elec_tran = 50 * (10 ** (-9))  # 50 nanoj
    elec_rec = 50 * (10 ** (-9))  # 50 nanoj
    fs = 10 * (10 ** (-12))  # 10 picoj
    mpf = 0.012 * (10 ** (-12))  # 0.012 picoj
    d_threshold = 87  # **********************
    r1 = 30 # meter
    r2 = 40 # meter

    if choose == 0:
        
        station_member = \
            base_station(num_base, pos_base)


        node_member, len_nodes = \
            random_nodes(width, height, station_member, set_energy, density)
        

        start()
    
    else:
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

            
            cch, node_member = \
                random_cch(node_member, t_predefine, len_nodes)
            

            cluster_member, node_member ,dead= \
                distance_candidate(node_member, cch, pkt_control, elec_tran,\
                                   elec_rec, fs, mpf, d_threshold, r1,dead)
  

            log_select, cluster_member, node_member, data_distance, dead= \
                nodes_select(cluster_member, node_member, pkt_control, \
                             elec_tran, elec_rec, fs, mpf, d_threshold,\
                             r2, data_distance , dead)


            cluster_member, node_member ,dead= \
                data_to_cluster(cluster_member, node_member, log_select, \
                                pkt_data, elec_tran, elec_rec, fs, mpf, \
                                d_threshold, station_member,dead)


            cluster_member, node_member = \
                back_to_nodes(cluster_member, node_member)

            count_lap += 1
            if dead == 1:
                print("LAP : "+ str(count_lap))
                for i in node_member:print(i)
                break;

        # plot_graph(cluster_member, node_member, cch, station_member, r1, r2, data_distance)


start()
