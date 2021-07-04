#!/usr/bin/env python

a = input()
b = input()
c = input()

a1 = b ** 2 + c ** 2

b1 = a ** 2 + c ** 2

c1 = b ** 2 + a ** 2

if a ** 2 == a1 or b ** 2 == b1 or c ** 2 == c1:
   print "Right-angled triangle."
elif a == b == c:
   print "Equilateral triangle."
elif a == b or b == c or a == c:
   print "Isosceles triangle."
else:
   print "Just a triangle."
