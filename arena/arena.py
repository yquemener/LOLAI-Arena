import os
import threading
import subprocess

from time import *

BOTS_PATH = "../bots/"
ROUND_TIMEOUT = 0.01

bots = ["AlwaysT", "AlwaysC", "Random"]
#bots = ["Random"]

class Match(threading.Thread):
    def __init__(self, c1, c2):
        self.bot1 = c1
        self.bot2 = c2
        self.scores=[0,0]
        self.error=0
        threading.Thread.__init__(self)

    def run(self):
        score1 = 0
        score2 = 0
        p1 = subprocess.Popen("./start", stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         cwd=os.path.abspath(BOTS_PATH+self.bot1+"/"))
        p2 = subprocess.Popen("./start", stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         cwd=os.path.abspath(BOTS_PATH+self.bot2+"/"))
        if p1.stdout.readline()!="OK\n":
            self.error = 1
            return
        if p2.stdout.readline()!="OK\n":
            self.error=2
            return
        p1.stdin.write("A\n")
        p2.stdin.write("A\n")
        for k in range(50):
            r1 = p1.stdout.readline().rstrip()
            r2 = p2.stdout.readline().rstrip()
            if r1=="C" and r2=="C":
                score1+=5
                score2+=5
            if r1=="C" and r2=="T":
                score1+=0
                score2+=10
            if r1=="T" and r2=="C":
                score1+=10
                score2+=0
            if r1=="T" and r2=="T":
                score1+=1
                score2+=1

            p1.stdin.write(r2+'\n')
            p2.stdin.write(r1+'\n')
        p1.stdin.write("Q\n")
        p2.stdin.write("Q\n")
        self.scores=[score1, score2]


contenders=list()

for c in bots:
    if not os.path.exists(BOTS_PATH+c):
        print "Error, could not find bot '"+c+"'. Ignoring"
    else:
        contenders.append(c)

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
