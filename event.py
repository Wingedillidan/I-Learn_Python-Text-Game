# Each random event consists of a type (trail, specific town, etc.) and a scenario the player must resolve.
# 
# Code by Collin McLean

import random, tools
from sys import exit

class Event(object):
    
    lose_msgs = ['You deaded', 'DOOOOOOOOM!', 'You have been made unalive', 'Over Game :c',
                 'GG', 'You got rekt', 'RIP', 'Lel, supes dead', 'GG no re', 'Fin']
    
    def __init__(self, msg_invalid="Didn't understand that :/"):
        self.invalid = msg_invalid
    
    
    def ask(self, question, answers, prompt='> '):
        print question
        
        for i in xrange(0, len(answers)):
            print '[%(i)i] %(answer)s' % {'i': i+1, 'answer': answers[i]}
        
        while True:
            response = raw_input(prompt)
            
            try:
                if int(response)-1 < len(answers) and int(response) >= 0:
                    tools.clear(1)
                    return int(response)-1
            except ValueError:
                pass
            
            for i in xrange(0, len(answers)):
                if answers[i].lower().strip() == response.lower().strip():
                    tools.clear(1)
                    return i
            
            print self.invalid
    
    
    def lose(self, msg=None, error=0):
        if msg:
            print msg
        else:
            i = random.randint(0, len(self.lose_msgs)-1)
            print self.lose_msgs[i]
        
        if error == 0:
            tools.next()
        
        exit(0)

### ----------------- RIVER EVENTS ------------------
    
class Snakes(Event):
    
    def scenario(self):
        print "OH NOES! SNAKES ARRIVED ON YOUR BOAT!"
        
        response = self.ask('How to unsnake the boat?', ['Yell at them', 'Eat them'])
        
        if response == 0:
            print "You yell as loud as you can, the snakes don't understand fleshbag."
            self.lose("You deaded. c( o_o c)")
        elif response == 1:
            print "You ate ALL the snakes, looks like you wiggled your way out of this one."
        else:
            self.lose("Error'd, received an unpossible output from 'ask'ed question", 1)
    
    
class Rudder(Event):
    
    def scenario(self):
        print "OH NOES! Your rudder ajam!"
        
        response = self.ask('What do?', ['Use a stick to clear the clutter', 'Improvise'])
        
        if response == 0:
            print "Your stick only added to the jam."
            self.lose()
        elif response == 1:
            print "IMPROV!"
        else:
            self.lose("Error'd, received an unpossible output from 'ask'ed question", 1)

            
class Grammar(Event):

    def scenario(self):
        print "OH NOES! Your entire crew was infected by the virus of poor grammar."
        print "Generic Crewmun: \"Your going to die captain!\""
        
        response = self.ask('How win?', ['Teach proper grammer', 'Revert ship to text talk'])
        
        if response == 0:
            print "It took some time, but eventually every one learned there grammar again... eventually"
        elif response == 1:
            print "The grammar nazis invaded."
            self.lose()
        else:
            self.lose("Error'd, received an unpossible output from 'ask'ed question", 1)
            

class Nothing(Event):
    
    def scenario(self):
        print "It's calm in this stretch of river."
        
        
### --------------- <TOWN NAME> EVENTS ---------------




### ----------------- RANDOMIZE ME! ------------------

class Generate(object):
    
    events = [Snakes(), Rudder()]
    
    def __init__(self):
        i = random.randint(0, len(self.events)-1)
        
        self.events[i].scenario()
    