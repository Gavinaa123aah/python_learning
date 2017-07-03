#coding=utf-8

class Student(object):
    def __init__(self,name, age, score):
        self.name = name
        self.score = score;

    def print_score(self):
        print  '%s : %s' % (self.name, self.score)

if __name__ == '__main__':
    kobe = Student('kobe', '37', '100')
    james = Student('james', '33', '101')

    kobe.print_score()