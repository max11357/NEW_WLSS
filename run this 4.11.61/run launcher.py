import multiprocessing
import math
import run1
import run2
import rundnm1
import time

width = 100 # meter
height = 100 # meter
density = float(0.0125)
num_base = 1
pos_base = "0,0"
set_energy = 1 # set energy = 1 Joule
pkt_control = 200 # bit
pkt_data = 4000  # bit
d_threshold = 87  # **********************
r1 = 30 # meter
r2 = r1*((2*math.log(10))**(0.5)) # meter
decimal = 2
decrease_t = 0.01
increase_t = 0.01

def runn1(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
        d_threshold, r1, r2, lap):
        for l in lap:
                run1.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
                        d_threshold, r1, r2, l)

    
def runn2(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
        d_threshold, r1, r2, lap):
        for l in lap:
                run2.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
                        d_threshold, r1, r2, l)

def runndnm1(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
        d_threshold, r1, r2, decimal, decrease_t, increase_t, lap):
        for l in lap:
                rundnm1.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
                        d_threshold, r1, r2, decimal, decrease_t, increase_t, l)

# if __name__ == "__main__":
#         t1 = time.time()
#         p1 = multiprocessing.Process(target=runn1, args=(range(1,201),))
#         p2 = multiprocessing.Process(target=runn2, args=(range(1,201),))
#         pdnm1 = multiprocessing.Process(target=rundnm1, args=(range(1,2),))

#         p1.start()
#         p2.start()
#         pdnm1.start()

#         p1.join()
#         p2.join()
#         pdnm1.join()

#         print("Time used:", time.time() - t1)