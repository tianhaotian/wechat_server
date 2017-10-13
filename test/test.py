#!/usr/bin/env python
#-*- encoding:utf-8 -*-

class A(object):
    def __init__(self, bag):
        self.a = bag.get('a', '')
        self.b = bag.get('b', '')

    @property
    def oa(self):
        return self.a+1

    @property
    def ob(self):
        return self.b+1

    def modify_a(self, a):
        self.a = a

    def modify_b(self, b):
        self.b = b

if __name__ == '__main__':
    bag = {'b':1}
    a = A(bag)
    a.modify_a(1)
    print a.oa