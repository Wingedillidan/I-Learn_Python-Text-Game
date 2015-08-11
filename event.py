# Each random event consists of a type (trail, specific town, etc.) and a scenario the player must resolve.
# 
# Code by Collin McLean

import random

class RandEvent(object):
    
    def __init__(self, msg_invalid="Didn't understand that :/"):
        self.invalid = msg_invalid
    
    def options(self, question, answers, prompt='> '):
        print question
        
        for i in xrange(1, len(answers):
            print '[%(i)i]' % i
        
        while True:
            response = raw_input(prompt)
            
            try:
                if int(response) < len(answers):
                    return int(response)
            except ValueError:
                pass
            
            for answer in answers:
                if answer 

### ----------------- RIVER EVENTS ------------------
    
class Snakes(RandEvent):
    
    def scenario(self):
        print "OH NOES! SNAKES ARRIVED ON YOUR BOAT!\n\n"
    
    
class Rudder(RandEvent):
    
    def scenario(self):
        print "OH NOES! Rudder jam!"

### --------------- <TOWN NAME> EVENTS ---------------




### ----------------- RANDOMIZE ME! ------------------

class Generate(object):
    
    events = [Snakes(), Rudder()]
    
    def __init__(self):
        i = random.randint(0, len(self.events)-1)
        
        self.events[i].scenario()
    