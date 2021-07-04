#!/usr/bin/env python

a = input()
b = input()

# a is smallest

if a < b:
   b = input()
else:
   a = input()

if a < b:
   b = input()
else:
   a = input()

if a < b:
   print a
else:
   print b
