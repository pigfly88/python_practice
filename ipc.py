from multiprocessing import Process, Queue
import os, time, random

def write(q):
    for i in range(1,7):
        print('Put %s to queue.' % i)
        q.put(i)
        time.sleep(random.random())

def read(q):
    while(True):
        c = q.get(True)
        print('Get %s from queue.' % c)

if __name__ == '__main__':
    q = Queue();
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()
    pw.join()
    pr.join()