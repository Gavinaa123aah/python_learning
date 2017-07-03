#coding=utf-8
class Student(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def print_info(self):
        print '%s  -- %s' % (self.username,self.password)


if __name__ == '__main__':
    student1 = Student('lijundong', '12345')
    student2 = Student('kobe', '333')

    classmates=[]

    classmates.append(student1)
    classmates.append(student2)

    s = classmates.pop()

    s.print_info()
    #print isinstance(classmates.pop(), Student)
