#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print ("I can add up the numbers and compare with yours")
a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))
c = int(input("Enter your answer: "))
sum = a + b 
if c == sum:
    print ("Correctly")
elif c != sum:
    print ("Wrong")
