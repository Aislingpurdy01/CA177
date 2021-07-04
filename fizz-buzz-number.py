#!/usr/bin/env python

integer = input()

if (integer % 5 == 0) and (integer % 3 == 0):
   print "fizz-buzz"

elif integer % 3 == 0:
   print "fizz"

elif integer % 5 == 0:
   print "buzz"

else:
   print integer
