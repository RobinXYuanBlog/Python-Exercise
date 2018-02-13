from multiprocessing import Process, Queue
import os, time, random


# Write data process
def proc_write(q, urls):
    print("Process (%s) is writing..." % os.getpid())
    for url in urls:
        q.put(url)
        print("Put %s to queue" % url)
        time.sleep(random.random())


# Read data process
def proc_read(q):
     print("Process %s is reading..." % os.getpid())
     while True:
         url = q.get(True)
         print("Get %s from queue" % url)


if __name__ == '__main__':
    # Parent proc create queue, transmit to child proc
    q = Queue()
    proc_writer1 = Process(target=proc_write, args=(q, ['url_11', 'url_12', 'url_13']))
    proc_writer2 = Process(target=proc_write, args=(q, ['url_21', 'url_22', 'url_23']))
    proc_reader = Process(target=proc_read, args=(q,))

    # Start child, write
    proc_writer1.start()
    proc_writer2.start()
    # Start child, read
    proc_reader.start()

    # Waiting for proc_writer finish
    proc_writer1.join()
    proc_writer2.join()
    # Infinite loop, abort proc
    proc_reader.terminate()


