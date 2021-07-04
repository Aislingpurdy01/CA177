#!/usr/bin/env python

day = input()
count = input()

remainder = (day + count) % 7

if remainder == 0:
   print "Monday"

elif remainder == 1:
   print "Tuesday"

elif remainder == 2:
   print "Wednesday"

elif remainder == 3:
   print "Thursday"

elif remainder == 4:
   print "Friday"

elif remainder == 5:
   print "Saturday"

elif remainder == 6:
   print "Sunday"
