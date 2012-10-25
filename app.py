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
    info = request.forms
    context = arena.play_game(**info)
    return context

@route('/vsall', method='POST')
def vsall():
    """ Tableau de résultat de tous les matchs"""
    # Idéalement, ca devrait etre un template mais j'ai juste recopie mon vieux code pour faire vite
    html='<html><body><table style="">'
    contenders = list_bot()
    scores = dict()
    for c in contenders:
        scores[c]=0
    html+='<tr><td style="border-style:dotted;border-width:1px;">\</td>'
    for c2 in contenders:
        html+='\n\t\t<TD style="border-style:dotted;border-width:1px;"><div style="text-align:center">'
        html+=c2+"</div></td>"
    html+="<td>Score final</td></tr>"
    for c1 in contenders:
        html+="\n\t<TR>"
        html+='\n\t\t<TD style="border-style:dotted;border-width:1px;"><div style="text-align:center">'
        html+=c1+"</div></td>"
        for c2 in contenders:
            html+='\n\t\t<TD style="border-style:dotted;border-width:1px;"><div style="text-align:center">'
            mat = Match((c1,c2))
            mat.start()
            mat.join(ROUND_TIMEOUT*200)
            bots = mat.give_results()["bots"]
            if mat.isAlive():
                html+="Failed to return"
            else:
                if(bots[1].score>bots[0].score):
                    html+=c2+" victorious<br>"+str((bots[0].score,bots[1].score))
                elif(bots[1].score<bots[0].score):
                    html+=c1+" victorious<br>"+str((bots[0].score,bots[1].score))
                else:
                    html+="Draw<br>"+str((bots[0].score,bots[1].score))
                scores[c1]+=bots[0].score
            html+="</div></td>"
        html+='<td style="border-style:dotted;border-width:1px;">'
        html+= str(scores[c1])
        html+='</td>'
        html+="</tr>"
    html+="</table></html>"
    return html
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

