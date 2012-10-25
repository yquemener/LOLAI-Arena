#!/usr/bin/env python
#-*- coding:utf8-*-

html='<html><body><table style="">'
for c1 in contenders:
    html+="\n\t<TR>"
    for c2 in contenders:
        html+='\n\t\t<TD style="border-style:dotted;border-width:1px;"><div style="text-align:center">'
        print "Match "+c1+" vs "+c2
        mat = Match(c1,c2)
        mat.start()
        mat.join(ROUND_TIMEOUT*200)
        if mat.isAlive():
            print "Failed to answer in time"
            html+="Failed to return"
        else:
            if(mat.scores[1]>mat.scores[0]):
                html+=c2+" victorious<br>"+str(mat.scores)
            elif(mat.scores[1]<mat.scores[0]):
                html+=c1+" victorious<br>"+str(mat.scores)
            else:
                html+="Draw<br>"+str(mat.scores)
            print mat.scores
        html+="</div></td>"
    html+="</tr>"
html+="</table></html>"
html_file=open("results.html","w")
html_file.write(html)
html_file.close()
print "That's all folks"

# ------------------------------
# Imports
# ------------------------------ 

# ------------------------------
# Classes
# ------------------------------ 

# ------------------------------
# Fonctions
# ------------------------------ 

# ------------------------------
# Bloc principal
# ------------------------------

if __name__ == '__main__':
    pass

# ------------------------------
# Fin du programme
# ------------------------------

# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 

