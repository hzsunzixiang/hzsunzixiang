#!/usr/bin/env python
# -*- coding:UTF-8

n = 59 
for x in range(1, 61):
    print"   %d|"%(x),
    if x%12==0:
        print "\n"

print "\n\n"
for i in [3]:
    for x in range(1, 61):
        print("   %s|"%(i**x % n)),
        if x%12==0:
            print "\n"
        #print("$$%s^%s \equiv %s (mod \ %s)$$"%(i, x, i**x % n, n))

#|  \\(k\\)        |   1|   2|   3|   4 |   5|   6|   7|   8|   9|  10|  11|  12|
#|            :--: |:--:|:--:|:--:| :--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
#|$$3^k(mod\ 59)$$ |   3|   9|   5|    4|   1|   3|   9|   5|   4|   1|   3|   9|

#
#         $$3^1 \equiv 3 (mod \ 7)$$
#         $$3^2 \equiv 2 (mod \ 7)$$
#         $$3^3 \equiv 6 (mod \ 7)$$
#         $$3^4 \equiv 4 (mod \ 7)$$
#         $$3^5 \equiv 5 (mod \ 7)$$
#         $$3^6 \equiv 1 (mod \ 7)$$

#n = 59 
#for i in [3]:
#    for x in range(1, n):
#        print("$$%s^%s \equiv %s (mod \ %s)$$"%(i, x, i**x % n, n))
