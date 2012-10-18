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
def liste_bot():
    """Liste les bot disponibles"""
    # C'est vraiment pas top de le faire comme ça, faudra faire des tests pour être sûr que c'est bien un bot et pas un fichier égaré!
    return os.listdir(BOTS_PATH)


# ------------------------------
# Les pages visibles
ROUND_TIMEOUT = 0.01

@route('/')
@route('/arena')
@view('template/arena.tpl')
def arena():
    """ Page des arènes de LoL on y voit les jeux proposés et leurs paramètres """
    context = {'bots' : liste_bot()}
    return context

@route('/vs' , method='POST')
@view('template/vs.tpl')
def vs():
    """ Page résumé du jeu qui vient de se dérouler """
    bots = [request.forms.get('player1'),request.forms.get('player2')]
    manche = int(request.forms.get('manche'))
    match = Match(bots, manche)
    match.start()
    match.join(ROUND_TIMEOUT*200)
    context = match.give_results()
    return context

@route('/vsall', method='POST')
def vsall():
    """ Tableau de résultat de tous les matchs"""
    # Idéalement, ca devrait etre un template mais j'ai juste recopie mon vieux code pour faire vite
    html='<html><body><table style="">'
    contenders = liste_bot()
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
            if mat.isAlive():
                html+="Failed to return"
            else:
                if(mat.scores[1]>mat.scores[0]):
                    html+=c2+" victorious<br>"+str(mat.scores)
                elif(mat.scores[1]<mat.scores[0]):
                    html+=c1+" victorious<br>"+str(mat.scores)
                else:
                    html+="Draw<br>"+str(mat.scores)
                scores[c1]+=mat.scores[0]
            html+="</div></td>"
        html+='<td style="border-style:dotted;border-width:1px;">'
        html+= str(scores[c1])
        html+='</td>'
        html+="</tr>"
    html+="</table></html>"
    return html
# ------------------------------
# Quand le fichier est directement lancé

if __name__ == '__main__':
    run(host='localhost', port=8080, reloader = True)

# ------------------------------
# Fin du programme

# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 

