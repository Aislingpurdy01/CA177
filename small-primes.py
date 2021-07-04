#!/usr/bin/env python

n = input()

if n == 2:
   print n, "is a prime"
elif n % 2 == 0 or n == 1:
   print n, "is not a prime"
elif n == 3 or n == 5 or n == 7:
   print n, "is a prime"
elif n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
   print n, "is not a prime"
else:
   print n, "is a prime"
