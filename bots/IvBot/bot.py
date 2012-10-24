#!/usr/bin/env python2
#-*- coding:utf8-*-  
from random import *
from time import *
import sys

seed(time())

print "OK"
received=raw_input()
ans="C"
while received!='Q':
    print ans
    received=raw_input()
    ans=received
