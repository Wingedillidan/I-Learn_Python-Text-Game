# Oregon trail style game with random events along the journey, except in a boat on the river.
# There are 3 sections of riverway, each consist of (15, 10, 20) tiles, therefore there are 4 towns/stops
# Sea is too open, open world games means lots of extra work =(
# Possible names: Chrimvera, Privako
# Type of boat? Uhhhhh
# 
# Code by Collin McLean

import tools, event, random

class Ship(object):
    
    def __init__(self, hp=100, fuel=0, food=0, scrap=0, day=0):
        self.hp = hp
        self.fuel = fuel
        self.food = food
        self.scrap = scrap
        self.day = day
        self.speed = 0
    
    def UI(self):
        pass
        # Where I left off 8/15/2015
        

class River(object):

    def __init__(self):
        pass
    
    def setsail(self, odds=70):
        if random.randint(0, 100) > odds:
            event.Nothing().scenario()
        else:
            event.Generate()


class Town(object):

    distance = 0
    odds = 0
    
    def __init__(self, ship):
        self.player = ship
    
    
    def sail(self):
        for i in xrange(0, self.distance+self.player.speed):
            tools.clear(2)
            
            self.player.hp -= 5
            print 'Day', self.player.day, '\nHealth:', self.player.hp
            River().setsail()
                    
            tools.next()
            self.player.day += 1
        
        tools.clear(2)
        print 'Day', self.player.day, '\nHealth:', self.player.hp
        
        result = self.enter()
        tools.next()
        tools.clear()
        self.player.day += 1
        
        return result
    
    
    def enter(self):
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
    
    def __init__(self, start, ship):
        self.player = ship
        
        self.towns = {'Chimvera': Chimvera(self.player),
        'Privako': Privako(self.player),
        'Kaapa': Kaapa(self.player),
        'PoopTown': PoopTown(self.player)
        }
        
        self.next = self.towns.get(start)
    
    
    def town(self):
        self.next = self.towns.get(self.next.sail())
    
    def num(self):
        return len(self.towns)

            
class Journey(object):
    def __init__(self, map):
        self.map = map
    
    
    def begin(self):
        while True:
            self.map.town()
                    

player = Ship()
map = Map("Chimvera", player)
engine = Journey(map)
engine.begin()