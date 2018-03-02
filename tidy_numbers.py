#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import izip

def check(ls): return all(int(p) <= int(n) for p,n in izip(ls, ls[1:]))
def fv(x): return next(i for i,j in enumerate(x) if x[i]>=x[i+1])
        
with open('B-large.in','r') as f: lines = f.read().splitlines()
cn = 1
for x in lines[1:]:
    if check(x): print 'Case #{}: {}'.format(cn,x)
    else: print 'Case #{}: {}'.format(cn,int(x)-(int(x[fv(x)+1:])+1))
    cn += 1