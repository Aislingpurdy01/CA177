#!/usr/bin/env python

v = input()
n = input()
print v
while n > 1:
   if v % 2 == 0:
    v = v / 2
    print v
    n = n - 1
   else:
    v = v * 3 + 1
    print v
    n = n - 1

