import math
import random as rd
r1 =30
width = 50
height = 50
density = 0.025 
station_member = [-50, 0]
set_energy = 0.5
d_threshold = 87
pkt_control = 200 # bit
pkt_data = 4000  # bit
elec_tran = 50 * (10 ** (-9))  # 50 nanoj
elec_rec = 50 * (10 ** (-9))  # 50 nanoj
fs = 10 * (10 ** (-12))  # 10 picoj
mpf = 0.012 * (10 ** (-12))
keep_divi = (((width*height)/(math.pi*(r1**2))))/(width*height*density)
t_predefine = 0.2
node_member = []
len_nodes = math.ceil(density * (width * height)) 
# Random nodes
count = 0
while len(node_member) != len_nodes:
    random_x, random_y = rd.randint(0, width), rd.randint(0, height)
    if [random_x, random_y] not in node_member and \
       [random_x, random_y] not in station_member:
        node_member.append([random_x, random_y])
    count += 1
    
for main in range(len(node_member)):
    for other in range(len(node_member)):
        distance = math.sqrt((node_member[main][0] - node_member[other][0])**2 + \
                            (node_member[main][1] - node_member[other][1])**2)
        if  distance < d_threshold:
            wast = (elec_tran+(fs*(distance**2)))*pkt_control*keep_divi
##            print(float(wast))
            if t_predefine < wast and wast <=keep_divi:
                print('--')
            else:
                print(1, other, t_predefine, wast)
        elif distance >= d_threshold :
            wast = ((elec_tran+(mpf*(distance**4)))*pkt_control)*keep_divi
##            print(float(wast))
            if t_predefine < wast and wast <=keep_divi:
                 print('--')
            else:
                print(2, other, t_predefine, wast)
##divi = []
##for x in range(1,keep_width+1):
##    for y in range(1,keep_heigth+1):
##        divi.append([x*50, y*50])
##print(divi)
