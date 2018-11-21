import multiprocessing
import math
import run1, run2, run3, run4, run5, run6, run7, run8, run9
import rundnm1, rundnm2, rundnm3, rundnm4, rundnm5, rundnm6, rundnm7, rundnm8, rundnm9
import time

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

def runn3(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
        d_threshold, r1, r2, lap):
        for l in lap:
                run3.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
                        d_threshold, r1, r2, l)

def runn4(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
        d_threshold, r1, r2, lap):
        for l in lap:
                run4.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
                        d_threshold, r1, r2, l)

def runn5(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
        d_threshold, r1, r2, lap):
        for l in lap:
                run5.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
                        d_threshold, r1, r2, l)

def runn6(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
        d_threshold, r1, r2, lap):
        for l in lap:
                run6.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
                        d_threshold, r1, r2, l)

def runn7(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
        d_threshold, r1, r2, lap):
        for l in lap:
                run7.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
                        d_threshold, r1, r2, l)

def runn8(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
        d_threshold, r1, r2, lap):
        for l in lap:
                run8.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
                        d_threshold, r1, r2, l)

def runn9(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
        d_threshold, r1, r2, lap):
        for l in lap:
                run9.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
                        d_threshold, r1, r2, l)

def runndnm1(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
        d_threshold, r1, r2, decimal, decrease_t, increase_t, lap):
        for l in lap:
                rundnm1.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
                        d_threshold, r1, r2, decimal, decrease_t, increase_t, l)

def runndnm2(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
        d_threshold, r1, r2, decimal, decrease_t, increase_t, lap):
        for l in lap:
                rundnm2.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
                        d_threshold, r1, r2, decimal, decrease_t, increase_t, l)

def runndnm3(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
        d_threshold, r1, r2, decimal, decrease_t, increase_t, lap):
        for l in lap:
                rundnm3.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
                        d_threshold, r1, r2, decimal, decrease_t, increase_t, l)

def runndnm4(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
        d_threshold, r1, r2, decimal, decrease_t, increase_t, lap):
        for l in lap:
                rundnm4.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
                        d_threshold, r1, r2, decimal, decrease_t, increase_t, l)

def runndnm5(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
        d_threshold, r1, r2, decimal, decrease_t, increase_t, lap):
        for l in lap:
                rundnm5.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
                        d_threshold, r1, r2, decimal, decrease_t, increase_t, l)

def runndnm6(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
        d_threshold, r1, r2, decimal, decrease_t, increase_t, lap):
        for l in lap:
                rundnm6.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
                        d_threshold, r1, r2, decimal, decrease_t, increase_t, l)

def runndnm7(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
        d_threshold, r1, r2, decimal, decrease_t, increase_t, lap):
        for l in lap:
                rundnm7.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
                        d_threshold, r1, r2, decimal, decrease_t, increase_t, l)

def runndnm8(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
        d_threshold, r1, r2, decimal, decrease_t, increase_t, lap):
        for l in lap:
                rundnm8.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
                        d_threshold, r1, r2, decimal, decrease_t, increase_t, l)

def runndnm9(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
        d_threshold, r1, r2, decimal, decrease_t, increase_t, lap):
        for l in lap:
                rundnm9.start(width, height, density, num_base, pos_base, set_energy, pkt_control, pkt_data, \
                        d_threshold, r1, r2, decimal, decrease_t, increase_t, l)


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
        amount_lap = range(1,10)
        
        t1 = time.time()
        
        p1 = multiprocessing.Process(target=runn1, args=(width, height, density, num_base, pos_base, \
                set_energy, pkt_control, pkt_data, d_threshold, r1, r2, amount_lap,))
        p2 = multiprocessing.Process(target=runn2, args=(width, height, density, num_base, pos_base, \
                set_energy, pkt_control, pkt_data, d_threshold, r1, r2, amount_lap,))
        p3 = multiprocessing.Process(target=runn3, args=(width, height, density, num_base, pos_base, \
                set_energy, pkt_control, pkt_data, d_threshold, r1, r2, amount_lap,))
        p4 = multiprocessing.Process(target=runn4, args=(width, height, density, num_base, pos_base, \
                set_energy, pkt_control, pkt_data, d_threshold, r1, r2, amount_lap,))
        p5 = multiprocessing.Process(target=runn5, args=(width, height, density, num_base, pos_base, \
                set_energy, pkt_control, pkt_data, d_threshold, r1, r2, amount_lap,))
        p6 = multiprocessing.Process(target=runn6, args=(width, height, density, num_base, pos_base, \
                set_energy, pkt_control, pkt_data, d_threshold, r1, r2, amount_lap,))
        p7 = multiprocessing.Process(target=runn7, args=(width, height, density, num_base, pos_base, \
                set_energy, pkt_control, pkt_data, d_threshold, r1, r2, amount_lap,))
        p8 = multiprocessing.Process(target=runn8, args=(width, height, density, num_base, pos_base, \
                set_energy, pkt_control, pkt_data, d_threshold, r1, r2, amount_lap,))
        p9 = multiprocessing.Process(target=runn9, args=(width, height, density, num_base, pos_base, \
                set_energy, pkt_control, pkt_data, d_threshold, r1, r2, amount_lap,))
        
        pdnm1 = multiprocessing.Process(target=runndnm1, args=(width, height, density, num_base, pos_base, \
                set_energy, pkt_control, pkt_data, d_threshold, r1, r2, decimal, decrease_t, \
                increase_t, amount_lap,))
        pdnm2 = multiprocessing.Process(target=runndnm2, args=(width, height, density, num_base, pos_base, \
                set_energy, pkt_control, pkt_data, d_threshold, r1, r2, decimal, decrease_t, \
                increase_t, amount_lap,))
        pdnm3 = multiprocessing.Process(target=runndnm3, args=(width, height, density, num_base, pos_base, \
                set_energy, pkt_control, pkt_data, d_threshold, r1, r2, decimal, decrease_t, \
                increase_t, amount_lap,))
        pdnm4 = multiprocessing.Process(target=runndnm4, args=(width, height, density, num_base, pos_base, \
                set_energy, pkt_control, pkt_data, d_threshold, r1, r2, decimal, decrease_t, \
                increase_t, amount_lap,))
        pdnm5 = multiprocessing.Process(target=runndnm5, args=(width, height, density, num_base, pos_base, \
                set_energy, pkt_control, pkt_data, d_threshold, r1, r2, decimal, decrease_t, \
                increase_t, amount_lap,))
        pdnm6 = multiprocessing.Process(target=runndnm6, args=(width, height, density, num_base, pos_base, \
                set_energy, pkt_control, pkt_data, d_threshold, r1, r2, decimal, decrease_t, \
                increase_t, amount_lap,))
        pdnm7 = multiprocessing.Process(target=runndnm7, args=(width, height, density, num_base, pos_base, \
                set_energy, pkt_control, pkt_data, d_threshold, r1, r2, decimal, decrease_t, \
                increase_t, amount_lap,))
        pdnm8 = multiprocessing.Process(target=runndnm8, args=(width, height, density, num_base, pos_base, \
                set_energy, pkt_control, pkt_data, d_threshold, r1, r2, decimal, decrease_t, \
                increase_t, amount_lap,))
        pdnm9 = multiprocessing.Process(target=runndnm9, args=(width, height, density, num_base, pos_base, \
                set_energy, pkt_control, pkt_data, d_threshold, r1, r2, decimal, decrease_t, \
                increase_t, amount_lap,))



        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p7.start()
        p8.start()
        p9.start()
        pdnm1.start()
        pdnm2.start()
        pdnm3.start()
        pdnm4.start()
        pdnm5.start()
        pdnm6.start()
        pdnm7.start()
        pdnm8.start()
        pdnm9.start()

        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
        p8.join()
        p9.join()
        pdnm1.join()
        pdnm2.join()
        pdnm3.join()
        pdnm4.join()
        pdnm5.join()
        pdnm6.join()
        pdnm7.join()
        pdnm8.join()
        pdnm9.join()

        print("Time used:", time.time() - t1)
