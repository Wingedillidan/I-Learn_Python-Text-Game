# Each random event consists of a type (trail, specific town, etc.) and a scenario the player must resolve.
# 
# Code by Collin McLean

import random, tools
from sys import exit

class Event(object):
    """Base event class, enclosed are a few tools generally used across all events."""
    
    # Add silly death messages to me =D
    lose_msgs = ['You deaded', 'DOOOOOOOOM!', 'You have been made unalive', 'Over Game :c',
                 'GG', 'You got rekt', 'RIP', 'Lel, supes dead', 'GG no re', 'Fin']
    
    def __init__(self, player, ui, msg_invalid="Didn't understand that :/"):
        """msg_invalid used for unacceptable answers in the 'ask' function"""
        self.invalid = msg_invalid
        self.player = player
        self.ui = ui
    
    
    def ask(self, question, answers, prompt='> '):
        """Function to ask and process a question, 'answers' should be in a list object"""
        ### add randomization to answer ordering? Randomize or make a crapton of questions/events
        print question
        
        # displays answers
        for i in xrange(0, len(answers)):
            print '[%(i)i] %(answer)s' % {'i': i+1, 'answer': answers[i]}
        
        # interprets the user's response, a valid response can be the integer of the answer's
        # position, OR the full answer typed out.
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
        """Game over output"""
        
        # error argument created with the original intention of handling impossible
        # outputs from the 'ask' function
        if msg:
            print msg
        else:
            i = random.randint(0, len(self.lose_msgs)-1)
            print self.lose_msgs[i]
        
        if error == 0:
            tools.next()
        
        exit(0)

### =================================================
### ----------------- RIVER EVENTS ------------------
### =================================================
    
class Snakes(Event):
    
    def scenario(self):
        print "OH NOES! SNAKES ARRIVED ON YOUR BOAT!"
        
        response = self.ask('How to unsnake the boat?', ['Yell at them', 'Eat them'])
        
        if response == 0:
            print "You yell as loud as you can, the snakes don't understand fleshbag. [-10 health]"
            self.player.change(hp=-10)
        elif response == 1:
            print "You ate ALL the snakes, looks like you wiggled your way out of this one. [+2 food]"
            self.player.change(hp=2)
        else:
            self.lose("Error'd, received an unpossible output from 'ask'ed question", 1)
    
    
class Rudder(Event):
    
    def scenario(self):
        print "OH NOES! Your rudder ajam!"
        
        response = self.ask('What do?', ['Use a stick to clear the clutter', 'Improvise'])
        
        if response == 0:
            print "Your stick only added to the jam. [-15 health]"
            self.player.change(hp=-15)
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
            print "It took some time, but eventually every one learned there grammar again... eventually [+1 day] [-5 health]" ### GET RID OF HARD CODE NAOW!
            
            ### make this better >.<
            self.player.change(day=1, hp=-5)
        elif response == 1:
            print "The grammar nazis invaded. [-20 health]" ### Again, self, not this, you're better than this...
            self.player.change(hp=-20)
        else:
            self.lose("Error'd, received an unpossible output from 'ask'ed question", 1)
            

class Nothing(Event):
    
    def scenario(self):
        print "It's calm in this stretch of river."
        
        
### ==================================================
### --------------- <TOWN NAME> EVENTS ---------------
### ==================================================



### ==================================================
### ------------- EVENT MANAGER CLASSES --------------
### ==================================================

            
class Library(object):
    """Manages event objects and randomly calls them up for adventureness"""
    
    def __init__(self, player, ui):
        self.ui = ui
        self.player = player
        self.events = [Snakes(self.player, self.ui), Rudder(self.player, self.ui), Grammar(self.player, self.ui)]
        
    
    def generate(self, odds=70):
        """Calls an event object, anything above the odds argument signals
        that there is no event/calm waters."""
        
        if random.randint(0,100) > odds:
            Nothing(self.player, self.ui).scenario()
        else:
            i = random.randint(0, len(self.events)-1)
            self.events[i].scenario()
        