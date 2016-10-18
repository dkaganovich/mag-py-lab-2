#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# 7
def pif(n):
    return [(x, y, z) for z in xrange(n, 0, -1) for y in xrange(z, 0, -1) for x in xrange(y, 0, -1) if x**2 + y**2 == z**2]
# print pif(18)


# 8
from math import sqrt
def prime(n):
    return [x for x in xrange(2, n) if all(x % y != 0 for y in xrange(2, int(sqrt(x) + 1)))]
# print prime(300)


# 9
class Cartesian:
    def __init__(self, x, n):
        self.x = sorted(x)
        self.prod = []
        self.n = n
    def __iter__(self):
        return self
    def next(self):
        if len(self.prod) == 0:
            self.prod = [self.x[0]] * self.n
        else:
            for i in xrange(len(self.prod) - 1, -1, -1):
                if self.prod[i] == self.x[-1]:
                    self.prod[i] = self.x[0]
                    continue
                self.prod[i] = self.x[self.x.index(self.prod[i]) + 1]
                break
        return self.prod
# a = Cartesian([1,"a"], 2)
# for i in xrange(10):
#     print a.next()


# 10
def pretty_format(obj, obj_str = "", pos = 0, offset = 0, result = ""):
    if pos == 0:
        obj_str = str(obj)
    while pos < len(obj_str):
        if obj_str[pos] == "[" or obj_str[pos] == "{":
            if len(result) > 0 and result[-1] == "\n":
                result += "\t" * offset
            result += obj_str[pos] + "\n"
            offset += 1
            pos += 1
            break
        elif obj_str[pos] == "]" or obj_str[pos] == "}":
            offset -= 1
            result += "\n" + "\t" * offset + obj_str[pos]
        elif obj_str[pos] == ",":
            result += ",\n"
        elif obj_str[pos] != " ":
            if len(result) > 0 and result[-1] == "\n":
                result += "\t" * offset
            result += obj_str[pos]
        else:
            pass
        pos += 1
    if pos != len(obj_str):
        result = pretty_format(obj, obj_str, pos, offset, result)
    return result
# print pretty_format([{3:{3:["a",2,3]}}, {1:2, 'a': [1, 245], 'b': 'hi'}])


# 11
from numbers import Real
from math import sqrt

class Vector:
    def __init__(self, *data):
        self.data = tuple(data)
    def magnitude(self):
        return sqrt(sum(a**2 for a in self))
    def __add__(self, o):
        return Vector(*[a + b for a, b in zip(self, o)])
    def __sub__(self, o):
        return Vector(*[a - b for a, b in zip(self, o)])
    def __mul__(self, o):
        if isinstance(o, Real):
            return Vector(*[a * o for a in self.data])
        elif isinstance(o, Vector):
            return Vector(*[a * b for a, b in zip(self, o)])
    def __rmul__(self, o):
        if isinstance(o, Real):
            return Vector(*[a * o for a in self])
    def __eq__(self, o):
        if not isinstance(o, Vector):
            return False
        return self.data == o.data
    def __iter__(self):
        return iter(self.data)
    def __getitem__(self, index):
        return self.data[index]
    def __repr__(self):
        return repr(self.data)
    def __str__ (self):
        return str(self.data)
# a = Vector(1,2,3)
# b = Vector(4,5,6)
# c = Vector(1,2,3)
# print a
# print b
# print c
# print a + b
# print a - b
# print a * b
# print a * 5
# print 2 * a
# print a == b
# print a == c
# print a.magnitude()
# for i in a:
#     print i
