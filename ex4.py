#coding=utf-8

#切片
def function1():
    L = ['a', 'b', 'c']
    print L[:2]

#迭代
def function2():
    d = {'a': 1, 'b': 2, 'c': 3}
    for key in d:
        print key
    for value in d.values():
        print  value
    for key,value in d.items():
        print key,"--",value
#判断是否为可迭代对象
def function3():
    from collections import Iterable
    print isinstance('aaaccc',Iterable)

#列表生成式
def function4():
    L = []
    for x in range(1,10):
        L.append(x * x)
    print L
    print [x * x for x in range(1,10)]
    print [x * x for x in range(1, 10) if x % 2 == 0]
    print [m + n for m in 'abc' for n in 'qwe']
#列出文件和目录
    import os
    print [d for d in os.listdir('.')]

#把所有字符改成小写
def function5():
    L = ['AAC', 'BSSF', 'ADDSdsa']
    print [s.lower() for s in L]



if __name__=="__main__":
    function5()