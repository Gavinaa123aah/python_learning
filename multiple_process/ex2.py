#coding=utf-8
from multiprocessing import Process
import os

#第一个自进程
def run_proc ( name ) :
    print 'run child process --name:%s--id:%s' % (name,os.getpid())
    for x in range(10**4):
        print x
#第二个子进程
def run_proc2 ():
    for x in range(10**4):
        print 'hello python!'

if __name__ == '__main__':
    print  'parent process: %s' % os.getpid()
    p = Process(target=run_proc,args=('test',))
    p2 = Process(target=run_proc2())
    print 'Process will start'
    p.start()
    p2.start()
    p.join()
    print 'process end'