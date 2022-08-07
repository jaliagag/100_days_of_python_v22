#!/usr/bin/env python
# -*- coding: utf-8 -*-

#https://www.youtube.com/watch?v=7XXR3s_fYU8

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B,C):
    pass

#print(D.mro())
#[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
print(D.num)
