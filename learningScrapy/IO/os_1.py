# Way 1 - Not support Windows

import os

if __name__ == '__main__':
    print('current Process (%s) start ...' % (os.getpid()))
    pid = os.fork()
    if pid < 0:
        print("Error in fork")
    elif pid == 0:
        print("I am child process(%s) and my parent process is(%s)", (os.getpid(), os.getppid()))
    else:
        print("I (%s) created a child process (%s)", (os.getpid(), pid))


# Way 2 - All platform

from multiprocessing import Process


def run_proc(name):
    print("Child process %s (%s) Running..." % (name, os.getpid()))


if __name__ == '__main__':
    print("Parent process %s." % os.getpid())
    for i in range(5):
        p = Process(target=run_proc, args=(str(i),))
        print("Process will start.")
        p.start()
    p.join()
    print("Process end.")

