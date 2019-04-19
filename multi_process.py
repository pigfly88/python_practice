from multiprocessing import Pool
import os, time, random

def run_proc(name):
    start = time.time()
    print('running child process (%s) %s.' % (name, os.getpid()))
    time.sleep(random.random() * 3)
    time_cost = time.time()-start
    print('%s complete, cost %0.2f seconds' % (name, time_cost))

if __name__ == '__main__':
    start = time.time();
    print('run parent process %s' % os.getpid())
    p = Pool(5)
    print('applying child process...')
    for i in range(1,6):
        p.apply_async(run_proc, args=('task'+str(i),))
    print('apply complete.')
    p.close()
    p.join() # 等待子进程执行完毕
    print('all child process done.')
    print('all process cost %.2f seconds' % (time.time()-start))