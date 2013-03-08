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

class Bot(object):
    """Bot class
    
    """

    def __init__(self, name, bots_path, attributes_hist = []):
        """Initiates bot class

        @param name: the name of the bot (which correspond to the name of the folder)
        @param bots_path: path where bots are

        """
        self.check_name(name, bots_path)
        self.uuid = str(uuid.uuid4())
        self.score = 0

        for attr in attributes_hist:
            self.add_hist_property(attr)
        
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


    def add_hist_property(self, attribute, doc="Auto-generated method"):
        """ This attribute begin a property. It will build automaticaly a history

        @param attribute: the name of the attribute
        """
        # create local setter and getter with a particular attribute name 
        getter = lambda self: self._get_hist_property(attribute)
        setter = lambda self, value: self._set_hist_property(attribute, value)

        # construct property attribute and add it to the class
        setattr(self.__class__, attribute, property(fget=getter, \
                                                    fset=setter, \
                                                    doc=doc))
        setattr(self, "hist_" + attribute, [])
        # I would like to understand the difference between self and self.__class__ in this example

    def _set_hist_property(self, attribute, value):
        """ How to set an attribute with an history
        This value is actually stored in self._attribute but it can be used as any attribute (self.attribute)
        """
        setattr(self, "_" + attribute, value)    

        getattr(self, "hist_"+attribute).append(value)

    def _get_hist_property(self, attribute):
        """ How to get an attribute with an history
        This value is actually stored in self._attribute but it can be used as any attribute (self.attribute)
        """
        if ("_"+attribute) in self.__dict__:
            return getattr(self,"_"+ attribute)
        else:
            return None



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
    b._ble
    b.ble
    b.ble = 3
    b._ble
    b.ble += 4
    b.ble
# ------------------------------
# Fin du programme
# ------------------------------

# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 

