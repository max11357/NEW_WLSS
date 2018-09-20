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

    return node_member, len_nodes


def random_cch(node_member, len_nodes):
    """random cch from amount Node"""
    cch = []
    # random candidate cluster
    while len(cch) == 0:
        for node in node_member:
            prob_v = round(rd.uniform(0, 1), 1)
            if prob_v <= node[3]:
                cch.append(node)
                node_member.remove(node)

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
##        for b in cch:
##            if b not in cluster_member:
##                node_member.append(b)
##        print("nodes AFTER : "+str(len(node_member)))
##        print("Cluster member : "+str(len(cluster_member))) 

    return cluster_member, node_member, dead


def nodes_select(cluster_member, node_member, pkt_control, elec_tran,\
                 elec_rec, fs, mpf, d_threshold, r2, data_distance, dead):
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
        node_select = []
        log_c_select = []
        
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
        
        # collect maximum range of each cluster can get
        log_c_select = sorted(log_c_select, key=lambda cluster: cluster[0])
        cluster_select = []
        log = []
        max_dis = []
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
    else:
        node_select = []
        max_dis = []

    return node_select, cluster_member, node_member, dead, data_distance, max_dis


def data_to_cluster(cluster_member, node_member, node_select, pkt_data, elec_tran,\
                 elec_rec, fs, mpf, d_threshold, station_member, dead):
    if dead == 0:
        # Cluster receive all pkt data from nodes_member
        for node in range(len(node_member)):
            if node_select[node][0] != -1 or node_select[node][1] != -1:
                # Send pkt data [node-->cluster]
                if  node_select[node][1] < d_threshold:
                    wast = ((elec_tran+(fs*(node_select[node][1]**2)))*pkt_data)
                    if node_member[node][2]-wast  > 0:
                        node_member[node][2] = node_member[node][2] - wast
                    else:
                        dead = 1
                elif node_select[node][1] >= d_threshold :
                    wast = ((elec_tran+(mpf*(node_select[node][1]**4)))*pkt_data)
                    if node_member[node][2]-wast  > 0:
                        node_member[node][2] = node_member[node][2] - wast
                    else:
                        dead = 1
                # Receive pkt data
                cluster_member[node_select[node][0]][2] = cluster_member[node_select[node][0]][2] - (elec_rec*pkt_data)
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



def optimize_t(cluster_member, node_member, node_select, max_dis, r1,pkt_data,\
               pkt_control, elec_tran,elec_rec, fs, mpf, d_threshold,dead):

##    for k in range(len(cluster_member)):
##        if max_dis[k][1] > r1 and cluster_member[k][3] <= 1 and cluster_member[k][3] >= 0:
##            cluster_member[k][3] =  round(cluster_member[k][3] + 0.1,1)
##        else:
##            cluster_member[k][3] =  round(cluster_member[k][3] - 0.1,1)
##
##    for i in max_dis:
##        for j in range(len(node_member)):
##            if node_select[j][0] == i[0]:
##                if i[1] > r1 and node_member[j][3] <= 1 and node_member[j][3] >= 0:
##                    node_member[j][3] = round(node_member[j][3] + 0.1,1)
##                else:
##                    node_member[j][3] = round(node_member[j][3] - 0.1,1)
    dead = 0
    if dead == 0:
            # Cluster receive all pkt data from nodes_member
        for distance in max_dis:
            for node in range(len(node_member)):
                if node_select[node][0] == distance[0]:
                    # Send pkt data [node<--cluster]
                    if  distance[1] > r1 :
##                    and node_member[node][3] <= 1 and node_member[node][3] >= 0:
                        wast = ((elec_tran+(fs*(distance[1]**2)))*pkt_control)
                        if cluster_member[distance[0]][2]-wast  > 0:
                            cluster_member[distance[0]][2] = cluster_member[distance[0]][2] - wast
                            node_member[node][3] = round(node_member[node][3] - 0.1,1)
                            cluster_member[distance[0]][3] =round(cluster_member[distance[0]][3] -  0.1,1)
                            
                        else:
                            dead = 1
                            
                    else:
                       wast = ((elec_tran+(fs*(distance[1]**2)))*pkt_control)
                       if cluster_member[distance[0]][2]-wast  > 0:
                           cluster_member[distance[0]][2] = cluster_member[distance[0]][2] - wast
                           node_member[node][3] = round(node_member[node][3] + 0.1,1)
                           cluster_member[distance[0]][3] =round(cluster_member[distance[0]][3] +  0.1,1)

                       else:
                            dead = 1
                    # Receive pkt data
                    node_member[node][2] = node_member[node][2] - (elec_rec*pkt_data)
                    
    
    return cluster_member, node_member, dead




def back_to_nodes(cluster_member, node_member, max_dis, r1, t_predefine):
    """ before next loop all cluster switch back to node_member """
    data =[]
    for j in max_dis:
        data.append([cluster_member[j[0]][3], j[1]])
    with open('data t '+str(t_predefine)+'and r0.csv', 'a', newline='') as csvnew:
        write = csv.writer(csvnew)
        for line1 in data:
            write.writerow(line1)
##        with open('data t and r0.csv',newline='') as f:
##            r = csv.reader(f)
##            data = [line for line in r]
            
    for cluster in cluster_member:
        if cluster not in node_member:
            node_member.append(cluster)
    cluster_member = []
    print("****************** ALL back to nodes ***")
    print("nodes : "+str(len(node_member)))
##    print("r1 : "+str(r1))
##    for j in max_dis:
##        print(cluster_member )
    print("*************************")
##    for i in node_member:
##        print(i)

    return cluster_member, node_member


    
def plot_graph(cluster_member, node_member, cch, station_member, r1, r2, data_distance):
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
    plt.hist(data_distance ,bins = [0,5,10,15,20,25,30,35,40,45,50])
    plt.savefig("distance.png")

def plot_data():
    data = []
    for i in range(2,10):
        t_predefine = i/10
        with open("data t "+str(t_predefine)+"and r0", 'r') as csvnew:
            read = csv.reader(csvnew)
            for line1 in read:
                data.append(list(map(int, line1)))
    print(data)

def start():
    print("Choose 0 set new input")
    print("Choose 1 loop with fixed T-value")
    print("Choose 2 loop with dynamic T-value")
    print("Choose 3 get N lap with fixed T-value")
    print("Choose 4 get N lap with dynamic T-value")
    choose = int(input("choose : "))
    print(" ")
    print("*************************************")

    # Change Variables Here!!
    width = 100 # meter
    height = 100 # meter
    density = float(0.0125)
    t_predefine =  float(0.1)
    num_base = 1
    pos_base = "0,0"
    set_energy = 1 # set energy = 1 Joule
    pkt_control = 200 # bit
    pkt_data = 4000  # bit
    elec_tran = 50 * (10 ** (-9))  # 50 nanoj
    elec_rec = 50 * (10 ** (-9))  # 50 nanoj
    fs = 10 * (10 ** (-12))  # 10 picoj
    mpf = 0.012 * (10 ** (-12))  # 0.012 picoj
    d_threshold = 87  # **********************
    r1 = 30 # meter
    r2 = r1*((2*math.log(10))**(0.5)) # meter

    if choose == 0:
        
        station_member = \
            base_station(num_base, pos_base)


        node_member, len_nodes = \
            random_nodes(width, height, station_member, set_energy, density, t_predefine)
        

        start()
    
    elif choose == 1:
        dead = 0
        count_lap = 0
        station_member, node_member, data_distance = [], [], []
        for i in range(2,10):
            t_predefine = i/10
            
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
                    random_cch(node_member, len_nodes)
                

                cluster_member, node_member ,dead = \
                    distance_candidate(node_member, cch, pkt_control, elec_tran,\
                                       elec_rec, fs, mpf, d_threshold, r1,dead)
      

                node_select, cluster_member, node_member, dead, data_distance, max_dis = \
                    nodes_select(cluster_member, node_member, pkt_control, \
                                 elec_tran, elec_rec, fs, mpf, d_threshold,\
                                 r2, data_distance , dead)


                cluster_member, node_member ,dead = \
                    data_to_cluster(cluster_member, node_member, node_select, \
                                    pkt_data, elec_tran, elec_rec, fs, mpf, \
                                    d_threshold, station_member,dead)

                
                plot_graph(cluster_member, node_member, cch, station_member, r1,r2,data_distance)


                cluster_member, node_member = \
                    back_to_nodes(cluster_member, node_member, max_dis, r1, t_predefine)
                
                count_lap += 1
                if dead == 1:
                    print("LAP : "+ str(count_lap))
                    break;
        plot_data()
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
        
        while True:
            
            with open("len_nodes.txt", "r") as text_file:
                len_nodes = int(text_file.read())

            
            cch, node_member = \
                random_cch(node_member, len_nodes)
            

            cluster_member, node_member ,dead = \
                distance_candidate(node_member, cch, pkt_control, elec_tran,\
                                   elec_rec, fs, mpf, d_threshold, r1,dead)
  

            node_select, cluster_member, node_member, dead, data_distance, max_dis = \
                nodes_select(cluster_member, node_member, pkt_control, \
                             elec_tran, elec_rec, fs, mpf, d_threshold,\
                             r2, data_distance , dead)


            cluster_member, node_member ,dead = \
                data_to_cluster(cluster_member, node_member, node_select, \
                                pkt_data, elec_tran, elec_rec, fs, mpf, \
                                d_threshold, station_member,dead)

            cluster_member, node_member, dead = \
                optimize_t(cluster_member, node_member, node_select, max_dis, r1,\
               pkt_control, elec_tran,elec_rec, fs, mpf, d_threshold,dead,pkt_data)
            
            
            #plot_graph(cluster_member, node_member, cch, station_member, r1,r2,data_distance)


            cluster_member, node_member = \
                back_to_nodes(cluster_member, node_member, max_dis, r1)
            
            count_lap += 1
            if dead == 1:
                print("LAP : "+ str(count_lap))
                break;

    elif choose == 3:
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
        
        lap = int(input("set lap : "))
        for _ in range(lap):
            with open("len_nodes.txt", "r") as text_file:
                    len_nodes = int(text_file.read())

            cch, node_member = \
                random_cch(node_member, len_nodes)
            

            cluster_member, node_member ,dead = \
                distance_candidate(node_member, cch, pkt_control, elec_tran,\
                                    elec_rec, fs, mpf, d_threshold, r1,dead)


            node_select, cluster_member, node_member, dead , data_distance, max_dis = \
                nodes_select(cluster_member, node_member, pkt_control, \
                                elec_tran, elec_rec, fs, mpf, d_threshold,\
                                r2, data_distance , dead)


            cluster_member, node_member ,dead = \
                data_to_cluster(cluster_member, node_member, node_select, \
                                pkt_data, elec_tran, elec_rec, fs, mpf, \
                                d_threshold, station_member,dead)


            plot_graph(cluster_member, node_member, cch, station_member, r1,r2,data_distance)
        

            cluster_member, node_member = \
                    back_to_nodes(cluster_member, node_member, max_dis, r1)

    elif choose == 4:
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
        
        lap = int(input("set lap : "))
        for _ in range(lap):

            with open("len_nodes.txt", "r") as text_file:
                    len_nodes = int(text_file.read())

            cch, node_member = \
                random_cch(node_member, len_nodes)
            

            cluster_member, node_member ,dead = \
                distance_candidate(node_member, cch, pkt_control, elec_tran,\
                                    elec_rec, fs, mpf, d_threshold, r1,dead)


            node_select, cluster_member, node_member, dead , data_distance, max_dis = \
                nodes_select(cluster_member, node_member, pkt_control, \
                                elec_tran, elec_rec, fs, mpf, d_threshold,\
                                r2, data_distance , dead)


            cluster_member, node_member ,dead = \
                data_to_cluster(cluster_member, node_member, node_select, \
                                pkt_data, elec_tran, elec_rec, fs, mpf, \
                                d_threshold, station_member,dead)
            

            cluster_member, node_member, dead = \
                optimize_t(cluster_member, node_member, node_select, max_dis, r1,\
               pkt_control, elec_tran,elec_rec, fs, mpf, d_threshold,dead, pkt_data)


            plot_graph(cluster_member, node_member, cch, station_member, r1,r2,data_distance)


##            cluster_member, node_member = \
##                    back_to_nodes(cluster_member, node_member, max_dis, r1)
    plot_graph(cluster_member, node_member, cch, station_member, r1,r2,data_distance)
start()
