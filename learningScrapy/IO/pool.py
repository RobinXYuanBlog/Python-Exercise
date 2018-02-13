from multiprocessing import Pool
import os, time, random


# Default processing number is the number of CPU cores

# 3 processes, 5 missions

def run_task(name):
    print("Task %s (pid = %s) is running..." % (name, os.getpid()))
    time.sleep(random.random() * 3)
    print("Task %s end." % name)


if __name__ == '__main__':
    print("Current process %s." % os.getpid())
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(i,))
    print("Waiting for all sub-processes done...")
    p.close()
    p.join()
    print("All sub-processes done.")

