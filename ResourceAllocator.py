
# Resource allocator
import time
import threading
import random
import numpy as np

def allocateRes(s_res, dist, nr_res, treatment_duration):  # Allocate
    t = threading.Thread(daemon=True, target=block_and_release_res, args=(s_res, dist, nr_res,treatment_duration))
    t.start()
    # print("Apply treatment")
    # print(f"resource number: {s_res} blocked")
    # print(f"strat timer for resource number: {s_res}")



def block_and_release_res(s_res, dist, nr_res,treatment_duration):  # timer
    #     t_dists = ["normal", "fixed", "exp"]

        # treatment_duration = int(random.uniform(1, 60))
    time.sleep(treatment_duration)
    #t.join()
    print(f"Treatment duration is: {treatment_duration}, for resource number: {s_res}")
    print(f"Release res: {s_res}")
    nr_res.append(s_res) #
    print("Do more stuff here")
    print("")




# exit_event = threading.Event()
# def signal_handler(signum, frame):
#     exit_event.set()