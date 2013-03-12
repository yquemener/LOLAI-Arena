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
from bottle import route, run, view, post, request, static_file
from arena import Arena


# ------------------------------
# Web pages
arena = Arena()

TEMPLATE_PATH = "Lib/template/"

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static/')

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
    info = request.forms
    context = arena.play_game(**info)
    return context

@route('/vsmarket' , method='POST')
@view(TEMPLATE_PATH + 'vs.tpl')
def vsmarket():
    """  Webpage which sum up the marke game and traces charts"""
    info = request.forms
    args = {"game_name": info['game_name']}

    index=0
    for aname in info.keys():
        if aname.startswith("bot_"):
            for i in range(int(info[aname])):
                args["bot"+str(index)]=aname[4:]
                index+=1

    context = arena.play_game(**args)
    return context

@route('/challenge', method='POST')
@view(TEMPLATE_PATH + 'challenge.tpl')
def vsall():
    """ Tableau de résultat de tous les matchs"""
    info = request.forms
    context = arena.play_challenge(**info)
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

