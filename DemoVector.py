#!/usr/bin/python env
#encoding:utf-8
"""
@version: python2.7
@author: ‘whyc‘
@license: Apache Licence 
@contact: 8720whyc@gmail.com
@site: 
@software: PyCharm
@file: DemoVector.py
@time: 17-7-28 下午11:50
test the python's Vector class
"""
from math import hypot
"""
简单的二维　加法，乘法实现
ｍａｇｉｃ　或者是　双下划线__ 这种方法
本身不会直接调用，由系统调用　
"""
class Vector():
    def __init__(self,x=.0,y=.0):
        self.x=x
        self.y=y
    #有点相当于Java的toString方法 当打印对象时返回，
    #对像的toString方法 结果，
    def __repr__(self):
        return 'Vector(%r,%r)'%(self.x,self.y)
    #当使用ａｂｓ(Vector)　时 系统将调用　Ｖｅｃｔｏｒ 自己实现的　__abs__　方法
    #相当于返回了 Vector.__abs__()
    def __abs__(self):
        return hypot(self.x,self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        y = self.x + other.x
        x = self.y + other.y
        return Vector(x,y)
    def __mul__(self, other):
        return Vector(self.x*other.x,self.y*other.y)

if __name__ == '__main__':
    v1 = Vector(3,4)
    v2 = Vector(3.4,6.7)
    v3 = v2 + v1
    print v3
    print "v3 hypot: ",abs(v1)
    print "v4: ",v3*v2*v1