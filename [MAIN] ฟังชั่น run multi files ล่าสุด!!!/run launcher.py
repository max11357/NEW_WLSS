import multiprocessing
import math
import run1
import rundnm1
import time

def runn1(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
        d_threshold, r1, r2, dead_lap):
        for l in dead_lap:
                run1.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
                        d_threshold, r1, r2, l)

# def runn2(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#         d_threshold, r1, r2, dead_lap):
#         for l in dead_lap:
#                 run2.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#                         d_threshold, r1, r2, l)

# def runn3(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#         d_threshold, r1, r2, dead_lap):
#         for l in dead_lap:
#                 run3.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#                         d_threshold, r1, r2, l)

# def runn4(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#         d_threshold, r1, r2, dead_lap):
#         for l in dead_lap:
#                 run4.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#                         d_threshold, r1, r2, l)

# def runn5(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#         d_threshold, r1, r2, dead_lap):
#         for l in dead_lap:
#                 run5.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#                         d_threshold, r1, r2, l)

# def runn6(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#         d_threshold, r1, r2, dead_lap):
#         for l in dead_lap:
#                 run6.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#                         d_threshold, r1, r2, l)

# def runn7(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#         d_threshold, r1, r2, dead_lap):
#         for l in dead_lap:
#                 run7.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#                         d_threshold, r1, r2, l)

# def runn8(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#         d_threshold, r1, r2, dead_lap):
#         for l in dead_lap:
#                 run8.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#                         d_threshold, r1, r2, l)

# def runn9(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#         d_threshold, r1, r2, dead_lap):
#         for l in dead_lap:
#                 run9.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#                         d_threshold, r1, r2, l)

def runndnm1(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
        d_threshold, r1, r2, decimal, decrease_t, increase_t, dead_lap):
        for l in dead_lap:
                rundnm1.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
                        d_threshold, r1, r2, decimal, decrease_t, increase_t, l)

# def runndnm2(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#         d_threshold, r1, r2, decimal, decrease_t, increase_t, dead_lap):
#         for l in dead_lap:
#                 rundnm2.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#                         d_threshold, r1, r2, decimal, decrease_t, increase_t, l)

# def runndnm3(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#         d_threshold, r1, r2, decimal, decrease_t, increase_t, dead_lap):
#         for l in dead_lap:
#                 rundnm3.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#                         d_threshold, r1, r2, decimal, decrease_t, increase_t, l)

# def runndnm4(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#         d_threshold, r1, r2, decimal, decrease_t, increase_t, dead_lap):
#         for l in dead_lap:
#                 rundnm4.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#                         d_threshold, r1, r2, decimal, decrease_t, increase_t, l)

# def runndnm5(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#         d_threshold, r1, r2, decimal, decrease_t, increase_t, dead_lap):
#         for l in dead_lap:
#                 rundnm5.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#                         d_threshold, r1, r2, decimal, decrease_t, increase_t, l)

# def runndnm6(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#         d_threshold, r1, r2, decimal, decrease_t, increase_t, dead_lap):
#         for l in dead_lap:
#                 rundnm6.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#                         d_threshold, r1, r2, decimal, decrease_t, increase_t, l)

# def runndnm7(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#         d_threshold, r1, r2, decimal, decrease_t, increase_t, dead_lap):
#         for l in dead_lap:
#                 rundnm7.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#                         d_threshold, r1, r2, decimal, decrease_t, increase_t, l)

# def runndnm8(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#         d_threshold, r1, r2, decimal, decrease_t, increase_t, dead_lap):
#         for l in dead_lap:
#                 rundnm8.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#                         d_threshold, r1, r2, decimal, decrease_t, increase_t, l)

# def runndnm9(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#         d_threshold, r1, r2, decimal, decrease_t, increase_t, dead_lap):
#         for l in dead_lap:
#                 rundnm9.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
#                         d_threshold, r1, r2, decimal, decrease_t, increase_t, l)


if __name__ == "__main__":
        width = 100 # meter
        height = 100 # meter
        density = float(0.0125)
        num_base = 1
        pos_base = "0,0"
        set_energy = 2 # set energy = 1 Joule
        pkt_control = 200 # bit
        pkt_data = 4000  # bit
        d_threshold = 87  # **********************
        r1 = 30 # meter
        r2 = r1*((2*math.log(10))**(0.5)) # meter
        decimal = 2
        decrease_t = 0.01
        increase_t = 0.01
        amount_dead_lap = range(1)
        
        t1 = time.time()
        
        p1 = multiprocessing.Process(target=runn1, args=(width, height, density, num_base, pos_base, \
                set_energy, pkt_control, pkt_data, d_threshold, r1, r2, amount_dead_lap,))
        # p2 = multiprocessing.Process(target=runn2, args=(width, height, density, num_base, pos_base, \
        #         set_energy, pkt_control, pkt_data, d_threshold, r1, r2, amount_dead_lap,))
        # p3 = multiprocessing.Process(target=runn3, args=(width, height, density, num_base, pos_base, \
        #         set_energy, pkt_control, pkt_data, d_threshold, r1, r2, amount_dead_lap,))
        # p4 = multiprocessing.Process(target=runn4, args=(width, height, density, num_base, pos_base, \
        #         set_energy, pkt_control, pkt_data, d_threshold, r1, r2, amount_dead_lap,))
        # p5 = multiprocessing.Process(target=runn5, args=(width, height, density, num_base, pos_base, \
        #         set_energy, pkt_control, pkt_data, d_threshold, r1, r2, amount_dead_lap,))
        # p6 = multiprocessing.Process(target=runn6, args=(width, height, density, num_base, pos_base, \
        #         set_energy, pkt_control, pkt_data, d_threshold, r1, r2, amount_dead_lap,))
        # p7 = multiprocessing.Process(target=runn7, args=(width, height, density, num_base, pos_base, \
        #         set_energy, pkt_control, pkt_data, d_threshold, r1, r2, amount_dead_lap,))
        # p8 = multiprocessing.Process(target=runn8, args=(width, height, density, num_base, pos_base, \
        #         set_energy, pkt_control, pkt_data, d_threshold, r1, r2, amount_dead_lap,))
        # p9 = multiprocessing.Process(target=runn9, args=(width, height, density, num_base, pos_base, \
        #         set_energy, pkt_control, pkt_data, d_threshold, r1, r2, amount_dead_lap,))
        
        pdnm1 = multiprocessing.Process(target=runndnm1, args=(width, height, density, num_base, pos_base, \
                set_energy, pkt_control, pkt_data, d_threshold, r1, r2, decimal, decrease_t, \
                increase_t, amount_dead_lap,))
        # pdnm2 = multiprocessing.Process(target=runndnm2, args=(width, height, density, num_base, pos_base, \
        #         set_energy, pkt_control, pkt_data, d_threshold, r1, r2, decimal, decrease_t, \
        #         increase_t, amount_dead_lap,))
        # pdnm3 = multiprocessing.Process(target=runndnm3, args=(width, height, density, num_base, pos_base, \
        #         set_energy, pkt_control, pkt_data, d_threshold, r1, r2, decimal, decrease_t, \
        #         increase_t, amount_dead_lap,))
        # pdnm4 = multiprocessing.Process(target=runndnm4, args=(width, height, density, num_base, pos_base, \
        #         set_energy, pkt_control, pkt_data, d_threshold, r1, r2, decimal, decrease_t, \
        #         increase_t, amount_dead_lap,))
        # pdnm5 = multiprocessing.Process(target=runndnm5, args=(width, height, density, num_base, pos_base, \
        #         set_energy, pkt_control, pkt_data, d_threshold, r1, r2, decimal, decrease_t, \
        #         increase_t, amount_dead_lap,))
        # pdnm6 = multiprocessing.Process(target=runndnm6, args=(width, height, density, num_base, pos_base, \
        #         set_energy, pkt_control, pkt_data, d_threshold, r1, r2, decimal, decrease_t, \
        #         increase_t, amount_dead_lap,))
        # pdnm7 = multiprocessing.Process(target=runndnm7, args=(width, height, density, num_base, pos_base, \
        #         set_energy, pkt_control, pkt_data, d_threshold, r1, r2, decimal, decrease_t, \
        #         increase_t, amount_dead_lap,))
        # pdnm8 = multiprocessing.Process(target=runndnm8, args=(width, height, density, num_base, pos_base, \
        #         set_energy, pkt_control, pkt_data, d_threshold, r1, r2, decimal, decrease_t, \
        #         increase_t, amount_dead_lap,))
        # pdnm9 = multiprocessing.Process(target=runndnm9, args=(width, height, density, num_base, pos_base, \
        #         set_energy, pkt_control, pkt_data, d_threshold, r1, r2, decimal, decrease_t, \
        #         increase_t, amount_dead_lap,))



        p1.start()
        # p2.start()
        # p3.start()
        # p4.start()
        # p5.start()
        # p6.start()
        # p7.start()
        # p8.start()
        # p9.start()
        pdnm1.start()
        # pdnm2.start()
        # pdnm3.start()
        # pdnm4.start()
        # pdnm5.start()
        # pdnm6.start()
        # pdnm7.start()
        # pdnm8.start()
        # pdnm9.start()

        p1.join()
        # p2.join()
        # p3.join()
        # p4.join()
        # p5.join()
        # p6.join()
        # p7.join()
        # p8.join()
        # p9.join()
        pdnm1.join()
        # pdnm2.join()
        # pdnm3.join()
        # pdnm4.join()
        # pdnm5.join()
        # pdnm6.join()
        # pdnm7.join()
        # pdnm8.join()
        # pdnm9.join()

        print("Time used:", time.time() - t1)
