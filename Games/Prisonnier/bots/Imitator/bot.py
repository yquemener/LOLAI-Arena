#!/usr/bin/env python2
#-*- coding:utf8-*-  

# --------------------
# bot copieur!
# Il fait toujours comme l'autre au coup d'avant

from random import *
from time import *

seed(time())

# Il est près
print "OK"

# Le premier choix est aléatoire (on a rien à copier)
ans = choice(['C','T'])

# Variable où l'on stockera le choix de l'autre
other = choice(['C','T'])

# Variable où l'on stockera le message du programme maitre
master = raw_input()

while master!='Q':
    # La strat est de toujour copier
    ans = other
    #On envoie notre réponse
    print ans
    # On regarde ce que l'autre a joué
    other = raw_input()
    # On attend le prochain signal ('A' si on refait une manche, 'Q' sur on arrete
    master = raw_input()
