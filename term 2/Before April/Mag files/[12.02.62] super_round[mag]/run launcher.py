import multiprocessing
import math
import rund30_3, rund50_3, rund100_3
import time

def runndnm30(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
          d_threshold, r1, r2, decimal, decrease_t, increase_t, false_values, drr):
        for dr in drr:
                rund30_3.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
          d_threshold, r1, r2, decimal, decrease_t, increase_t, false_values, dr)

def runndnm50(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
          d_threshold, r1, r2, decimal, decrease_t, increase_t, false_values, drr):
        for dr in drr:
                rund50_3.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
          d_threshold, r1, r2, decimal, decrease_t, increase_t, false_values, dr)

def runndnm100(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
          d_threshold, r1, r2, decimal, decrease_t, increase_t, false_values, drr):
        for dr in drr:
                rund100_3.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
          d_threshold, r1, r2, decimal, decrease_t, increase_t, false_values, dr)


if __name__ == "__main__":
        width = 100 # meter
        height = 100 # meter
        density = float(0.0125)
        num_base = 1
        pos_base = "-10,50"
        set_energy = 2 # set energy = 1 Joule
        pkt_control = 200 # bit
        pkt_data = 4000  # bit
        d_threshold = 87  # **********************
        r1 = 30 # meter
        r2 = r1*((2*math.log(10))**(0.5)) # meter
        decimal = 2
        decrease_t = 0.01
        increase_t = 0.01
        drr = range(1,101)
        false_values = 3
        t1 = time.time()
        
        
        pdnm30 = multiprocessing.Process(target=runndnm30, args=(width, height, density, num_base, \
                pos_base, set_energy, pkt_control, pkt_data, d_threshold, r1, r2, decimal, \
                decrease_t, increase_t, false_values, drr,))
        pdnm50 = multiprocessing.Process(target=runndnm50, args=(width, height, density, num_base, \
                pos_base, set_energy, pkt_control, pkt_data, d_threshold, r1, r2, decimal, \
                decrease_t, increase_t, false_values, drr,))
        pdnm100 = multiprocessing.Process(target=runndnm100, args=(width, height, density, num_base, \
                pos_base, set_energy, pkt_control, pkt_data, d_threshold, r1, r2, decimal, \
                decrease_t, increase_t, false_values, drr,))



        pdnm30.start()
        pdnm50.start()
        pdnm100.start()

        pdnm30.join()
        pdnm50.join()
        pdnm100.join()

        print("Time used:", time.time() - t1)
