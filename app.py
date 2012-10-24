#!/usr/bin/env python
#-*- coding:utf8-*-

# ------------------------------
# Easier import system
# Files in folders which are in .pth will be imortable with a simple import
import os
import site

CUR_DIR = os.path.dirname(os.path.realpath(__file__))
site.addsitedir(CUR_DIR)

# ------------------------------
# Imports
from bottle import route, run, view, post, request
from arena import Arena


# ------------------------------
# Web pages
arena = Arena()

print arena.games

TEMPLATE_PATH = "Lib/template/"

@route('/')
@view(TEMPLATE_PATH + 'index.tpl')
def index():
    """ Webpage listing games and their settings"""
    context = {'games' : arena.games}
    return context

@route('/vs' , method='POST')
@view(TEMPLATE_PATH + 'vs.tpl')
def vs():
    """  Webpage which sum up the game"""
    game = request.forms.get('game')
    bots = [request.forms.get('player1'),request.forms.get('player2')]
    round = int(request.forms.get('round'))
    context = arena.play_game(game, bots, round = round)
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

