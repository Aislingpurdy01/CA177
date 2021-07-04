#!/usr/bin/env python

n = 10
total = 0
i = 0

while i < n:
   m = input()
   if m < 0:
      total = total - m

   else:
      total = total + m
   i = i + 1

print total
