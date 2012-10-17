#!/usr/bin/env python
#-*- coding:utf8-*-

# ------------------------------
# Imports
from bottle import route, run, view, post, request
from match import Match

import os


# ------------------------------
# Bricolages temporaire

BOTS_PATH = "../bots/"
def list_bot():
    """ List avialable bots"""
    # C'est vraiment pas top de le faire comme ça, faudra faire des tests pour être sûr que c'est bien un bot et pas un fichier égaré!
    return os.listdir(BOTS_PATH)


# ------------------------------
# Web pages

ROUND_TIMEOUT = 0.01

@route('/arena')
@view('template/arena.tpl')
def arena():
    """ Webpage listing games and their settings"""
    context = {'bots' : list_bot()}
    return context

@route('/vs' , method='POST')
@view('template/vs.tpl')
def vs():
    """  Webpage which sum up the game"""
    bots = [request.forms.get('player1'),request.forms.get('player2')]
    manche = int(request.forms.get('manche'))
    match = Match(bots, manche)
    match.start()
    match.join(ROUND_TIMEOUT*200)
    context = match.give_results()
    return context

# ------------------------------
# What is run in this file

if __name__ == '__main__':
    run(host='localhost', port=8080, reloader = True)

# ------------------------------
# End of the program

# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 

