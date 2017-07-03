#coding=utf-8
import threading,time

def new1():
    print 'this is new thread:  --%s' % threading.currentThread().name
    #time.sleep(5)
    for x in range(10):
        print 'new1 11111!'

def new2():
    print 'this is new thread:  --%s' % threading.currentThread().name
    #time.sleep(3)

    for x in range(10):
        print 'new2 2222'

if __name__ == '__main__':
    print 'threading is %s' % threading.current_thread().name


    t = threading.Thread(target=new1, name='new1')
    t.start()
    t2 = threading.Thread(target=new2,name='new2')
    t2.start()

    t.join()
    print 'ending!!!'