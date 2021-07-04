#!/usr/bin/env python

n = 10
smallest = 0

i = 0
while i < n - 1:
   m = input()
   if smallest > m:
      smallest = m
   i = i + 1

print smallest
