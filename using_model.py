'a test module'

__author__ = 'lijundong'

import  sys

def test():
    args = sys.argv
    if len(args) == 1:
        print 'hello world'
    elif len(args) == 2:
        print 'hello ',abs[1]
    else:
        print 'too many arguments!'
if __name__ == '__main__':
    test()