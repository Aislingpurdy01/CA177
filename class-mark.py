#!/usr/bin/env python

integer = input()

if integer >= 70:
   print "first"

elif integer >= 55 and integer < 70:
   print "second"

elif integer >= 40 and integer < 55:
   print "third"

elif integer < 40:
   print "fail"
