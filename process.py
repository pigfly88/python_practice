from multiprocessing import Process
import os

def run_proc(name):
    print('run child process %s (%s).' % (name, os.getpid()))

if __name__ == '__main__':
    print('run parent process %s.' % os.getpid())

    p = Process(target=run_proc, args=('test',))
    print('child process will start.')
    p.start()
    p.join()
    print('child procss end.')



# 调用fork函数时，从父进程拷贝一个进程成为子进程，然后把进程id分别返回给父子进程
# 父进程拿到的是子进程的pid，而子进程拿到的永远是0
# pid = os.fork()
# if(pid==0):
#     print("I'm child!")
# else:
#     print("I'm father, fork a new process, pid is " + str(pid))
