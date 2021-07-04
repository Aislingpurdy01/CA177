#!/usr/bin/env python

n = 10
total = 0
m = 1000000000
i = 0
a = 0
l = 10
b = 0
s = 1
while i < n:
   x = input()
   total = total + x * m
   i = i + 1
   m = m / 10
   
while a < n:
print (total - (total / l * l) - b) / s
c = total - (total / l * l)
b = c
a = a + 1
l = l * 10
s = s * 10