# Oregon trail style game with random events along the journey, except in a boat on the river.
# There are 3 sections of riverway, each consist of (15, 10, 20) tiles, therefore there are 4 towns/stops
# Sea is too open, open world games means lots of extra work =(
# Possible names: Chrimvera, Privako
# Type of boat? Uhhhhh
# 
# Code by Collin McLean

import tools, event, random

class Ship(object):
    """Player object defined as the ship sailing on the river."""
    
    def __init__(self, hp=100, fuel=0, food=0, scrap=0, day=0):
        """Retains ship stats: health, fuel level (WIP), stored food (WIP), scrap (1 scrap increases chances
        at a full 25hp rebuild), day, and speed (modifies amount of river sections to destination, WIP)."""
        
        self.hp = hp
        self.fuel = fuel
        self.food = food
        self.scrap = scrap
        self.day = day
        self.speed = 0
    
    def UI(self):
        
        print 'HP:', self.hp
        
                    

class River(object):
    """Manages river event triggers and which ones trigger (pretty much all random)."""
    def __init__(self):
        pass
    
    def setsail(self, odds=70):
        """Calls a river event, anything above the odds threshold means
        nothing happens/calm waters."""
        
        if random.randint(0, 100) > odds:
            event.Nothing().scenario()
        else:
            event.Generate()


class Town(object):
    """Base town class, introduces the function that runs the river travel
    to the destination town."""
    
    # Distance is equivalent to amount of possible river events
    distance = 0
    odds = 0
    
    def __init__(self, ship):
        self.player = ship
    
    
    def sail(self):
        """Runs every event, or the distance, to the town and adjusts according
        to the speed set by the player."""
        
        ### To do, figure out better way to manage speed
        for i in xrange(0, self.distance+self.player.speed):
            tools.clear(2)
            
            # Each river event costs the player's ship 5hp for wear & tear
            # in post-apocalyptic environments (everything is post-apocalyptic... I think)
            self.player.hp -= 5
            print 'Day', self.player.day, '\nHealth:', self.player.hp
            River().setsail()
            
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


class Map(object):
    """Stores and navigates through the towns based on an order stored within
    each individual town object"""
    
    def __init__(self, start, ship):
        """The ship argument is the player."""
        
        self.player = ship
        
        ### Is there a better way of doing this?
        self.towns = {'Chimvera': Chimvera(self.player),
        'Privako': Privako(self.player),
        'Kaapa': Kaapa(self.player),
        'PoopTown': PoopTown(self.player)
        }
        
        self.next = self.towns.get(start)
    
    
    def town(self):
        """The specific town returns the proper string"""
        self.next = self.towns.get(self.next.sail())
    
    def num(self):
        """Number of towns mapped out (any towns missing from the game need to be
        added to the towns dict within this class."""
        return len(self.towns)

            
class Journey(object):
    """Game's Engine, needs a map to know where to go ;)"""
    
    def __init__(self, map):
        self.map = map
    
    
    def begin(self):
        ### Is there a way to do this better?
        ### Is there a way to reduce the amount of infrastructure classes?
        while True:
            self.map.town()