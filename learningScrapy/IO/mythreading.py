import random
import time
import threading


def thread_run(urls):
    print('Current %s is running...' % threading.current_thread().name)
    for url in urls:
        print('%s ---->> %s' % (threading.current_thread().name, url))
        time.sleep(random.random())
    print('%s ended.' % threading.current_thread().name)


print('%s is running...' % threading.current_thread().name)

t1 = threading.Thread(target=thread_run,
                      name='Thread_1',
                      args=(['url_11', 'url_12', 'url_13'], ))

t2 = threading.Thread(target=thread_run,
                      name='Thread_2',
                      args=(['url_21', 'url_22', 'url_23'], ))

t1.start()
t2.start()

t1.join()
t2.join()

print('%s ended.' % threading.current_thread().name)