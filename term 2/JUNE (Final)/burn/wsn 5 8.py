import random as rd
import math
import matplotlib.pyplot as plt
import csv
import sys
##sys.setrecursionlimit(10000)

def base_bs(num_base, pos_base, super_round, diff_per):
    """input bs point"""
    # Set POS bs here
    bs_member = []
    for _ in range(num_base):
        bs_member.append(map(int, pos_base.split(',')))
    # append data to csv. file
    with open('bs_member SR '+str(super_round)+' '+str(diff_per)+'.csv', 'w', newline='') as csvnew:
        write = csv.writer(csvnew)
        for line in bs_member:
            write.writerow(line)

    return bs_member

        
def random_cm(width, height, set_energy, density, t_value, super_round, diff_per):
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
            cm_original.append([ random_x, random_y, set_energy, t_value, data_set, count+1])
        count += 1
    # append data to csv. file
    with open('cm_original SR '+str(super_round)+' '+str(diff_per)+'.csv', 'w', newline='') as csvnew:
        write = csv.writer(csvnew)
        for line1 in cm_original:
            write.writerow(line1)
    with open('len_cm SR '+str(super_round)+' '+str(diff_per)+".txt", "w") as text_file:
        text_file.write(str(len_cm))

    return cm_original, len_cm


def random_cch(cm_original, len_cm, super_round, diff_per, count_lap, dead, decimal):
    """random cch from amount Node"""
    cch = []
    cluster_member = []

    if dead == 0:
        # random candidate cluster
        for cm in cm_original:
            prob_v = round(rd.uniform(0, 1), decimal)
            if prob_v <= cm[3]:
                cch.append(cm)
        cluster_member = [i for i in cm_original if i not in cch]

        if len(cch) == 0:
            random_cch(cm_original, len_cm, super_round, diff_per, count_lap, dead)
            
##        with open('check cch SR '+str(super_round)+' '+str(diff_per)+'.csv', 'a', newline='') as csvnew:
##            write = csv.writer(csvnew)
##            for line in cch:
##                write.writerow([count_lap, line[0],line[1],line[2], line[3]])
##            write.writerow('')

    return cch, cluster_member 


def comp_1(cch, r1, dead, cm_original, super_round, diff_per):
    me_ch = []
    shutdown = []

    if dead == 0:
        # sort by energy [from most to least]
        for lap in range(len(cch)-1,0,-1):
            for cm in range(lap):
                if cch[cm][2] < cch[cm+1][2]:
                    temp = cch[cm]
                    cch[cm] = cch[cm+1]
                    cch[cm+1] = temp
        # Choose who should be cluster member

        for main in range(len(cch)):
                state = []
                for other in range(len(cch)):
                    if cch[main] != cch[other]: # ทำให้ไม่เช็คตัวเอง
                        distance = math.sqrt((cch[main][0] - cch[other][0])**2 + (cch[main][1] - cch[other][1])**2)
                        if distance <= r1: # main - other  overlapกัน
                            if main < other: # main เลขน้อยเป็นต่อไปได้
                                state.append(1)
                            elif other < main: # other เลขน้อย shutdown ทันที
                                if cch[other] not in shutdown: # ถ้าตัว other ไม่เคยถูก shutdown ก่อนหน้านี้
                                    shutdown.append(cch[main])
                                    state.append(0)
                                    break
                                elif cch[other] in shutdown: # ถ้าเคยถูก shutdown มาก่อน
                                    state.append(1)
                        else: # main - other  ไม่overlapกัน
                            state.append(1)
                if 0 not in state:
                    me_ch.append(cch[main])
        
        # # print(count_lap, "Before len cch : ", len(me_ch))
        # cut_out = []
        # for ch in me_ch:
        #     first, other = me_ch[0][2], ch[2] 
        #     diff = abs(((first - other) / first)*100)
        #     if diff >= 80:
        #         # print(me_ch[0][2], ch[2])
        #         cut_out.append(ch)

    return me_ch, shutdown


def e_comp(me_ch, cch, pkt_control, elec_tran, elec_rec, fs, \
        mpf, d_threshold, dead, r1, dead_point, used_energy):
    
    # BROADCAST
    if dead == 0:
        # Calculate all energy use to send/Receive pkt control
        for main in range(len(me_ch)):
            # Send pkt control
            if  r1 < d_threshold:
                e_tx = (elec_tran + (fs*(r1**2)))*pkt_control
                if me_ch[main][2] - e_tx > 0:
                    me_ch[main][2] = me_ch[main][2] - e_tx
                    used_energy['1'] = used_energy.get('1')+e_tx
                else:
                    dead_point = me_ch[main]
                    dead_point.append('1')
                    dead = 1
            elif r1 >= d_threshold:
                e_tx = (elec_tran + (mpf*(r1**2)))*pkt_control
                if me_ch[main][2] - e_tx > 0:
                    me_ch[main][2] = me_ch[main][2] - e_tx
                    used_energy['1'] = used_energy.get('1')+e_tx
                else:
                    dead_point = me_ch[main]
                    dead_point.append('1')
                    dead = 1
            for other in range(len(cch)):
                distance = math.sqrt((cch[main][0] - cch[other][0])**2 + \
                                (cch[main][1] - cch[other][1])**2)
                e_rx = elec_rec*pkt_control
                # Receive pkt control
                if distance <= r1 and distance != 0: # if its in range of r1 its can recieve
                    if cch[other][2] - e_rx > 0:
                        cch[other][2] = cch[other][2] - e_rx
                        used_energy['2'] = used_energy.get('2')+e_rx
                    else:
                        dead_point = cch[other]
                        dead_point.append('2')
                        dead = 0
            
            
    return dead, cch, dead_point, used_energy


def comp_2(me_ch, shutdown, cluster_member, dead, super_round, diff_per):
    cluster_head = []       
    
    if dead == 0:
        for ch in me_ch:
            cluster_head.append(ch)
##            with open('cluster data SR '+str(super_round)+' '+str(diff_per)+'.csv', 'a', newline='') as csvnew:
##                write = csv.writer(csvnew)
##                for line in [ch]:
##                    write.writerow(line)
##        with open('cluster data SR '+str(super_round)+' '+str(diff_per)+'.csv', 'a', newline='') as csvnew:
##                write = csv.writer(csvnew)
##                write.writerow('')
        for cm in shutdown:
            cluster_member.append(cm)

    return cluster_head, cluster_member


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
                    else:
                        dead_point = cluster_head[ch]
                        dead_point.append('3')
                        dead = 1
                elif r2 >= d_threshold :
                    e_tx = ((elec_tran + (mpf*(r2**4)))*pkt_control)
                    if cluster_head[ch][2] - e_tx  > 0:
                        cluster_head[ch][2] = cluster_head[ch][2] - e_tx
                        used_energy['3'] = used_energy.get('3')+e_tx
                    else:
                        dead_point = cluster_head[ch]
                        dead_point.append('3')
                        dead = 1
                for cm in range(len(cluster_member)):
                    distance = math.sqrt((cluster_member[cm][0] - cluster_head[ch][0])**2 +
                                        (cluster_member[cm][1] - cluster_head[ch][1])**2)
                    # Receive pkt control
                    e_rx = elec_rec*pkt_control
                    if distance <= r2:
                        if cluster_member[cm][2] - e_rx > 0:
                            cluster_member[cm][2] = cluster_member[cm][2] - e_rx
                            used_energy['4'] = used_energy.get('4')+e_rx
                        else:
                            dead_point = cluster_member[cm]
                            dead_point.append('4')
                            dead = 1


    return cluster_head, cluster_member, dead, dead_point, used_energy

def cm_choose_ch(cluster_head, cluster_member, r2, dead):
    cm_select = []
    log_cm_select = []
    amount_cm_in_ch = {}
    
    if dead == 0:
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
                    elif distance > r2 and check == 0:
                        shotest = -1
                        what_cluster = -1
                cm_select.append([what_cluster, shotest])
                log_cm_select.append([what_cluster, shotest])
        

    return cm_select, log_cm_select, amount_cm_in_ch


def e_join(cluster_head, cluster_member, cm_select, pkt_control, elec_tran,\
            elec_rec, fs, mpf, d_threshold, dead, dead_point, used_energy):
    # UNICAST
    if dead == 0:
        # ch receive all pkt control from cm
        for cm in range(len(cluster_member)):
            if cm_select[cm][1] > 0:
                # Send pkt control [cm-->ch]
                if  cm_select[cm][1] < d_threshold:
                    e_tx = ((elec_tran + (fs*(cm_select[cm][1]**2)))*pkt_control)
                    if cluster_member[cm][2] - e_tx  > 0:
                        cluster_member[cm][2] = cluster_member[cm][2] - e_tx
                        used_energy['5'] = used_energy.get('5')+e_tx
                    else:
                        dead_point = cluster_member[cm]
                        dead_point.append('5')
                        dead = 1
                elif cm_select[cm][1] >= d_threshold :
                    e_tx = ((elec_tran + (mpf*(cm_select[cm][1]**4)))*pkt_control)
                    if cluster_member[cm][2] - e_tx  > 0:
                        cluster_member[cm][2] = cluster_member[cm][2] - e_tx
                        used_energy['5'] = used_energy.get('5')+e_tx
                    else:
                        dead_point = cluster_member[cm]
                        dead_point.append('5')
                        dead = 1
                # Receive pkt control
                e_rx = elec_rec*pkt_control
                if cluster_head[cm_select[cm][0]][2] - e_rx > 0:
                    cluster_head[cm_select[cm][0]][2] = cluster_head[cm_select[cm][0]][2] - e_rx
                    used_energy['6'] = used_energy.get('6')+e_rx
                else:
                    dead_point = cluster_member[cm]
                    dead_point.append('6')
                    dead = 1

    return cluster_head, cluster_member, dead, dead_point, used_energy


def calculate_some_data(cm_select, log_cm_select, amount_cm_in_ch, dead):
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
        # collect how many nodes out of range
        for i in cm_select:
            if i[0] == -1:
                cm_out_of_range += 1
            

    return max_distance, count_ch_member, cm_out_of_range, dead


def e_conf(cluster_head, cluster_member, pkt_control, elec_tran, \
        elec_rec, fs, mpf, d_threshold, dead, dead_point, max_distance, used_energy):
    # BROADCAST
    # Maybe use max_distance[ch][1]
    if dead == 0:
        # ch send confirm pkt control to cm
        for ch in range(len(cluster_head)):
            # Send pkt control
            if  max_distance[ch][1] < d_threshold:
                e_tx = ((elec_tran + (fs*(max_distance[ch][1]**2)))*pkt_control)
                if cluster_head[ch][2] - e_tx > 0 : 
                    cluster_head[ch][2] = cluster_head[ch][2] - e_tx
                    used_energy['7'] = used_energy.get('7')+e_tx
                else:
                    dead_point = cluster_head[ch]
                    dead_point.append('7')
                    dead = 1
            elif max_distance[ch][1] >= d_threshold :
                e_tx = ((elec_tran + (mpf*(max_distance[ch][1]**4)))*pkt_control)
                if cluster_head[ch][2] - e_tx  > 0:
                    cluster_head[ch][2] = cluster_head[ch][2] - e_tx
                    used_energy['7'] = used_energy.get('7')+e_tx
                else:
                    dead_point = cluster_head[ch]
                    dead_point.append('7')
                    dead = 1
            for cm in range(len(cluster_member)):
                distance = math.sqrt((cluster_member[cm][0] - cluster_head[ch][0])**2 +
                                    (cluster_member[cm][1] - cluster_head[ch][1])**2)
                # Receive pkt control
                e_rx = elec_rec*pkt_control
                if distance <= max_distance[ch][1]:
                    if cluster_member[cm][2] - e_rx > 0:
                        cluster_member[cm][2] = cluster_member[cm][2] - e_rx
                        used_energy['8'] = used_energy.get('8')+e_rx
                    else:
                        dead_point = cluster_member[cm]
                        dead_point.append('8')
                        dead = 1

    return cluster_head, cluster_member, dead, dead_point, used_energy


def check_data(cluster_head, cluster_member, cache, collect_envi, \
        cm_select, count_sr, diff_per, dead, diff_per_ch, super_round, count_lap, collect_times):

    # pull data
    at1, at2, at3, at4, at5, at6, at7, at8, at9, at10, \
    at11, at12, at13, at14, at15, at16, at17, at18, at19 = \
        [], [], [], [], [], [], [], [], [] ,[], [], [], [], [], [], [], [], [], []
    count = 1
    with open('place.csv', 'r', newline='') as csvnew:
        read = csv.reader(csvnew)
        for line in read:
            eval('at%d'% (count)).append(line)
            count += 1
    
    # calculate how many percentage difference of data between each round.
    send_or_not = []
    check_super_round = 1
    real_send = [count_lap, len(cluster_member)]
    
    if dead == 0:
        # cm
        if count_sr == 0:
            sum_origi_ch = [ [] for _ in range(len(cluster_head))]
            for cm in range(len(cluster_member)):
                sum_origi_ch[cm_select[cm][0]].append( float(eval('at%d'% (cluster_member[cm][4]))[0][cache]))
                send_or_not.append([cluster_member[cm][5], 1])
                collect_envi.append([cluster_member[cm][5], eval('at%d'% (cluster_member[cm][4]))[0][cache]])
            real_send.append(len(cluster_member))
        else:
            real_cm_send  = 0
            sum_origi_ch = [ [] for _ in range(len(cluster_head))]
            for cm in range(len(cluster_member)):
                sum_cm = 0
                count = 0
                for cec in collect_envi:
                    if cluster_member[cm][5] == cec[0]:
                        old = float(cec[1])
                        new = float(eval('at%d'% (cluster_member[cm][4]))[0][cache])
                        diff = abs((new-old)/old)*100
                        sum_origi_ch[cm_select[cm][0]].append( eval('at%d'% (cluster_member[cm][4]))[0][cache])
                        if diff >= diff_per:
                            real_cm_send += 1 # real CM send
                            send_or_not.append([cluster_member[cm][5], 1])
                            cec[1] = new
                        else:
                            send_or_not.append([cluster_member[cm][5], 0])
                    count += 1
            real_send.append(real_cm_send)
        # ch
        real_send.append(len(cluster_head))
        sum_envi_ch = [ [] for _ in range(len(cluster_head))]
        for cm in range(len(cluster_member)):
            sum_envi_ch[cm_select[cm][0]].append(float(collect_envi[cm][1]))
        if count_sr == 0:
            ch_change = []
            bs_change = []
            origi = []
            real_send.append(len(cluster_head))
            for ch in range(len(cluster_head)):
                sum_origi_ch[ch].append(float(eval('at%d'% (cluster_head[ch][4]))[0][cache]))
                sum_envi_ch[ch].append(float(eval('at%d'% (cluster_head[ch][4]))[0][cache]))
            for ch in range(len(cluster_head)):
                ch_avg = 0
                send_or_not.append([cluster_head[ch][5], 1])
                collect_envi.append([cluster_head[ch][5], sum(sum_envi_ch[ch])/ float(len(sum_envi_ch[ch]))])# avg of ch
                ch_change.append([count_lap,ch, sum(sum_envi_ch[ch])/ float(len(sum_envi_ch[ch]))])
                bs_change.append([count_lap,ch, sum(sum_envi_ch[ch])/ float(len(sum_envi_ch[ch]))])
            with open('data at ch '+str(super_round)+' '+str(diff_per)+'.csv', 'a', newline='') as csvnew:
                write = csv.writer(csvnew)
                for item in ch_change:
                    write.writerow(item)
            with open('data at bs '+str(super_round)+' '+str(diff_per)+'.csv', 'a', newline='') as csvnew:
                write = csv.writer(csvnew)
                for item in bs_change:
                    write.writerow(item)
        else:
            ch_change = []
            bs_change = []
            ch_current = [count_lap,count_sr+1]
            real_ch_send = 0
            sum_origi_ch = [ [] for _ in range(len(cluster_head))]
            for cm in range(len(cluster_member)):
                sum_origi_ch[cm_select[cm][0]].append( float(eval('at%d'% (cluster_member[cm][4]))[0][cache]))
            x = 0
            for ch in range(len(cluster_head)):
                sum_origi_ch[ch].append(float(eval('at%d'% (cluster_head[ch][4]))[0][cache]))
                sum_envi_ch[ch].append(float(eval('at%d'% (cluster_head[ch][4]))[0][cache]))
            count = 0
            for ch in range(len(cluster_head)):
                for cec in collect_envi:
                    if cluster_head[ch][5] == cec[0]:
                        old = float(cec[1])
                        origi = sum(sum_origi_ch[ch])/ float(len(sum_origi_ch[ch]))
                        new = sum(sum_envi_ch[ch])/ float(len(sum_envi_ch[ch]))
                        diff = abs((new-old)/old)*100
                        y = [count_lap,ch,origi,old, new]
                        if diff >= diff_per_ch:
                            x = [count_lap,ch,origi,old, new, new]
                            offen = [count_lap,ch,count]
                            count +=1
                            real_ch_send += 1 # real CM send
                            send_or_not.append([cluster_head[ch][5], 1])
                            cec[1] = new
                            # collect amount of times ch not send
                            collect_times[ch].append(0)
                        else:
                            x = [count_lap,ch,origi,old,new,old]
                            send_or_not.append([cluster_head[ch][5], 0])
                            # collect amount of times ch not send
                            collect_times[ch].append(1)
                ch_change.append(y)
                bs_change.append(x)
            with open('data at ch '+str(super_round)+' '+str(diff_per)+'.csv', 'a', newline='') as csvnew:
                write = csv.writer(csvnew)
                for item in ch_change:
                    write.writerow(item)
            with open('data at bs '+str(super_round)+' '+str(diff_per)+'.csv', 'a', newline='') as csvnew:
                write = csv.writer(csvnew)
                for item in bs_change:
                    write.writerow(item)
        cache += 1
        with open('real send '+str(super_round)+' '+str(diff_per)+'.csv', 'a', newline='') as csvnew:
            write = csv.writer(csvnew)
            for line in [real_send]:
                write.writerow(line)
    return cache, send_or_not, collect_envi, check_super_round

def e_intra_sr(cluster_head, cluster_member, cm_select, pkt_data, elec_tran,\
                    elec_rec, fs, mpf, d_threshold, dead, dead_point, used_energy, send_or_not):
    # UNICAST
    if dead == 0:
        # ch receive all pkt data from cm
        for cm in range(len(cluster_member)):
            for son in send_or_not:
                if cm_select[cm][1] != 0 and cluster_member[cm][5] == son[0] and son[1] == 1:
                    # Send pkt data [cm-->ch]
                    if  cm_select[cm][1] < d_threshold:
                        e_tx = ((elec_tran + (fs*(cm_select[cm][1]**2)))*pkt_data)
                        if cluster_member[cm][2] - e_tx  > 0:
                            cluster_member[cm][2] = cluster_member[cm][2] - e_tx
                            used_energy['9'] = used_energy.get('9')+e_tx
                        else:
                            dead_point = cluster_member[cm]
                            dead_point.append('9')
                            dead = 1
                    elif cm_select[cm][1] >= d_threshold :
                        e_tx = ((elec_tran + (mpf*(cm_select[cm][1]**4)))*pkt_data)
                        if cluster_member[cm][2] - e_tx  > 0:
                            cluster_member[cm][2] = cluster_member[cm][2] - e_tx
                            used_energy['9'] = used_energy.get('9')+e_tx
                        else:
                            dead_point = cluster_member[cm]
                            dead_point.append('9')
                            dead = 1
                    # Receive pkt data
                    e_rx = elec_rec*pkt_data
                    if cluster_head[cm_select[cm][0]][2] - e_rx > 0:
                        cluster_head[cm_select[cm][0]][2] = cluster_head[cm_select[cm][0]][2] - e_rx
                        used_energy['10'] = used_energy.get('10')+e_rx
                    else:
                        dead_point = cluster_member[cm]
                        dead_point.append('10')
                        dead = 1   

    return cluster_head, cluster_member, dead, dead_point, used_energy

def e_agg_sr(cluster_head, count_ch_member, pkt_data, fs, dead_point, dead,\
          used_energy, send_or_not):
    # summarize data
    if dead == 0:
        for ch in range(len(cluster_head)):
            for son in send_or_not:
                if cluster_head[ch][5] == son[0] and son[1] == 1 and used_energy['10'] != 0:
                    e_agg = (count_ch_member[ch]+1)*(5*(10**(-9)))
                    if cluster_head[ch][2] - e_agg > 0:
                        cluster_head[ch][2] -= e_agg
                        used_energy['11'] = used_energy.get('11')+e_agg
                    else:
                        dead_point = cluster_head[ch]
                        dead_point.append('11')
                        dead = 1

    return cluster_head, dead, dead_point,  used_energy


def e_route_sr(cluster_head, bs_member, pkt_data, elec_tran, elec_rec, fs, mpf, \
        d_threshold, dead, dead_point, used_energy, send_or_not, super_round, diff_per):
    # UNICAST
    if dead == 0:
        base_x, base_y = zip(*bs_member)
        for ch in range(len(cluster_head)):
            # Send pkt data [clsuter-->bs]
            for son in send_or_not:
                if cluster_head[ch][5] == son[0] and son[1] == 1 and used_energy['10'] != 0:
                    distance = math.sqrt((int(base_x[0] - cluster_head[ch][0])**2 + int(base_y[0] - cluster_head[ch][1])**2))
                    e_tx = (elec_tran + (mpf*(distance**4)))*pkt_data
                    if cluster_head[ch][2] - e_tx  > 0:
                        cluster_head[ch][2] = cluster_head[ch][2] - e_tx
                        used_energy['12'] = used_energy.get('12')+e_tx
                    else:
                        dead_point = cluster_head[ch]
                        dead_point.append('12')
                        dead = 1
        

    return cluster_head, bs_member, dead, dead_point, used_energy

def optimize_t(cluster_head, cluster_member, cm_select, max_distance, decimal, \
                decrease_t, increase_t, r1, dead, check_optimize_t, ch_t_compare):
    
    # optimize the t-value in the next round
    # [Energy] -->  cluster_member[cm][2], cluster_head[ch][2]
    # [T-Value] --> cluster_member[cm][3], cluster_head[ch][3]
    check_optimize_t = 1
    if dead == 0:
        avg_e_ch = [ [] for _ in range(len(cluster_head))] # build list to collect E for each CH
        
        for ch in range(len(cluster_head)):
            avg_e_ch[ch].append(cluster_head[ch][2]) # ch add data
        for cm in range(len(cluster_member)):
            avg_e_ch[cm_select[cm][0]].append(cluster_member[cm][2]) # cm add data  
        for ch in range(len(cluster_head)):
            
            e_avg = sum(avg_e_ch[ch]) / len(avg_e_ch[ch]) # find AVG each list of CH
            energy = cluster_head[ch][2]
            if max_distance[ch][1] > r1:
                if cluster_head[ch][3] < 1:
                    diff = energy/e_avg
                    if diff > 1.1:
                        ch_t_compare.append([ch, cluster_head[ch][3], round(cluster_head[ch][3] + 0.01, decimal)])
                        cluster_head[ch][3] =  round(cluster_head[ch][3] + 0.01, decimal)
                    elif diff > 0.9 and diff <= 1.1:
                        t_change = abs(diff-0.9)*0.05
                        ch_t_compare.append([ch, cluster_head[ch][3], round(cluster_head[ch][3] + t_change, decimal)])
                        cluster_head[ch][3] =  round(cluster_head[ch][3] + t_change, decimal)
                    elif diff <= 0.9:
                        ch_t_compare.append([ch, cluster_head[ch][3], round(cluster_head[ch][3] + 0.000, decimal)])
                        cluster_head[ch][3] =  round(cluster_head[ch][3] + 0.000, decimal)
                else:
                    ch_t_compare.append([ch, cluster_head[ch][3], cluster_head[ch][3]])
                    
            elif max_distance[ch][1] < r1:
                if cluster_head[ch][3] > 0:
                    diff = energy/e_avg
                    if diff > 1.1:
                        ch_t_compare.append([ch, cluster_head[ch][3], round(cluster_head[ch][3] - 0.000, decimal)])
                        cluster_head[ch][3] =  round(cluster_head[ch][3] - 0.000, decimal)
                    elif diff > 0.9 and diff <= 1.1:
                        t_change = abs(((1.1 - diff))*0.05)
                        ch_t_compare.append([ch, cluster_head[ch][3], round(cluster_head[ch][3] - t_change, decimal)])
                        cluster_head[ch][3] =  round(cluster_head[ch][3] - t_change, decimal)

                    elif diff <= 0.9:
                        ch_t_compare.append([ch, cluster_head[ch][3], round(cluster_head[ch][3] - 0.01, decimal)])
                        cluster_head[ch][3] =  round(cluster_head[ch][3] - 0.01, decimal)
                else:
                    ch_t_compare.append([ch, cluster_head[ch][3], cluster_head[ch][3]])
            else:
                ch_t_compare.append([ch, cluster_head[ch][3], cluster_head[ch][3]])

        for d in range(len(max_distance)):
            e_avg = sum(avg_e_ch[d]) / len(avg_e_ch[d]) # find AVG each list of CH
            
            for cm in range(len(cluster_member)):
                energy = cluster_member[cm][2]
                if cm_select[cm][0] == max_distance[d][0]:
                    if max_distance[d][1] > r1:
                        if cluster_member[cm][3] < 1:
                            diff = energy/e_avg
                            if diff > 1.1:
                                cluster_member[cm][3] =  round(cluster_member[cm][3] + 0.01, decimal)
                            elif diff > 0.9 and diff <= 1.1:                                
                                t_change = abs(diff-0.9)*0.05
                                cluster_member[cm][3] =  round(cluster_member[cm][3] + t_change, decimal)
                            elif diff <= 0.9:
                                cluster_member[cm][3] =  round(cluster_member[cm][3] + 0.000, decimal)
                    elif max_distance[d][1] < r1:
                        if cluster_member[cm][3] > 0:
                            
                            diff = energy/e_avg
                            if diff > 1.1:
                                cluster_member[cm][3] =  round(cluster_member[cm][3] - 0.000, decimal)
                            elif diff > 0.9 and diff <= 1.1:
                                t_change = abs(((1.1 - diff))*0.05)
                                cluster_member[cm][3] =  round(cluster_member[cm][3] - t_change, decimal)
                            elif diff <= 0.9:
                                cluster_member[cm][3] =  round(cluster_member[cm][3] - 0.01, decimal)

    return cluster_head, cluster_member, dead, ch_t_compare, check_optimize_t


def back_to_cm_dynamic(cluster_head, cluster_member, max_distance, count_lap, \
        dead_round, dead, count_ch_member, len_cm, cm_out_of_range, ch_t_compare, \
        check_super_round, super_round, count_sr, check_optimize_t, cache, collect_envi, diff_per, collect_times):
    """ before next loop all cluster switch back to node_member """
    # collect data highest distance from each cluster
    if dead == 0:
        log1 =[]
        for d in max_distance:
            if d[1] != 0:
                log1.append([dead_round, count_lap, d[1], ch_t_compare[d[0]][1], ch_t_compare[d[0]][2]])
        with open('data t and rd SR '+str(super_round)+' '+str(diff_per) +'.csv', 'a', newline='') as csvnew:
            write = csv.writer(csvnew)
            for line1 in log1:
                write.writerow(line1)

        log2= [[count_lap, len(cluster_head), count_ch_member, len_cm, len_cm-cm_out_of_range]]
##        with open('data cluster SR '+str(super_round)+' '+str(diff_per)+'.csv', 'a', newline='') as csvnew:
##            write = csv.writer(csvnew)
##            for line in log2:
##                write.writerow(line)
        count_sr += 1
        # print(count_sr," -> ", super_round)
        if check_super_round == 1 and count_sr == super_round:
            check_optimize_t = 0
            check_super_round = 0
            count_sr = 0
            ch_t_compare = []
            collect_envi = []
            # collect amount of times ch not send
            cache_ct = 0
            log1 = []
            for i in collect_times:
                cache_ct += sum(i)
            log1.append([count_lap, math.ceil(cache_ct/len(collect_times))])
            
            with open('offen send SR '+str(super_round)+' '+str(diff_per) +'.csv', 'a', newline='') as csvnew:
                write = csv.writer(csvnew)
                for line1 in log1:
                    write.writerow(line1)
            for ch in cluster_head:
                if ch not in cluster_member:
                    cluster_member.append(ch)
    return cluster_member, count_sr, check_optimize_t, check_super_round, count_sr, cache, collect_envi, ch_t_compare


def start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
          d_threshold, r1, r2, decimal, decrease_t, increase_t, dead_round, super_round, diff_per, diff_per_ch):
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
    base_bs(num_base, pos_base, super_round, diff_per)

    cm_original, len_cm = \
    random_cm(width, height, set_energy, density, t_value, super_round, diff_per)

    # Suprer Round Checking
    check_super_round = 0
    check_optimize_t = 0
    count_sr = 0
    cache = 0
    collect_envi = []
    ch_t_compare = []
    count_lap = 1
    dead = 0

    bs_member, cm_original = [], []

    with open('bs_member SR '+str(super_round)+' '+str(diff_per)+".csv", 'r') as csvnew:
        read = csv.reader(csvnew)
        for line1 in read:
            bs_member.append(list(map(int, line1)))
    with open('cm_original SR '+str(super_round)+' '+str(diff_per)+".csv", 'r') as csvnew:
        read = csv.reader(csvnew)
        for line2 in read:
            cm_original.append(list(map(float, line2)))
    while True:
        with open('len_cm SR '+str(super_round)+' '+str(diff_per)+".txt", "r") as text_file:
            len_cm = int(text_file.read())

        if cache > 4608 - 1:
            cache = 0

        if check_super_round == 0:

            cch, cluster_member = \
            random_cch(cm_original, len_cm, super_round, diff_per, count_lap, dead, decimal)

            # ----------------------------------------------------------------------------------
            me_ch, shutdown = \
            comp_1(cch, r1, dead, cm_original, super_round, diff_per)

            dead, cch, dead_point, used_energy = \
            e_comp(me_ch, cch, pkt_control, elec_tran, elec_rec, fs, mpf, d_threshold, \
                dead, r1, dead_point, used_energy)

            cluster_head, cluster_member = \
            comp_2(me_ch, shutdown, cluster_member, dead, super_round, diff_per)

            # collect amount of times ch not send
            collect_times = [ [] for _ in range(len(cluster_head))]
            # ----------------------------------------------------------------------------------
            
            cluster_head, cluster_member, dead, dead_point, used_energy = \
            e_dis(cluster_head, cluster_member, pkt_control, elec_tran, \
                elec_rec, fs, mpf, d_threshold, dead, r2, dead_point, used_energy)

        cm_select, log_cm_select, amount_cm_in_ch = \
        cm_choose_ch(cluster_head, cluster_member, r2, dead)

        if check_super_round == 0:
            cluster_head, cluster_member, dead, dead_point, used_energy = \
            e_join(cluster_head, cluster_member, cm_select, pkt_control, elec_tran,\
                elec_rec, fs, mpf, d_threshold, dead, dead_point, used_energy)

            max_distance, count_ch_member, cm_out_of_range, dead = \
            calculate_some_data(cm_select, log_cm_select, amount_cm_in_ch, dead)
    
            cluster_head, cluster_member, dead, dead_point, used_energy = \
            e_conf(cluster_head, cluster_member, pkt_control, elec_tran, \
                elec_rec, fs, mpf, d_threshold, dead, dead_point, max_distance, used_energy)

        cache, send_or_not, collect_envi, check_super_round = \
        check_data(cluster_head, cluster_member, cache, collect_envi, cm_select, count_sr, \
            diff_per, dead, diff_per_ch, super_round, count_lap, collect_times)

        cluster_head, cluster_member, dead, dead_point, used_energy = \
        e_intra_sr(cluster_head, cluster_member, cm_select, pkt_data, elec_tran,\
            elec_rec, fs, mpf, d_threshold, dead, dead_point, used_energy, send_or_not)

        cluster_head, dead, dead_point, used_energy = \
        e_agg_sr(cluster_head, count_ch_member, pkt_data, fs, dead_point, dead,\
          used_energy, send_or_not)

        cluster_head, bs_member, dead, dead_point, used_energy = \
        e_route_sr(cluster_head, bs_member, pkt_data, elec_tran, elec_rec, fs, mpf, \
            d_threshold, dead, dead_point, used_energy, send_or_not, super_round, diff_per)

        if check_optimize_t == 0:
            cluster_head, cluster_member, dead, ch_t_compare, check_optimize_t = \
            optimize_t(cluster_head, cluster_member, cm_select, max_distance, decimal, \
                decrease_t, increase_t, r1, dead, check_optimize_t, ch_t_compare)

        cluster_member, count_sr, check_optimize_t, check_super_round, count_sr, cache, \
        collect_envi, ch_t_compare = \
        back_to_cm_dynamic(cluster_head, cluster_member, max_distance, count_lap, \
            dead_round, dead, count_ch_member, len_cm, cm_out_of_range, ch_t_compare, \
            check_super_round, super_round, count_sr, check_optimize_t, cache, collect_envi, diff_per, collect_times)

        check_ch = []
        if dead == 0:
            check_cm = []
            for ch in range(len(cluster_head)):
                check_ch.append([count_lap,'ch',cluster_head[ch][:2],cluster_head[ch][2],cluster_head[ch][3]])
            for cm in cluster_member:
                check_cm.append([count_lap,'cm',cm[:2],cm[2], cm[3]])
##            with open('check ch SR '+str(super_round)+' '+str(diff_per)+'.csv', 'a', newline='') as csvnew:
##                write = csv.writer(csvnew)
##                for line in check_ch:
##                    write.writerow(line)
##                write.writerow(' ')
##            with open('check cm SR '+str(super_round)+' '+str(diff_per)+'.csv', 'a', newline='') as csvnew:
##                write = csv.writer(csvnew)
##                for line in check_cm:
##                    write.writerow(line)
##                write.writerow(' ')
            with open('used energy SR '+str(super_round)+' '+str(diff_per)+'.csv', 'a', newline='') as csvnew:
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
            for ch in range(len(cluster_head)):
                check_ch.append([count_lap,'ch',cluster_head[ch][:2],cluster_head[ch][2],cluster_head[ch][3]])
            check_cm = []
            for cm in cluster_member:
                check_cm.append([count_lap,'cm',cm[:2],cm[2], cm[3]])
##            with open('check ch SR '+str(super_round)+' '+str(diff_per)+'.csv', 'a', newline='') as csvnew:
##                write = csv.writer(csvnew)
##                for line in check_ch:
##                    write.writerow(line)
##                write.writerow(' ')
##            with open('check cm SR '+str(super_round)+' '+str(diff_per)+'.csv', 'a', newline='') as csvnew:
##                write = csv.writer(csvnew)
##                for line in check_cm:
##                    write.writerow(line)
##                write.writerow(' ')
            print("rund"+str(t_value)+" DeadLAP : "+ str(count_lap-1))
            with open('used energy SR '+str(super_round)+' '+str(diff_per)+'.csv', 'a', newline='') as csvnew:
                writer = csv.DictWriter(csvnew, used_energy.keys())
                if csvnew.tell == 0:
                    writer.writeheader()
                    writer.writerow(used_energy)
                else:
                    writer.writerow(used_energy)

            dead_point = [dead_point]
            with open('dead point SR '+str(super_round)+' '+str(diff_per)+'.csv', 'a', newline='') as csvnew:
                write = csv.writer(csvnew)
                for line in dead_point:
                    write.writerow(line)
            log3 = [[t_value, count_lap]]
            with open('count lap SR '+str(super_round)+' '+str(diff_per)+'.csv', 'a', newline='') as csvnew:
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
set_energy = 3# set energy = 1 Joule
pkt_control = 200 # bit
pkt_data = 4000  # bit
d_threshold = 87  # **********************
r1 = 30 # meter
r2 = r1*((2*math.log(10))**(0.5)) # meter
decimal = 6
decrease_t = 0.01
increase_t = 0.01
super_round = 5
diff_per = 8
diff_per_ch = 1

for l in range(100):
    if l == 0:
        header = ['A1','B1','C1']
        header1 = ['lap','num CM','CM send','num CH','CH send']
        fields = ['A1','B1','C1','D1','E1','F1','G1','H1','I1','J1','K1','L1']
        with open('data t and rd SR '+str(super_round)+' '+str(diff_per) +'.csv', 'a', newline='') as csvnew:
            write = csv.writer(csvnew)
            write.writerow(header)
        with open('used energy SR '+str(super_round)+' '+str(diff_per) +'.csv', 'a', newline='') as csvnew:
            write = csv.writer(csvnew)
            write.writerow(fields)
        with open('real send '+str(super_round)+' '+str(diff_per) +'.csv', 'a', newline='') as csvnew:
            write = csv.writer(csvnew)
            write.writerow(header1)
        with open('offen send SR '+str(super_round)+' '+str(diff_per) +'.csv', 'a', newline='') as csvnew:
            write = csv.writer(csvnew)
            write.writerow(header[:2])
        print('start')
    start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
            d_threshold, r1, r2, decimal, decrease_t, increase_t, l, super_round, diff_per, diff_per_ch)
