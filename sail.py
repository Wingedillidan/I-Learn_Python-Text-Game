# Oregon trail style game that puts the player sailing on a boat in a probably post-apocalyptic world wherein
# you must sail through x amount of port towns and encounter dangerous events along the way.
#
# Every town consists of the town itself as-well-as the process of sailing to it, which is calculated
# as each event equals one section of river, the speed of your travel modifies how many events you get
# so the sections consist of a flexible theoretical time... this is still a WIP. River events are
# randomized scenarios.
# Type of boat? Uhhhhh 
#
# Code by Collin McLean

import tools, event, random, ui
from sys import exit

### =================================================
### ------------------ THE PLAYER -------------------
### =================================================

class Ship(object):
    """Player object defined as the ship sailing on the river."""
    
    ### MAKE THIS WORK
    # ui = ui.Controller()
    
    
    def __init__(self, hp=100, fuel=0, food=0, scrap=0, day=0):
        """Retains ship stats: health, fuel level (WIP), stored food (WIP), scrap (1 scrap increases chances
        at a full 25hp rebuild), day, and speed (modifies amount of river sections to destination, WIP)."""
        
        self.hp = hp
        self.fuel = fuel
        self.food = food
        self.scrap = scrap
        self.day = day
        self.speed = 0
        self.crew = 0
    
    def check(self):
        ### Move around the lose function to incorporate it here
        
        if self.hp <= 0:
            print "Your ship is rekt!"
            exit(0)
    
    
    def change(self, hp=0, fuel=0, food=0, scrap=0, day=0, speed=0, crew=0):
        """Adjusts the ship stats and then checks for any possible lose conditions"""
        
        if self.hp + hp > 100:
            self.hp = 100
        else:
            self.hp += hp
            
        self.fuel += fuel
        self.food += food
        self.scrap += scrap
        self.day += day
        self.speed += speed
        self.crew += crew
        
        self.check()


### =================================================
### ------------------ TOWNS -------------------
### =================================================

class Town(object):
    """Base town class, introduces the function that runs the river travel
    to the destination town."""
    
    # Distance is equivalent to amount of possible river events
    distance = 0
    odds = 0
    
    def __init__(self, ship, ui):
        self.player = ship
        self.ui = ui
    
    
    def sail(self):
        """Runs every event, or the distance, to the town and adjusts according
        to the speed set by the player."""
        
        events = event.Library(self.player, self.ui)
        
        ### To do, figure out better way to manage speed
        for i in xrange(0, self.distance+self.player.speed):
            tools.clear(2)
            
            # Each river event costs the player's ship 5hp for wear & tear
            # in post-apocalyptic environments (everything is post-apocalyptic... I think)
            self.player.hp -= 5
            print 'Day', self.player.day, '\nHealth:', self.player.hp
            events.generate(self.odds)
            
            tools.next()
            self.player.day += 1
        
        tools.clear(2)
        print 'Day', self.player.day, '\nHealth:', self.player.hp
        
        ### Fix formatting, this needs its own function or class
        result = self.enter()
        tools.next()
        tools.clear()
        self.player.day += 1
        
        return result
    
    
    def enter(self):
        """Define this within a specific town class, you 'enter'ed into town."""
        print "Error'd, blank town object used."


class Chimvera(Town):
    
    def enter(self):
        print "CHIMVERA HOLDER"
        
        return 'Privako'


class Privako(Town): 
    
    distance = 5
    odds = 70
    
    def enter(self):
        print "PRIVAKO HOLDER"
        
        return 'Kaapa'
    
    
class Kaapa(Town):
    
    distance = 1
    odds = 80
    
    def enter(self):
        print "KAAPA HOLDER"
        
        return 'PoopTown'


class PoopTown(Town):
    
    distance = 1
    odds = 90
    
    def enter(self):
        print "Congrats, you made it to the end! Welcome to PoopTown."
        
        exit(0)


class Journey(object):
    """Stores and navigates through the towns based on an order stored within
    each individual town object"""
    
    def __init__(self, start, ship, ui):
        """The ship argument is the player."""
        
        self.player = ship
        self.ui = ui
        
        ### Is there a better way of doing this?
        self.towns = {'Chimvera': Chimvera(self.player, ui),
        'Privako': Privako(self.player, ui),
        'Kaapa': Kaapa(self.player, ui),
        'PoopTown': PoopTown(self.player, ui)
        }
        
        self.next = self.towns.get(start)
    
    
    def begin(self):
        """The specific town returns the proper string"""
        while True:
            self.next = self.towns.get(self.next.sail())
    
    def num(self):
        """Number of towns mapped out (any towns missing from the game need to be
        added to the towns dict within this class."""
        return len(self.towns)