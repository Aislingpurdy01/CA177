#!/usr/bin/env python

n = input()

if n % 2 == 0:
   a = n / 2

else:
   a = n * 3 + 1

if a % 2 == 0:
   b = a / 2

else:
   b = a * 3 + 1

if b % 2 == 0:
   c = b / 2

else:
   c = b * 3 + 1

print n, a, b, c
