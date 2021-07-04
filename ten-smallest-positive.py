#!/usr/bin/env python

n = 100
smallest = input()

i = 0
while i < n :
   v = input()
   if smallest > v:
      smallest = smallest + v
      smallest = v
   i = i + 1
   
print smallest