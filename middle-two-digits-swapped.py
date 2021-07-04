#!/usr/bin/env python

a = input()

print ((a / 100) - ((a / 1000) * 10)) * 10 + ((a / 1000) - ((a / 10000) * 10))
