#coding=utf-8
#selenium the first exercise
from selenium import webdriver
from multiprocessing import Process
import time

def proc1():
    print 'begin'
    dr = webdriver.Chrome("/Users/working_tool/chromedriver")
    dr.get("http://baidu.com")
def proc2():
    print 'begin'
    dr = webdriver.Chrome("/Users/working_tool/chromedriver")
    dr.get("http://google.com")

if __name__ == '__main__':
    p = Process(target=proc1())
    p2 = Process(target=proc2())
    p.start()
    p2.start()