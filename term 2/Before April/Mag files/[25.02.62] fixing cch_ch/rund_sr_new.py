import random as rd
import math
import matplotlib.pyplot as plt
import csv
from collections import OrderedDict


def base_bs(num_base, pos_base, t_value):
    """input bs point"""
    # Set POS bs here
    bs_member = []
    for _ in range(num_base):
        bs_member.append(map(int, pos_base.split(',')))
    # append data to csv. file
    with open('bs_memberD'+str(t_value*10)+'.csv', 'w', newline='') as csvnew:
        write = csv.writer(csvnew)
        for line in bs_member:
            write.writerow(line)

    return bs_member

        
def random_cm(width, height, bs_member, set_energy, density, t_value):
    """random cm"""
    # Random cm
    cm_original = []
    len_cm = math.ceil(density * (width * height)) 
    count = 0
    while len(cm_original) != len_cm:
        cache_cm = []
        random_x, random_y = rd.randint(0, width), rd.randint(0, height)
        data_set = rd.randint(1, 19)
        if [random_x, random_y] not in cache_cm:
            cache_cm.append([random_x, random_y])
        if [random_x, random_y] in cache_cm:
            cm_original.append([random_x, random_y, set_energy, t_value, data_set, count+1])
        count += 1
    
    # append data to csv. file
    with open('cm_originalD'+str(t_value*10)+'.csv', 'w', newline='') as csvnew:
        write = csv.writer(csvnew)
        for line1 in cm_original:
            write.writerow(line1)
    with open("len_cmD"+str(t_value*10)+".txt", "w") as text_file:
        text_file.write(str(len_cm))

    return cm_original, len_cm


def pull_data():
    count = 1
    at1, at2, at3, at4, at5, at6 = [],[],[],[],[],[]
    at7, at8, at9, at10, at11, at12 = [],[],[],[],[],[]
    at13, at14, at15, at16, at17, at18, at19 = [],[],[],[],[],[],[]
    count = 1
    with open('place.csv', 'r', newline='') as csvnew:
        read = csv.reader(csvnew)
        for line in read:
            eval('at%d'% (count)).append(line)
            count += 1
    # for cm in range(len(cm_original)):
    #     place = rd.randint(1, 19)
    #     print(eval('at%d'% (place)))
    #     print(" ")
    #     print(eval('at%d'% (place))[0][:6])
    #     print(" ")
        # cm_original[cm].append(eval('at%d'% (place))[0][:6])
    
    return at1, at2, at3, at4, at5, at6, at7, at8, at9, at10, at11, at12, at13, at14, at15, at16, at17, at18, at19


def random_cch(cm_original, len_cm, count_lap):
    """random cch from amount Node"""
    cch = []
    # random candidate cluster
    for cm in cm_original:
        prob_v = round(rd.uniform(0, 1), 1)
        if prob_v <= cm[3]:
            cch.append(cm)
    with open('check cch.csv', 'a', newline='') as csvnew:
        write = csv.writer(csvnew)
        for line in cch:
            write.writerow([count_lap, line[0],line[1],line[2], line[3]])
        write.writerow(' ')

    cluster_member = [i for i in cm_original if i not in cch]
    if len(cch) == 0:
        random_cch(cluster_member, len_cm)

    return cch, cluster_member


def e_comp(cch, pkt_control, elec_tran, elec_rec, fs, \
                         mpf, d_threshold, dead, r1, dead_point, used_energy):
    # BROADCAST
    if dead == 0:
        # Calculate all energy use to send/Receive pkt control
        for main in range(len(cch)):
            # Send pkt control
            if  r1 < d_threshold:
                e_tx = (elec_tran + (fs*(r1**2)))*pkt_control
                if cch[main][2] - e_tx > 0:
                    cch[main][2] = cch[main][2] - e_tx
                    used_energy['1'] = used_energy.get('1')+e_tx
                else:
                    dead_point = cch[main]
                    dead_point.append('1')
                    dead = 1
                e_rx = elec_rec*pkt_control
                # Receive pkt control
                if cch[main][2] - e_rx > 0:
                        cch[main][2] = cch[main][2] - e_rx
                        used_energy['2'] = used_energy.get('2')+e_rx
                else:
                    dead_point = cch[main]
                    dead_point.append('2')
                    dead = 0
            elif r1 >= d_threshold:
                e_tx = (elec_tran + (mpf*(r1**4)))*pkt_control
                if cch[main][2] - e_tx  > 0:
                    cch[main][2] = cch[main][2] - e_tx
                    used_energy['1'] = used_energy.get('1')+e_tx
                else:
                    dead_point = cch[main]
                    dead_point.append('1')
                    dead = 1
                e_rx = elec_rec*pkt_control
                # Receive pkt control
                if cch[main][2] - e_rx > 0:
                        cch[main][2] = cch[main][2] - e_rx
                        used_energy['2'] = used_energy.get('2')+e_rx
                else:
                    dead_point = cch[main]
                    dead_point.append('2')
                    dead = 0
            # for other in range(len(cch)):
            #     distance = math.sqrt((cch[main][0] - cch[other][0])**2 + \
            #                    (cch[main][1] - cch[other][1])**2)
            #     e_rx = elec_rec*pkt_control
            #     # Receive pkt control
            #     if  main != other and distance <= r1: # if its in range of r1 its can't recieve
            #         if cch[other][2] - e_rx > 0:
            #             cch[other][2] = cch[other][2] - e_rx
            #             used_energy['2'] = used_energy.get('2')+e_rx
            #             print(2,e_rx)
            #         else:
            #             dead_point = cch[other]
            #             dead_point.append('2')
            #             dead = 0            
            
    return dead, cch, dead_point, used_energy


def comp(cch, r1, cluster_member, dead, cm_original):
    cluster_head = []
    if dead == 0:
        # sort by energy [from most to least]
        for lap in range(len(cch)-1,0,-1):
            for cm in range(lap):
                if cch[cm][2] < cch[cm+1][2]:
                    temp = cch[cm]
                    cch[cm] = cch[cm+1]
                    cch[cm+1] = temp
        # print("BEFORE")
        # for i in cch:print(i)
        # print("**************************")

        me_ch = []
        me_not = []
        count = 0
        for main in range(len(cch)):
            log_distance = []
            for other in range(len(cch)):
                distance = math.sqrt((cch[main][0] - cch[other][0])**2 + \
                                    (cch[main][1] - cch[other][1])**2)
                log_distance.append(distance)
            for log in range(len(log_distance)):
                if log_distance[log] != 0 and log_distance[log] <= r1:
                    if cch[main][2] >= cch[log][2] and cch[main] not in me_not:
                        me_ch.append(cch[main])
                        me_not.append(cch[log])
                        count = 1
                elif log_distance[log] != 0 and log_distance[log] > r1:
                    if log == len(cch)-1 and cch[main] not in me_not and count == 0:
                        me_ch.append(cch[main])
            count = 0
        
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
        
        # for i in me_ch2: print(i)
        # print("**************************")
        # for i in me_not2: print(i)
        # print("**************************")
        # print("-----------------------------------------------")


        # print("AFTER")
        # for i in cch:print(i)
        # print("**************************")

        

        # Choose who should be cluster member
        # me_ch = []
        # me_not = []
        # for main in range(len(cch)):
        #     log_distance = []
        #     for other in range(len(cch)):
        #         distance = math.sqrt((cch[main][0] - cch[other][0])**2 + \
        #                             (cch[main][1] - cch[other][1])**2)
        #         log_distance.append(distance)
        #     for log in range(len(log_distance)):
        #         if log_distance[log] != 0 and log_distance[log] <= r1:
        #             if main < log and cch[main] not in me_not:
        #                 me_ch.append(cch[main])
        #                 me_not.append(cch[log])
        #         elif log_distance[log] != 0 and log_distance[log] > r1:
        #             if other == len(cch)-1 and cch[main] not in me_not:
        #                 me_ch.append(cch[main])
        # me_ch2 = []
        # me_not2 = []
        # for cm in me_ch:
        #     if cm not in me_ch2:
        #         me_ch2.append(cm)
        # for ch2 in me_not:
        #     if ch2 not in me_not2:
        #         me_not2.append(ch2)
        # for ch in me_ch2:
        #     cluster_head.append(ch)
        # for not_ch in me_not2:
        #     cluster_member.append(not_ch)
        
        for i in range(len(cluster_head)):
            ld = []
            for j in range(len(cluster_head)):
                distance = math.sqrt((cluster_head[i][0] - cluster_head[j][0])**2 + \
                                    (cluster_head[i][1] - cluster_head[j][1])**2)
                ld.append(distance)
            # print(cluster_head[i])
            for lo in range(len(ld)):
                if ld[lo] != 0 and ld[lo] <= r1:
                    print(ld[lo])
            # print(" ")
        
        # for i in cluster_head:print(i)
        # print("-------------------------------------------------")
        
    return cluster_head, cluster_member, dead, cm_original


def e_dis(cluster_head, cluster_member, pkt_control, elec_tran, \
                elec_rec, fs, mpf, d_threshold, dead, r2, dead_point, used_energy):
    # BROADCAST
    if dead == 0:
        # Calculate all energy use to send/Receive pkt control
        for ch in range(len(cluster_head)):
            # Send pkt control
            if  r2 < d_threshold:
                e_tx = ((elec_tran + (fs*(r2**2)))*pkt_control)
                if cluster_head[ch][2] - e_tx > 0 : 
                    cluster_head[ch][2] = cluster_head[ch][2] - e_tx
                    used_energy['3'] = used_energy.get('3')+e_tx
                    # print(3, e_tx )
                else:
                    dead_point = cluster_head[ch]
                    dead_point.append('3')
                    dead = 1
            elif r2 >= d_threshold :
                e_tx = ((elec_tran + (mpf*(r2**4)))*pkt_control)
                if cluster_head[ch][2] - e_tx  > 0:
                    cluster_head[ch][2] = cluster_head[ch][2] - e_tx
                    used_energy['3'] = used_energy.get('3')+e_tx
                    # print(3, e_tx)
                else:
                    dead_point = cluster_head[ch]
                    dead_point.append('3')
                    dead = 1
            # for cm in range(len(cluster_member)):
            #     print(ch, cm, end = ' ')
            #     distance = math.sqrt((cluster_member[cm][0] - cluster_head[ch][0])**2 +
            #                         (cluster_member[cm][1] - cluster_head[ch][1])**2)
            #     # Receive pkt control
            #     e_rx = elec_rec*pkt_control
            #     if distance <= r2:
            #         if cluster_member[cm][2] - e_rx > 0:
            #             cluster_member[cm][2] = cluster_member[cm][2] - e_rx
            #             used_energy['4'] = used_energy.get('4')+e_rx
            #             print(4,e_rx) 
            #         else:
            #             dead_point = cluster_member[cm]
            #             dead_point.append('4')
            #             dead = 1
        for cm in cluster_member:
            e_rx = elec_rec*pkt_control
            if cm[2] - e_rx > 0:
                cm[2] = cm[2] - e_rx
                used_energy['4'] = used_energy.get('4')+e_rx
                # print(4,e_rx) 
            else:
                dead_point = cm
                dead_point.append('4')
                dead = 1

    return cluster_head, cluster_member, dead, dead_point, used_energy


def cm_choose_ch(cluster_head, cluster_member, r2, data_distance, dead):
    cm_select = []
    log_cm_select = []
    amount_cm_in_ch = {}
    data_clus_mem = []
    
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

    return cm_select, log_cm_select, data_distance, amount_cm_in_ch, dead


def e_join(cluster_head, cluster_member, cm_select, pkt_control, elec_tran,\
                    elec_rec, fs, mpf, d_threshold, dead, dead_point, used_energy):
    # UNICAST
    if dead == 0:
        # ch receive all pkt control from cm
        for cm in range(len(cluster_member)):
            if cm_select[cm][1] > 0:
                # Send pkt control [cm-->ch]
                if  cm_select[cm][1] < d_threshold:
                    e_tx = ((elec_tran + (fs*(cm_select[cm][1]**2)))*200)
                    if cluster_member[cm][2] - e_tx  > 0:
                        cluster_member[cm][2] = cluster_member[cm][2] - e_tx
                        used_energy['5'] = used_energy.get('5')+e_tx
                        # print(5,e_tx)
                    else:
                        dead_point = cluster_member[cm]
                        dead_point.append('5')
                        dead = 1
                elif cm_select[cm][1] >= d_threshold :
                    e_tx = ((elec_tran + (mpf*(cm_select[cm][1]**4)))*200)
                    if cluster_member[cm][2] - e_tx  > 0:
                        cluster_member[cm][2] = cluster_member[cm][2] - e_tx
                        used_energy['5'] = used_energy.get('5')+e_tx
                        # print(5,t_ex)
                    else:
                        dead_point = cluster_member[cm]
                        dead_point.append('5')
                        dead = 1
                # Receive pkt control
                # e_rx = elec_rec*200
                # if cluster_head[cm_select[cm][0]][2] - e_rx > 0:
                #     cluster_head[cm_select[cm][0]][2] = cluster_head[cm_select[cm][0]][2] - e_rx
                #     used_energy['6'] = used_energy.get('6')+e_rx
                # else:
                #     dead_point = cluster_head[cm_select[cm][0]]
                #     dead_point.append('6')
                #     dead = 1
        for ch in cluster_head:
            e_rx = elec_rec*200
            # print(e_rx, pkt_data)
            if ch[2] - e_rx > 0:
                ch[2] = ch[2] - e_rx
                used_energy['6'] = used_energy.get('6')+e_rx
                # print(6, e_rx)
            else:
                dead_point = ch
                dead_point.append('6')
                dead = 1

    return cluster_head, cluster_member, dead, dead_point, used_energy


def calculate_some_data(cluster_head, cm_select, log_cm_select, amount_cm_in_ch, dead):
    max_distance = []
    ch_select = []
    count_ch_member = []
    cm_out_of_range = 0

    if dead == 0:
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
        # for i in log_cm_select: print(i)
        # print("-----")
        # for i in max_distance: print(i)
        # print("")
        
        for i in cm_select:
            if i[0] == -1:
                cm_out_of_range += 1
            
    return max_distance, count_ch_member, cm_out_of_range, dead


def e_conf(cluster_head, cluster_member, pkt_control, elec_tran, \
                elec_rec, fs, mpf, d_threshold, dead, dead_point, max_distance,\
           used_energy, cm_select):
##    print('ch confirm')
    # UNICAST
    if dead == 0:
        # ch send confirm pkt control to cm
        for ch in range(len(cluster_head)):
                # Send pkt control
            if  max_distance[ch][1] < d_threshold:
                e_tx = ((elec_tran + (fs*(max_distance[ch][1]**2)))*pkt_control)
                
##                print('--less', e_tx, max_distance[ch][1], pkt_control )
                if cluster_head[ch][2] - e_tx > 0 : 
                    cluster_head[ch][2] = cluster_head[ch][2] - e_tx
                    used_energy['7'] = used_energy.get('7')+e_tx
##                    print(7, e_tx)
                    
                else:
                    dead_point = cluster_head[ch]
                    dead_point.append('7')
                    dead = 1
            elif max_distance[ch][1] >= d_threshold :
                e_tx = ((elec_tran + (mpf*(max_distance[ch][1]**4)))*pkt_control)
                if cluster_head[ch][2] - e_tx  > 0:
                    cluster_head[ch][2] = cluster_head[ch][2] - e_tx
                    used_energy['7'] = used_energy.get('7')+e_tx
##                    print('--more', e_tx, max_distance[ch][1], pkt_control )
##                    print(7, e_tx)
                else:
                    dead_point = cluster_head[ch]
                    dead_point.append('7')
                    dead = 1
##            for cm in range(len(cluster_member)):
##                if cm_select[cm][0] == ch:
##                    distance = math.sqrt((cluster_member[cm][0] - cluster_head[ch][0])**2 +
##                                        (cluster_member[cm][1] - cluster_head[ch][1])**2)
##                    # Receive pkt control
##                    e_rx = elec_rec*pkt_control
##                    if distance <= max_distance[ch][1]:
##                        if cluster_member[cm][2] - e_rx > 0:
##                            cluster_member[cm][2] = cluster_member[cm][2] - e_rx
##                            used_energy['8'] = used_energy.get('8')+e_rx
##                            print(8,e_rx)
##    ##                                print('cm recive',e_rx)
##                        else:
##                            dead_point = cluster_member[cm]
##                            dead_point.append('8')
##                            dead = 1
        for cm in cluster_member:
            e_rx = elec_rec*pkt_control
##                if distance <= max_distance[ch][1]:
            if cm[2] - e_rx > 0:
                cm[2] = cm[2] - e_rx
                used_energy['8'] = used_energy.get('8')+e_rx
##                print(8,e_rx)
##                                print('cm recive',e_rx)
            else:
                dead_point = cm
                dead_point.append('8')
                dead = 1

    return cluster_head, cluster_member, dead, dead_point, used_energy


def check_data(cluster_head, cluster_member, at1, at2, at3, at4, at5, at6, \
                at7, at8, at9, at10, at11, at12, at13, at14, at15, \
                at16, at17, at18, at19, t_value, cache, collect_envi, cm_select, count_sr):
    send_or_not = []
    check_super_round = 1
    
    if count_sr == 0:
        for cm in range(len(cluster_member)):
            send_or_not.append([cluster_member[cm][5], 1])
            collect_envi.append([cluster_member[cm][5], eval('at%d'% (cluster_member[cm][4]))[0][cache]])
    else:
        for cm in range(len(cluster_member)):
            for cec in collect_envi:
                if cluster_member[cm][5] == cec[0]:
                    old = float(cec[1])
                    new = float(eval('at%d'% (cluster_member[cm][4]))[0][cache])
                    diff = abs(((old - new) / old)*100)
                    if diff > 0.0:
                        send_or_not.append([cluster_member[cm][5], 1])
                        cec[1] = new
                    else:
                        send_or_not.append([cluster_member[cm][5], 0])
                        
    sum_envi_ch = [ [] for _ in range(len(cluster_head))]
    for cm in range(len(cluster_member)):
        sum_envi_ch[cm_select[cm][0]].append(float(collect_envi[cm][1]))

    if count_sr == 0:
        for ch in range(len(cluster_head)):
            sum_envi_ch[ch].append(float(eval('at%d'% (cluster_head[ch][4]))[0][cache]))
        for ch in range(len(cluster_head)): 
            send_or_not.append([cluster_head[ch][5], 1])
            collect_envi.append([cluster_head[ch][5], sum(sum_envi_ch[ch])/ float(len(sum_envi_ch[ch]))])
    else:
        for ch in range(len(cluster_head)):
            sum_envi_ch[ch].append(float(eval('at%d'% (cluster_head[ch][4]))[0][cache]))
        for ch in range(len(cluster_head)):
            for cec in collect_envi:
                if cluster_head[ch][5] == cec[0]:
                    old = float(cec[1])
                    new = sum(sum_envi_ch[ch])/ float(len(sum_envi_ch[ch]))
                    diff = abs(((old - new) / old)*100)
                    if diff > 0.0:
                        send_or_not.append([cluster_head[ch][5], 1])
                        cec[1] = new
                    else:
                        send_or_not.append([cluster_head[ch][5], 0])
    cache += 1
    
    return cache, send_or_not, collect_envi, check_super_round


def e_intra_sr(cluster_head, cluster_member, cm_select, pkt_data, elec_tran,\
                    elec_rec, fs, mpf, d_threshold, dead, dead_point, used_energy, send_or_not):
##    print('--- sr data')
    # UNICAST
    if dead == 0:
        # ch receive all pkt data from cm
        for cm in range(len(cluster_member)):
            for son in send_or_not:
                if cm_select[cm][1] > 0 and cluster_member[cm][5] == son[0] and son[1] == 1:
                    # Send pkt data [cm-->ch]
                    if  cm_select[cm][1] < d_threshold:
                        e_tx = ((elec_tran + (fs*(cm_select[cm][1]**2)))*pkt_data)
##                        print('**',e_tx,cm_select[cm][1],pkt_data )
                        if cluster_member[cm][2] - e_tx  > 0:
                            cluster_member[cm][2] = cluster_member[cm][2] - e_tx
                            used_energy['9'] = used_energy.get('9')+e_tx
                            
                        else:
                            dead_point = cluster_member[cm]
                            dead_point.append('9')
                            dead = 1
                    elif cm_select[cm][1] >= d_threshold :
                        e_tx = ((elec_tran + (mpf*(cm_select[cm][1]**4)))*pkt_data)
##                        print('**>',e_tx,cm_select[cm][1],pkt_data )
                        if cluster_member[cm][2] - e_tx  > 0:
                            cluster_member[cm][2] = cluster_member[cm][2] - e_tx
                            used_energy['9'] = used_energy.get('9')+e_tx
                        else:
                            dead_point = cluster_member[cm]
                            dead_point.append('9')
                            dead = 1
##                    # Receive pkt data
##                    e_rx = elec_rec*pkt_data
##                    print(e_rx, pkt_data)
##                    if cluster_head[cm_select[cm][0]][2] - e_rx > 0:
##                        cluster_head[cm_select[cm][0]][2] = cluster_head[cm_select[cm][0]][2] - e_rx
##                        used_energy['10'] = used_energy.get('10')+e_rx
##                    else:
##                        dead_point = cluster_head[cm_select[cm][0]]
##                        dead_point.append('10')
##                        dead = 1
        for ch in cluster_head:
            e_rx = elec_rec*pkt_data
##            print(e_rx, pkt_data)
            if cluster_head[cm_select[cm][0]][2] - e_rx > 0:
                cluster_head[cm_select[cm][0]][2] = cluster_head[cm_select[cm][0]][2] - e_rx
                used_energy['10'] = used_energy.get('10')+e_rx
            else:
                dead_point = cluster_head[cm_select[cm][0]]
                dead_point.append('10')
                dead = 1
                print(cluster_head[0])
            

    return cluster_head, cluster_member, dead, dead_point, used_energy


def e_agg_sr(cluster_head, count_ch_member, pkt_data, elec_tran, dead_point, dead,\
          used_energy, send_or_not):
##    print('--- sr merge')
    # summarize data
    if dead == 0:
        for member in range(len(count_ch_member)):
            for son in send_or_not:
                if cluster_head[member][5] == son[0] and son[1] == 1:
                    e_agg = (count_ch_member[member]+1)*pkt_data*(elec_tran**10)
                    if cluster_head[member][2] - e_agg > 0:
                        cluster_head[member][2] -= e_agg
                        used_energy['11'] = used_energy.get('11')+e_agg
                    else:
                        dead_point = cluster_head[member]
                        dead_point.append('11')
                        dead = 1

    return cluster_head, dead, dead_point,  used_energy


def e_route_sr(cluster_head, bs_member, pkt_data, elec_tran, elec_rec, fs, mpf, \
                  d_threshold, dead, dead_point, used_energy, send_or_not):
##    print('--- sr sync')
    # UNICAST
    if dead == 0:
        base_x, base_y = zip(*bs_member)
        for ch in range(len(cluster_head)):
            # Send pkt data [clsuter-->bs]
            for son in send_or_not:
                if cluster_head[ch][5] == son[0] and son[1] == 1:
                    distance = math.sqrt((int(base_x[0] - cluster_head[ch][0])**2 + int(base_y[0] - cluster_head[ch][1])**2))
                    if  distance < d_threshold:
                        e_tx = (elec_tran + (fs*(distance**2)))*pkt_data
##                        print(elec_tran, fs, distance,pkt_data, cluster_head[ch][2], e_tx)
                        if cluster_head[ch][2] - e_tx  > 0:
                            cluster_head[ch][2] = cluster_head[ch][2] - e_tx
                            used_energy['12'] = used_energy.get('12')+e_tx
                        else:
                            dead_point = cluster_head[ch]
                            dead_point.append('12')
                            dead = 1
                    elif distance >= d_threshold :
                        e_tx = (elec_tran + (mpf*(distance**4)))*pkt_data
##                        print(elec_tran, fs, distance,pkt_data, cluster_head[ch][2], e_tx)
                        if cluster_head[ch][2] - e_tx  > 0:
                            cluster_head[ch][2] = cluster_head[ch][2] - e_tx
                            used_energy['12'] = used_energy.get('12')+e_tx
                        else:
                            dead_point = cluster_head[ch]
                            dead_point.append('12')
                            dead = 1
        
    return cluster_head, bs_member, dead, dead_point, used_energy


def e_intra(cluster_head, cluster_member, cm_select, pkt_data, elec_tran,\
                    elec_rec, fs, mpf, d_threshold, dead, dead_point, used_energy):
##    print('cm send data')
    # UNICAST
    if dead == 0:
        # ch receive all pkt data from cm
        for cm in range(len(cluster_member)):
            if cm_select[cm][1] > 0:
                # Send pkt data [cm-->ch]
                if  cm_select[cm][1] < d_threshold:
                    e_tx = ((elec_tran + (fs*(cm_select[cm][1]**2)))*pkt_data)
                    if cluster_member[cm][2] - e_tx  > 0:
                        cluster_member[cm][2] = cluster_member[cm][2] - e_tx
                        used_energy['9'] = used_energy.get('9')+e_tx
##                        print(cm,cm_select[cm][0] , end= ' ')
                    else:
                        dead_point = cluster_member[cm]
                        dead_point.append('9')
                        dead = 1
                elif cm_select[cm][1] >= d_threshold :
                    e_tx = ((elec_tran + (mpf*(cm_select[cm][1]**4)))*pkt_data)
                    if cluster_member[cm][2] - e_tx  > 0:
                        cluster_member[cm][2] = cluster_member[cm][2] - e_tx
                        used_energy['9'] = used_energy.get('9')+e_tx
##                        print(cm, cm_select[cm][0] ,end= ' ' )
                    else:
                        dead_point = cluster_member[cm]
                        dead_point.append('9')
                        dead = 1
##                # Receive pkt data
##                e_rx = elec_rec*pkt_data
##                if cluster_head[cm_select[cm][0]][2] - e_rx > 0:
##                    cluster_head[cm_select[cm][0]][2] = cluster_head[cm_select[cm][0]][2] - e_rx
##                    used_energy['10'] = used_energy.get('10')+e_rx
##    ##                    print(cluster_head[cm_select[cm][0]] )
##                else:
##                    dead_point = cluster_member[cm]
##                    dead_point.append('10')
##                    dead = 1
        for ch in cluster_head:
            e_rx = elec_rec*pkt_data
##            print(e_rx, pkt_data)
            if cluster_head[cm_select[cm][0]][2] - e_rx > 0:
                cluster_head[cm_select[cm][0]][2] = cluster_head[cm_select[cm][0]][2] - e_rx
                used_energy['10'] = used_energy.get('10')+e_rx
            else:
                dead_point = cluster_head[cm_select[cm][0]]
                dead_point.append('10')
                dead = 1

    return cluster_head, cluster_member, dead, dead_point, used_energy


def e_agg(cluster_head, count_ch_member, pkt_data, elec_tran, dead_point, dead,\
          used_energy):
##    print('merge')
    # summarize data
    if dead == 0:
        for member in range(len(count_ch_member)):
            e_agg = (count_ch_member[member]+1)*pkt_data*(elec_tran**10)
            if cluster_head[member][2] - e_agg > 0:
                cluster_head[member][2] -= e_agg
                used_energy['11'] = used_energy.get('11')+e_agg
            else:
                dead_point = cluster_head[member]
                dead_point.append('11')
                dead = 1

    return cluster_head, dead, dead_point,  used_energy


def e_route(cluster_head, bs_member, pkt_data, elec_tran, elec_rec, fs, mpf, \
                  d_threshold, dead, dead_point, used_energy):
##    print('sync')
    # UNICAST
    if dead == 0:
        base_x, base_y = zip(*bs_member)
        for ch in cluster_head:
            # Send pkt data [clsuter-->bs]
            distance = math.sqrt((int(base_x[0] - ch[0])**2 + int(base_y[0] - ch[1])**2))
            if  distance < d_threshold:
                e_tx = (elec_tran + (fs*(distance**2)))*pkt_data
##                print(elec_tran, fs, distance,pkt_data, cluster_head[ch][2], e_tx)
                if ch[2] - e_tx  > 0:
                    ch[2] = ch[2] - e_tx
                    used_energy['12'] = used_energy.get('12')+e_tx
                else:
                    dead_point = ch
                    dead_point.append('12')
                    dead = 1
            elif distance >= d_threshold :
                e_tx = (elec_tran + (mpf*(distance**4)))*pkt_data
##                print(elec_tran, fs, distance,pkt_data, cluster_head[ch][2], e_tx)
                if ch[2] - e_tx  > 0:
                    ch[2] = ch[2] - e_tx
                    used_energy['12'] = used_energy.get('12')+e_tx
                else:
                    dead_point = ch
                    dead_point.append('12')
                    dead = 1
    
    return cluster_head, bs_member, dead, dead_point, used_energy


def optimize_t(cluster_head, cluster_member, cm_select, max_distance, decimal, \
                decrease_t, increase_t, r1, dead, check_optimize_t, ch_t_compare):
    # optimize the t-value in the next round
    check_optimize_t = 1
    if dead == 0:
        for ch in range(len(cluster_head)):
            if max_distance[ch][1] > r1:
                if cluster_head[ch][3] < 1 :
                    ch_t_compare.append([ch, cluster_head[ch][3], round(cluster_head[ch][3] + increase_t, decimal)])
                    cluster_head[ch][3] =  round(cluster_head[ch][3] + increase_t, decimal)
                else:
                    ch_t_compare.append([ch, cluster_head[ch][3], cluster_head[ch][3]])

            elif max_distance[ch][1] < r1:
                if cluster_head[ch][3] > 0:
                    ch_t_compare.append([ch, cluster_head[ch][3], round(cluster_head[ch][3] - increase_t, decimal)])
                    cluster_head[ch][3] =  round(cluster_head[ch][3] - decrease_t, decimal)
                else:
                    ch_t_compare.append([ch, cluster_head[ch][3], cluster_head[ch][3]])
            else:
                ch_t_compare.append([ch, cluster_head[ch][3], cluster_head[ch][3]])

        for d in range(len(max_distance)):
            for cm in range(len(cluster_member)):
                if cm_select[cm][0] == max_distance[d][0]:
                    if max_distance[d][1] > r1:
                        if cluster_member[cm][3] < 1:
                            cluster_member[cm][3] = round(cluster_member[cm][3] + increase_t, decimal)
                    elif max_distance[d][1] < r1:
                        if cluster_member[cm][3] > 0:
                            cluster_member[cm][3] = round(cluster_member[cm][3] - decrease_t, decimal)
        
        # print(ch_t_compare)

    return cluster_head, cluster_member, dead, ch_t_compare, check_optimize_t


def plot_graph(cluster_head, cluster_member, cch, bs_member, r1, r2, data_distance):
    # split 2d list to 1d *list* [use with graph only]
    node_x, node_y, energy_node, t_value = zip(*cluster_member)
    # PLOT
    fig, ax = plt.subplots()
    ax.set_aspect('equal', adcmustable='datalim')
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


def back_to_cm_dynamic(cluster_head, cluster_member, max_distance, r1, t_value, count_lap, \
                    dead_round, dead, count_ch_member, len_cm, cm_out_of_range, ch_t_compare, \
                    check_super_round, super_round, count_sr, check_optimize_t, cache, collect_envi):
    """ before next loop all cluster switch back to node_member """
    # collect data highest distance from each cluster
    if dead == 0:
        log1 =[]
        for d in max_distance:
            if d[1] != 0:
                log1.append([dead_round, count_lap, d[1], ch_t_compare[d[0]][1], ch_t_compare[d[0]][2]])
        with open('data t dynamic '+str(t_value)+' and r0.csv', 'a', newline='') as csvnew:
            write = csv.writer(csvnew)
            for line1 in log1:
                write.writerow(line1)

        log2= [[count_lap, len(cluster_head), count_ch_member, len_cm, len_cm-cm_out_of_range]]
        with open('data cluster dynamic '+str(t_value)+'.csv', 'a', newline='') as csvnew:
            write = csv.writer(csvnew)
            for line in log2:
                write.writerow(line)
        
        count_sr += 1
        # print(count_sr," -> ", super_round)
        if check_super_round == 1 and count_sr == super_round:
            check_optimize_t = 0
            check_super_round = 0
            count_sr = 0
            ch_t_compare = []
            collect_envi = []
            
            for ch in cluster_head:
                if ch not in cluster_member:
                    cluster_member.append(ch)
        
    
    return cluster_member, count_sr, check_optimize_t, check_super_round, count_sr, cache, collect_envi, ch_t_compare


def start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
          d_threshold, r1, r2, decimal, decrease_t, increase_t, dead_round, super_round):
    # Change Variables Here!!
    t_value =  float(0.1)
    elec_tran = 50 * (10 ** (-9))  # 50 nanocm
    elec_rec = 50 * (10 ** (-9))  # 50 nanocm
    fs = 10 * (10 ** (-12))  # 10 picocm
    mpf = 0.013 * (10 ** (-12))  # 0.012 picocm
    dead_point = []
    used_energy = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0, '8':0,\
                   '9':0,'10':0,'11':0,'12':0}
    
    # Random new network topology
    bs_member = \
    base_bs(num_base, pos_base, t_value)


    cm_original, len_cm = \
    random_cm(width, height, bs_member, set_energy, density, t_value)

    # Suprer Round Checking
    check_super_round = 0
    check_optimize_t = 0
    count_sr = 0
    cache = 0
    collect_envi = []
    ch_t_compare = []
    
    dead = 0
    count_lap = 1
    bs_member, data_distance = [], []
    cm_original = []
    with open("bs_memberD"+str(t_value*10)+".csv", 'r') as csvnew:
        read = csv.reader(csvnew)
        for line1 in read:
            bs_member.append(list(map(int, line1)))
    with open("cm_originalD"+str(t_value*10)+".csv", 'r') as csvnew:
        read = csv.reader(csvnew)
        for line2 in read:
            cm_original.append(list(map(float, line2)))
    
    while True:
        with open("len_cmD"+str(t_value*10)+".txt", "r") as text_file:
            len_cm = int(text_file.read())
        
        at1, at2, at3, at4, at5, at6, at7, at8, at9, at10, at11, at12, at13, at14, at15, at16, at17, at18, at19 = \
        pull_data()

        if cache > 4000:
            cache = 0
        
        if check_super_round == 0:
            cch, cluster_member = \
            random_cch(cm_original, len_cm, count_lap)

            dead, cch, dead_point, used_energy = \
            e_comp(cch, pkt_control, elec_tran, elec_rec, fs, mpf, d_threshold,\
                dead, r1, dead_point, used_energy)
            
            cluster_head, cluster_member, dead, cm_original = \
            comp(cch, r1, cluster_member, dead, cm_original)
            
            cluster_head, cluster_member, dead, dead_point , used_energy= \
            e_dis(cluster_head, cluster_member, pkt_control, elec_tran, elec_rec, \
                fs, mpf, d_threshold, dead, r2, dead_point, used_energy)

        cm_select, log_cm_select, data_distance, amount_cm_in_ch, dead = \
        cm_choose_ch(cluster_head, cluster_member, r2, data_distance, dead)

        max_distance, count_ch_member, cm_out_of_range, dead = \
        calculate_some_data(cluster_head, cm_select, log_cm_select, amount_cm_in_ch, dead)

        if check_super_round == 0:
            cluster_head, cluster_member, dead, dead_point, used_energy = \
            e_join(cluster_head, cluster_member, cm_select, pkt_data, elec_tran, \
                elec_rec, fs, mpf, d_threshold, dead, dead_point, used_energy)
    

            cluster_head, cluster_member, dead, dead_point, used_energy = \
            e_conf(cluster_head, cluster_member, pkt_control, elec_tran, elec_rec, \
                fs, mpf, d_threshold, dead, dead_point, max_distance, used_energy, cm_select)


            cache, send_or_not, collect_envi, check_super_round = \
            check_data(cluster_head, cluster_member, at1, at2, at3, at4, at5, at6, \
                at7, at8, at9, at10, at11, at12, at13, at14, at15, at16, at17, at18, \
                at19, t_value, cache, collect_envi, cm_select, count_sr)


            cluster_head, cluster_member, dead, dead_point, used_energy = \
            e_intra_sr(cluster_head, cluster_member, cm_select, pkt_data, elec_tran, \
                elec_rec, fs, mpf, d_threshold, dead, dead_point, used_energy, send_or_not)


            cluster_head, dead, dead_point, used_energy = \
            e_agg_sr(cluster_head, count_ch_member, pkt_data, elec_tran, dead_point, dead,\
              used_energy, send_or_not)


            cluster_head, bs_member, dead, dead_point, used_energy = \
            e_route_sr(cluster_head, bs_member, pkt_data, elec_tran, elec_rec, fs, mpf, \
                d_threshold, dead, dead_point, used_energy, send_or_not)
        else:
        
            cluster_head, cluster_member, dead, dead_point, used_energy = \
            e_intra(cluster_head, cluster_member, cm_select, pkt_data, elec_tran, \
                elec_rec, fs, mpf, d_threshold, dead, dead_point, used_energy)
                    
                    
            cluster_head, dead, dead_point, used_energy = \
            e_agg(cluster_head, count_ch_member, pkt_data, elec_tran, dead_point, \
                dead, used_energy)


            cluster_head, bs_member, dead, dead_point, used_energy = \
            e_route(cluster_head, bs_member, pkt_data, elec_tran, elec_rec, fs, \
                mpf, d_threshold, dead, dead_point, used_energy)

        
        if check_optimize_t == 0:
            cluster_head, cluster_member, dead, ch_t_compare, check_optimize_t = \
            optimize_t(cluster_head, cluster_member, cm_select, max_distance, decimal, \
                decrease_t, increase_t, r1, dead, check_optimize_t, ch_t_compare)


        # plot_graph(cluster_head, cluster_member, cch, bs_member, r1, r2, data_distance)
        
##
####        if len(ch_t_compare) == 0:
####            print(ch_t_compare)
##        if dead == 0:
##            check_ch = []
##            for ch in range(len(cluster_head)):
##                check_ch.append([count_lap,'ch',cluster_head[ch][:2],cluster_head[ch][2], ch_t_compare[ch][1], ch_t_compare[ch][2]])
        
        get_t = ch_t_compare
        cluster_member, count_sr, check_optimize_t, check_super_round, count_sr, cache, \
        collect_envi, ch_t_compare = \
        back_to_cm_dynamic(cluster_head, cluster_member, max_distance, r1, t_value, \
            count_lap, dead_round, dead, count_ch_member, len_cm, cm_out_of_range, \
            ch_t_compare, check_super_round, super_round, count_sr, check_optimize_t, \
            cache, collect_envi)

        
        check_ch = []
        if dead == 0:
            check_cm = []
            for ch in range(len(cluster_head)):
                check_ch.append([count_lap,'ch',cluster_head[ch][:2],cluster_head[ch][2],cluster_head[ch][3]])
            for cm in cluster_member:
                check_cm.append([count_lap,'cm',cm[:2],cm[2], cm[3]])
##            check_ch.sort()
##            check_cm.sort()
            with open('check ch.csv', 'a', newline='') as csvnew:
                write = csv.writer(csvnew)
                for line in check_ch:
                    write.writerow(line)
                write.writerow(' ')
            with open('check cm.csv', 'a', newline='') as csvnew:
                write = csv.writer(csvnew)
                for line in check_cm:
                    write.writerow(line)
                write.writerow(' ')
            with open('used energy SR '+str(super_round)+'.csv', 'a', newline='') as csvnew:
                writer = csv.DictWriter(csvnew,  used_energy.keys())
                if csvnew.tell == 0:
                    writer.writeheader()
                    writer.writerow(used_energy)
                else:
                    writer.writerow(used_energy)
            count_lap += 1
            used_energy = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0, '8':0,\
                   '9':0,'10':0,'11':0,'12':0}
        elif dead == 1:
            check_ch = []
            for ch in range(len(cluster_head)):
                check_ch.append([count_lap,'ch',cluster_head[ch][:2],cluster_head[ch][2],cluster_head[ch][3]])
            check_cm = []
            for cm in cluster_member:
                check_cm.append([count_lap,'cm',cm[:2],cm[2], cm[3]])
##            check_ch.sort()
##            check_cm.sort()
            with open('check ch.csv', 'a', newline='') as csvnew:
                write = csv.writer(csvnew)
                for line in check_ch:
                    write.writerow(line)
                write.writerow(' ')
            with open('check cm.csv', 'a', newline='') as csvnew:
                write = csv.writer(csvnew)
                for line in check_cm:
                    write.writerow(line)
                write.writerow(' ')
            print("rund"+str(t_value)+" DeadLAP : "+ str(count_lap-1))
            dead_point = [dead_point]
            with open('dead point SR '+str(super_round)+'.csv', 'a', newline='') as csvnew:
                write = csv.writer(csvnew)
                for line in dead_point:
                    write.writerow(line)
            log3 = [[t_value, count_lap]]
            with open('count lap SR '+str(super_round)+'.csv', 'a', newline='') as csvnew:
                write = csv.writer(csvnew)
                for line in log3:
                    write.writerow(line)
            break
    print(dead_round, end="\n")

width = 100 # meter
height = 100 # meter
density = float(0.0125)
num_base = 1
pos_base = "-50,50"
set_energy = 3 # set energy = 1 Joule
pkt_control = 200 # bit
pkt_data = 4000  # bit
d_threshold = 87  # **********************
r1 = 30 # meter
r2 = r1*((2*math.log(10))**(0.5)) # meter
decimal = 2
decrease_t = 0.01
increase_t = 0.01
super_round = 1

for l in range(1):
                start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
                        d_threshold, r1, r2, decimal, decrease_t, increase_t, l, super_round)


