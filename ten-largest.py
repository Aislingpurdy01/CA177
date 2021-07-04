#!/usr/bin/env python

n = 10
largest = input()

i = 0
while i < n - 1:
   m = input()
   if largest < m:
      largest = m
   i = i + 1

print largest
