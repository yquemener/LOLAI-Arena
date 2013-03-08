#!/usr/bin/env python
#-*- coding:utf8-*-

# ------------------------------
# Imports
# ------------------------------ 
import os
import subprocess
import uuid


# ------------------------------
# Classes
# ------------------------------ 
DEBUG = {"send" : 1}

class HistoryData(object):
    """ Descriptor. It will allow to store automaticaly some data on update
    
    It should work like that
    o = Object() # any object
    o.attribute = HistoryData()
    o.attribute = 2     # call __set__ of HistoryData and sets attribute to 2 and sets o.history[attribute] to [2] 
    o.attribute = 3     # call __set__ of HistoryData and sets attribute to 3 and sets o.history[attribute] to [2,3] 
    
    """
    def __init__(self, attribute, value=None):
        if value != None:
            self.history = [value]

    def __get__(self, obj, objtype):
        print "------------------"
        print "Now: {val}".format(val = self.history[-1])
        print "History: {hist}".format(hist = self.history)
        return self.history[-1]

    def __set__(self, obj, value):
        # Saving old value
        self.history.append(value)

    def get_history(self):
        return self.history


class Bot(object):
    """Bot class
    
    """

    plop = HistoryData('plop', 4)

    def __init__(self, name, bots_path, attributes_hist = []):
        """Initiates bot class

        @param name: the name of the bot (which correspond to the name of the folder)
        @param bots_path: path where bots are

        """
        self.check_name(name, bots_path)
        self.uuid = str(uuid.uuid4())
        self.score = 0

        for attr in attributes_hist:
            setattr(self.__class__ , attr, HistoryData(attr,0))
        
    def check_name(self, name, bots_path):
        """Checks if the name correspond to a folder containing program
    
        @param name: the name of the bot (which correspond to the name of the folder)
        @param bots_path: path where bots are
        
        """
        if not os.path.exists(bots_path + name):
            raise ValueError("Could not find bot '{bot}'".format(bot=bots_path + name))
        else:
            self.name = name
            self.path = bots_path + name + os.sep

    def start_bot(self):
        """Starts the subprocess associated to the bot 
        
        """
        self.proc = subprocess.Popen("./start", stdin=subprocess.PIPE,
									 stdout=subprocess.PIPE,
									 cwd=os.path.abspath(self.path))

    def ready(self):
        """Checks if the bot is ready to play or raise an error.
        
        """
        if self.proc.stdout.readline() != "OK\n":
            raise ValueError("Le bot {bot} n'arrive pas à se préparer".format(bot=self.name))

    def send_msg(self, msg):
        """Sends message to the bot
    
        @param msg: the message to send
        
        """
        self.proc.stdin.write(msg+"\n")

        if DEBUG["send"]:
            print "Send to bot {bot}: \n\t {msg}".format(bot = self.name, masg = msg)

    #TODO: rename get_ans to get_answer!!!
    def get_ans(self):
        """Gets the answer of the bot
        
        @return: the bot's answer
        
        """
        return self.proc.stdout.readline().rstrip()

    def __str__(self):
        """ Overload __str__ to get a nice print

        @return: nice presentation
        """
        return "Bot {name} num: {uuid}".format(name = self.name , uuid = self.uuid)



# ------------------------------
# Fonctions
# ------------------------------ 

# ------------------------------
# Bloc principal
# ------------------------------

if __name__ == '__main__':
    b = Bot("shy", "../Games/Calebasse/bots/", ['ble'])
    print dir(b)
    #b.ble = HistoryData("ble")
    print b.ble
    print b.__dict__
    b.ble = 2
    b.ble
    b.ble = 3
    b.ble
    b.ble += 4
    b.ble

    print b.__dict__
    print b.plop
    b.plop = 2
    b.plop
    b.plop = 3
    b.plop
    b.plop += 4
    b.plop

    print dir(b)
# ------------------------------
# Fin du programme
# ------------------------------

# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 

