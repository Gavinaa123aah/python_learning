#coding=utf-8
#使用进程池来启动大量子进程

from multiprocessing import  Pool
import os, time, random

def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool()
    for x in range(5):
        p.apply(long_time_task,args=(x,))
    print 'waiting for all subProcess'
    p.close()
    p.join()
    print 'all subProcess finish'