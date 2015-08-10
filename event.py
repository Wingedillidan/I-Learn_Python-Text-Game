# Each random event consists of a type (trail, specific town, etc.) and a scenario the player must resolve.
# 
# 

import random

class RandEvent(object):

    def __init__(self):
        pass


### ----------------- RIVER EVENTS ------------------
    
class Snakes(RandEvent):
    
    def scenario(self):
        print "OH NOES! SNAKES!"
    
    
class Rudder(RandEvent):
    
    def scenario(self):
        pass

### --------------- <TOWN NAME> EVENTS ---------------




### ----------------- RANDOMIZE ME! ------------------

class Generate(object):
    
    def __init__(self):
        pass