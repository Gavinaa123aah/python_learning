#coding=utf-8
#进程间通讯
from multiprocessing import Process, Queue
import os, time, random

def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

def write2(q):
    for value in range(5,10):
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw2 = Process(target=write2, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    pw2.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    pw2.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
