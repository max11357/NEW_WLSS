import multiprocessing
import math
import time
import run_random_new, run_loop

if __name__ == "__main__":
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
        # amount_lap = range(1,201)

        # run_random_new.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
        #         d_threshold, r1, r2)
        
        run_loop.start(pkt_control, pkt_data, d_threshold, r1, r2)
        

