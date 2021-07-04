#!/usr/bin/env python

a = input() * 3
b = input()
c = input() * 3
d = input()

if a + b > c + d:
  print "Home win."

elif a + b < c + d:
  print "Away win."

else:
  print "Draw."
