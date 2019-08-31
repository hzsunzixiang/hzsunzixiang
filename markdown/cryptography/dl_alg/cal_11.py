#!/usr/bin/env python
# -*- coding:UTF-8
n = 11 
for i in [2,3,4,5,6,7,8,9,10]:
    #print "for ", i
    for x in range(1, n):
        print("$$%s^%s \equiv %s (mod \ %s)$$"%(i, x, i**x % n, n))


#         $$3^1 \equiv 3 (mod \ 7)$$
#         $$3^2 \equiv 2 (mod \ 7)$$
#         $$3^3 \equiv 6 (mod \ 7)$$
#         $$3^4 \equiv 4 (mod \ 7)$$
#         $$3^5 \equiv 5 (mod \ 7)$$
#         $$3^6 \equiv 1 (mod \ 7)$$
