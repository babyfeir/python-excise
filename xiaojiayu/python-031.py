# !/usr/bin/env python
# -*- coding: UTF-8 -*-

import pickle

class Person(object):

    def __init__(self, n, a):
        self.name = n
        self.age = a

    def show(self):
        print(self.name + "_" + str(self.age))

aa = Person('JGood', 2)
aa.show()
f = open('d:\\p.txt','w')
pickle.dump(aa, f ,0)
f.close()

f = open('d:\\p.txt', 'r')
bb = pickle.load(f)
f.close()
bb.show()
