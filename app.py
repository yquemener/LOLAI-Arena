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
from prisonnier import Prisonnier

# ------------------------------
# Bricolages temporaire

BOTS_PATH = "Games/Prisonnier/bots/"
TEMPLATE_PATH = "Lib/template/"

def list_bot():
    """ List avialable bots"""
    # C'est vraiment pas top de le faire comme ça, faudra faire des tests pour être sûr que c'est bien un bot et pas un fichier égaré!
    return os.listdir(BOTS_PATH)


# ------------------------------
# Web pages


@route('/arena')
@view(TEMPLATE_PATH + 'arena.tpl')
def arena():
    """ Webpage listing games and their settings"""
    context = {'bots' : list_bot()}
    return context

@route('/vs' , method='POST')
@view(TEMPLATE_PATH + 'vs.tpl')
def vs():
    """  Webpage which sum up the game"""
    bots = [request.forms.get('player1'),request.forms.get('player2')]
    manche = int(request.forms.get('manche'))
    match = Prisonnier(bots, manche)
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

