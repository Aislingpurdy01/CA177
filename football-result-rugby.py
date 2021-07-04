#!/usr/bin/env python

a = input() * 5
b = input() * 2
c = input() * 3
d = input() * 5
e = input() * 2
f = input() * 3

if a + b + c > d + e + f:
   print "Home win."

elif a + b + c < d + e + f:
   print "Away win."

else:
   print "Draw."
