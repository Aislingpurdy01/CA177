#!/usr/bin/env python

a = input()

middle = ((a / 100) - ((a / 10000) * 100))

print (middle * 10000) + ((a / 10000) * 100) + (a - ((a / 100) * 100))
