import random as rd
import math
import matplotlib.pyplot as plt
import csv


def base_bs(num_base, pos_base):
    """input bs point"""
    # Set POS bs here
    bs_member = []
    for _ in range(num_base):
        bs_member.append(map(int, pos_base.split(',')))
    # append data to csv. file
    with open('bs_member7.csv', 'w', newline='') as csvnew:
        write = csv.writer(csvnew)
        for line in bs_member:
            write.writerow(line)

    return bs_member


def random_cm(width, height, bs_member, set_energy, density, t_value, decrease_val):
    """random cm"""
    # Random cm
    cm_original = []
    len_cm = math.ceil(density * (width * height)) 
    count = 0
    while len(cm_original) != len_cm:
        random_x, random_y = rd.randint(0, width), rd.randint(0, height)
        if [random_x, random_y, set_energy, t_value] not in cm_original and \
           [random_x, random_y, set_energy, t_value] not in bs_member:
            cm_original.append([random_x, random_y, set_energy, t_value, decrease_val])
        count += 1
    # append data to csv. file
    with open('cm_original7.csv', 'w', newline='') as csvnew:
        write = csv.writer(csvnew)
        for line1 in cm_original:
            write.writerow(line1)
    with open("len_cm7.txt", "w") as text_file:
        text_file.write(str(len_cm))

    return cm_original, len_cm


def random_cch(cm_original, len_cm, reduce_cch):
    """random cch from amount Node"""
    cch = []
    # random candidate cluster
    temp = cm_original[0][4]
    second = 0
    for cm in cm_original:
        if cm[4] > temp:
            second = temp
            temp = cm[4]
    keep = []
    for cm in  cm_original:
        if cm[4] > 5 and len(keep) < len(cm_original)*reduce_cch:
            if second == cm[4] or temp == cm[4] :
                cm_original.remove(cm)
                keep.append(cm)
                
    for cm in cm_original:
        prob_v = round(rd.uniform(0, 1), 1)
        if prob_v  <= cm[3]:
            cch.append(cm)
    cluster_member = [i for i in cm_original if i not in cch]

    if len(cch) == 0:
        random_cch(cluster_member, len_cm)
    
    for i in keep:
        cm_original.append(i)
    return cch, cluster_member


def e_distance_candidate(cch, pkt_control, elec_tran, elec_rec, fs, \
                         mpf, d_threshold, dead, r, dead_point):
    
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
                        dead_point = cch[other]
                        dead_point.append('cch anno')
                        dead = 0
            # Send pkt control
            if  r1 < d_threshold:
                e_tx = (elec_tran + (fs*(r1**2)))*pkt_control
                if cch[main][2] - e_tx > 0:
                    cch[main][2] = cch[main][2] - e_tx
                else:
                    dead_point = cch[main]
                    dead_point.append('cch recive each')
                    dead = 1
            elif r1 >= d_threshold:
                e_tx = (elec_tran + (mpf*(r1**4)))*pkt_control
                if cch[main][2] - e_tx  > 0:
                    cch[main][2] = cch[main][2] - e_tx
                else:
                    dead_point = cch[main]
                    dead_point.append('cch recive each')
                    dead = 1
            
    return dead, cch, dead_point


def distance_candidate(cch, r1, cluster_member, dead, cm_original):
    cluster_head = []
    if dead == 0:
        # sort by energy [from most to least]
        for lap in range(len(cch)-1,0,-1):
            for cm in range(lap):
                if cch[cm][2] < cch[cm+1][2]:
                    temp = cch[cm]
                    cch[cm] = cch[cm+1]
                    cch[cm+1] = temp
        
        # Choose who should be cluster member
        me_ch = []
        me_not = []
        for main in range(len(cch)):
            log_distance = []
            for other in range(len(cch)):
                distance = math.sqrt((cch[main][0] - cch[other][0])**2 + \
                                    (cch[main][1] - cch[other][1])**2)
                log_distance.append(distance)
            count = 0
            for log in range(len(log_distance)):
                if log_distance[log] != 0 and log_distance[log] <= r1:
                    if main < log and cch[main] not in me_not:
                        me_ch.append(cch[main])
                        me_not.append(cch[log])
                        count = 0
                elif log_distance[log] != 0 and log_distance[log] > r1 and count >= len(log_distance)-1:
                    if main < log and cch[main] not in me_not:
                        me_ch.append(cch[main])
                count += 1

        me_ch2 = []
        me_not2 = []
        for cm in me_ch:
            if cm not in me_ch2:
                me_ch2.append(cm)
        for ch2 in me_not:
            if ch2 not in me_not2:
                me_not2.append(ch2)

        for ch in me_ch2:
            cluster_head.append(ch)
        for not_ch in me_not2:
            cluster_member.append(not_ch)
        for i in cm_original:
            for x in cluster_member:
                if i[:2] == x[:2]:
                    i[4] += 1
    return cluster_head, cluster_member, dead, cm_original


def e_cm_select_ch(cluster_head, cluster_member, pkt_control, elec_tran, \
                   elec_rec, fs, mpf, d_threshold, dead, r2, dead_point):
    if dead == 0:
        # Calculate all energy use to send/Receive pkt control
            for ch in range(len(cluster_head)):
                # Send pkt control
                if  r2 < d_threshold:
                    e_tx = ((elec_tran + (fs*(r2**2)))*pkt_control)
                    if cluster_head[ch][2] - e_tx > 0 : 
                        cluster_head[ch][2] = cluster_head[ch][2] - e_tx
                    else:
                        dead_point = cluster_head[ch]
                        dead_point.append('cch announce')
                        dead = 1
                elif r2 >= d_threshold :
                    e_tx = ((elec_tran + (mpf*(r2**4)))*pkt_control)
                    if cluster_head[ch][2] - e_tx  > 0:
                        cluster_head[ch][2] = cluster_head[ch][2] - e_tx
                    else:
                        dead_point = cluster_head[ch]
                        dead_point.append('cch')
                        dead = 1
                for cm in range(len(cluster_member)):
                    distance = math.sqrt((cluster_member[cm][0] - cluster_head[ch][0])**2 +
                                        (cluster_member[cm][1] - cluster_head[ch][1])**2)
                    # Receive pkt control
                    e_rx = elec_rec*pkt_control
                    if distance <= r2:
                        if cluster_member[cm][2] - e_rx > 0:
                            cluster_member[cm][2] = cluster_member[cm][2] - e_rx
                        else:
                            dead_point = cluster_member[cm]
                            dead_point.append('cch')
                            dead = 1

    return cluster_head, cluster_member, dead, dead_point


def cm_select_ch(cluster_head, cluster_member, r2, data_distance, dead):
    max_distance = []
    cm_select = []
    log_cm_select = []
    ch_select = []
    amount_cm_in_ch = {}
    count_ch_member = []

    for ch in range(len(cluster_head)):
        amount_cm_in_ch.update({ch:0})

    if dead == 0:
        # Cluster choose who's my member
        for cm in range(len(cluster_member)):
            shotest = -1  # shortest distance
            what_cluster = -1  # what cluster?
            check = 0
            for ch in range(len(cluster_head)):
                distance = math.sqrt((cluster_member[cm][0] - cluster_head[ch][0])**2 +
                                     (cluster_member[cm][1] - cluster_head[ch][1])**2)
                if distance <= r2:
                    if what_cluster is -1:
                        shotest = distance
                        what_cluster = ch
                        check = 1
                    elif distance < shotest:
                        shotest = distance
                        what_cluster = ch
                        check = 1
                    data_distance.append(shotest)
                elif distance > r2 and check == 0:
                    shotest = -1
                    what_cluster = -1
            cm_select.append([what_cluster, shotest])
            log_cm_select.append([what_cluster, shotest])
        

        #count amount of cm of each ch in dict
        for ch1 in amount_cm_in_ch:
            for ch2 in range(len(log_cm_select)):
                if ch1 == log_cm_select[ch2][0]:
                    amount_cm_in_ch[ch1] += 1
        
        # if ch didn't have cm at all
        for ch3 in amount_cm_in_ch.keys():
            count_ch_member.append(amount_cm_in_ch[ch3])
            if amount_cm_in_ch[ch3] == 0:
                cm_select.append([ch3, 0])
                log_cm_select.append([ch3, 0])
        
        # collect maximum range of each ch can get from they cm
        log_cm_select = sorted(log_cm_select, key=lambda ch: ch[0])
        log = []
        check_ch = 0
        for j in log_cm_select:
            if j[0] != -1 and j[0] == check_ch:
                log.append(j)
            elif j[0] != -1 and j[0] != check_ch:
                ch_select.append(log)
                log = []
                log.append(j)
                check_ch += 1
        ch_select.append(log)
        
        for k in range(len(ch_select)):
            log_max = max(b for (a, b) in ch_select[k])
            max_distance.append([k, log_max])
            
    return data_distance, cm_select, max_distance, dead, count_ch_member


def e_data_exchange(cluster_head, cluster_member, cm_select, pkt_data, elec_tran,\
                    elec_rec, fs, mpf, d_threshold, dead, dead_point):
    if dead == 0:
        # ch receive all pkt data from cm
        for cm in range(len(cluster_member)):
            if cm_select[cm][1] > 0:
                # Send pkt data [cm-->ch]
                if  cm_select[cm][1] < d_threshold:
                    e_tx = ((elec_tran + (fs*(cm_select[cm][1]**2)))*pkt_data)
                    if cluster_member[cm][2] - e_tx  > 0:
                        cluster_member[cm][2] = cluster_member[cm][2] - e_tx
                    else:
                        dead_point = cluster_member[cm]
                        dead_point.append('data cm to ch')
                        dead = 1
                elif cm_select[cm][1] >= d_threshold :
                    e_tx = ((elec_tran + (mpf*(cm_select[cm][1]**4)))*pkt_data)
                    if cluster_member[cm][2] - e_tx  > 0:
                        cluster_member[cm][2] = cluster_member[cm][2] - e_tx
                    else:
                        dead_point = cluster_member[cm]
                        dead_point.append('data cm to ch')
                        dead = 1
                # Receive pkt data
                e_rx = elec_rec*pkt_data
                if cluster_head[cm_select[cm][0]][2] - e_rx > 0:
                    cluster_head[cm_select[cm][0]][2] = cluster_head[cm_select[cm][0]][2] - e_rx
                else:
                    dead_point = cluster_member[cm]
                    dead_point.append('ch recive out of energy ')
                    dead = 1

    return cluster_head, cluster_member, dead, dead_point


def e_to_bs(cluster_head, bs_member, pkt_data, elec_tran, elec_rec, fs, mpf, \
                  d_threshold, dead, count_ch_member, dead_point):
    if dead == 0:
        base_x, base_y = zip(*bs_member)
        
        for member in range(len(count_ch_member)):
            e_agg = (count_ch_member[member]+1)*pkt_data*elec_tran
            cluster_head[member][2] -= e_agg
        
        for ch in cluster_head:
            # Send pkt data [clsuter-->bs]
            distance = math.sqrt((int(base_x[0] - ch[0])**2 + int(base_y[0] - ch[1])**2))
            if  distance < d_threshold:
                e_tx = (elec_tran + (fs*(distance**2)))*pkt_data
                if ch[2] - e_tx  > 0:
                    ch[2] = ch[2] - e_tx
                else:
                    dead_point = ch
                    dead_point.append('ch to bs')
                    dead = 1
            elif distance >= d_threshold :
                e_tx = (elec_tran + (mpf*(distance**4)))*pkt_data
                if ch[2] - e_tx  > 0:
                    ch[2] = ch[2] - e_tx
                else:
                    dead_point = ch
                    dead_point.append('ch to bs')
                    dead = 1
    return cluster_head, bs_member, dead, dead_point


def plot_graph(cluster_head, cluster_member, cch, bs_member, r1, r2, data_distance):
    # split 2d list to 1d *list* [use with graph only]
    node_x, node_y, energy_node, t_value = zip(*cluster_member)
    # PLOT
    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='datalim')
    # PLOT NODES DOT 
    plt.plot(node_x[0:], node_y[0:], '.', color='green', alpha=0.7)
    # PLOT CLUSTER DOT 
    for plot in cluster_head:
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


def back_to_cm(cluster_head, cluster_member, max_distance, r1, t_value, count_lap, dead_lap, dead, count_ch_member):
    """ before next loop all cluster switch back to cluster_member """
    # collect data highest distance from each cluster
    if dead == 0:
        log1 =[]
        for d in max_distance:
            if d[1] != 0:
                log1.append([dead_lap, count_lap, d[1], cluster_head[d[0]][3]])
        with open('data t '+str(t_value)+' and r0.csv', 'a', newline='') as csvnew:
            write = csv.writer(csvnew)
            for line1 in log1:
                write.writerow(line1)
        
        log2 = [[count_lap, len(cluster_head), count_ch_member]]
        with open('data cluster fix '+str(t_value)+'.csv', 'a', newline='') as csvnew:
            write = csv.writer(csvnew)
            for line in log2:
                write.writerow(line)
        
        # all cluster back to node
        for ch in cluster_head:
            if ch not in cluster_member:
                cluster_member.append(ch)

    return cluster_member


def start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
          d_threshold, r1, r2, dead_lap, reduce_cch):
    # Change Variables Here!!
    t_value =  float(0.7)
    decrease_val = float(0.0)
    elec_tran = 50 * (10 ** (-9))  # 50 nanoj
    elec_rec = 50 * (10 ** (-9))  # 50 nanoj
    fs = 10 * (10 ** (-12))  # 10 picoj
    mpf = 0.012 * (10 ** (-12))  # 0.012 picoj
    dead_point = []
    
    
    # Random new network topology
    bs_member = \
    base_bs(num_base, pos_base)


    cm_original, len_cm = \
    random_cm(width, height, bs_member, set_energy, density, t_value, decrease_val)


    dead = 0
    count_lap = 1
    bs_member, cm_original, data_distance = [], [], []
    with open("bs_member7.csv", 'r') as csvnew:
        read = csv.reader(csvnew)
        for line1 in read:
            bs_member.append(list(map(int, line1)))
    with open("cm_original7.csv", 'r') as csvnew:
        read = csv.reader(csvnew)
        for line2 in read:
            cm_original.append(list(map(float, line2)))
    
    while True:
        with open("len_cm7.txt", "r") as text_file:
            len_cm = int(text_file.read())


        cch, cluster_member = \
        random_cch(cm_original, len_cm, reduce_cch)


        dead, cch, dead_point = \
        e_distance_candidate(cch, pkt_control, elec_tran, elec_rec, fs, mpf, d_threshold, dead, r1, dead_point)
        

        cluster_head, cluster_member, dead, cm_original = \
        distance_candidate(cch, r1, cluster_member, dead, cm_original)
        
        cluster_head, cluster_member, dead, dead_point = \
        e_cm_select_ch(cluster_head, cluster_member, pkt_control, elec_tran, elec_rec, fs, mpf, d_threshold, dead, r2, dead_point)

        
        data_distance, cm_select, max_distance, dead, count_ch_member = \
        cm_select_ch(cluster_head, cluster_member, r2, data_distance, dead)
        

        cluster_head, cluster_member, dead, dead_point = \
        e_data_exchange(cluster_head, cluster_member, cm_select, pkt_data, elec_tran,elec_rec, fs, mpf, d_threshold, dead, dead_point)
        

        cluster_head, bs_member, dead, dead_point = \
        e_to_bs(cluster_head, bs_member, pkt_data, elec_tran, elec_rec, fs, mpf, d_threshold, dead, count_ch_member, dead_point)
        
        
        # plot_graph(cluster_head, cluster_member, cch, bs_member, r1, r2, data_distance)


        cluster_member = \
        back_to_cm(cluster_head, cluster_member, max_distance, r1, t_value, count_lap, dead_lap, dead, count_ch_member)
        
        
        if dead == 0:
            count_lap += 1
        elif dead == 1:
            print("DeadLAP : "+ str(count_lap-1))
            dead_point = [dead_point]
            with open('dead point fix '+str(t_value)+'.csv', 'a', newline='') as csvnew:
                write = csv.writer(csvnew)
                for line in dead_point:
                    write.writerow(line)
            log3 = [[t_value, count_lap]]
            with open('count lap fix '+str(t_value)+'.csv', 'a', newline='') as csvnew:
                write = csv.writer(csvnew)
                for line in log3:
                    write.writerow(line)
            break
        
    print(dead_lap, end="\n")
width = 100 # meter
height = 100 # meter
density = float(0.0125)
num_base = 1
pos_base = "-10,50"
set_energy = 1 # set energy = 1 Joule
pkt_control = 200 # bit
pkt_data = 4000  # bit
d_threshold = 87  # **********************
r1 = 30 # meter
r2 = r1*((2*math.log(10))**(0.5)) # meter
decimal = 2
decrease_t = 0.01
increase_t = 0.01
reduce_cch = 0.3

for l in range(50):
    start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
            d_threshold, r1, r2, l, reduce_cch)
