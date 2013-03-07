#!/usr/bin/env python
#-*- coding:utf8-*-

# ------------------------------
# Easier import system
# Files in folders which are in .pth will be imortable with a simple import
import os
import site 
import sys

CUR_DIR = os.path.dirname(os.path.realpath(__file__))
site.addsitedir(CUR_DIR)

# ------------------------------
# Imports
from arena import Arena
from bottle import route, run, view, post, request


arena = Arena()
if len(sys.argv)!=4:
    print "Usage: python cli.py gamename bot1name bot2name"
    exit()
(dump, gamename, bot1name, bot2name) = sys.argv

games = arena.games
if gamename not in games.keys():
    print "Unkown game : "+ gamename
    exit()
if bot1name not in games[gamename]["bots"]:
    print "Unkown bot : "+bot1name
    exit()
if bot2name not in games[gamename]["bots"]:
    print "Unkown bot : "+bot2name
    exit()

args = {"game_name" : gamename, "bot1" : bot1name, "bot2": bot2name}

arena.play_game(**args)

# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 

