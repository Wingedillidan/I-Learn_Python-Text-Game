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
    
    def __init__(self):
        pass
    
    
    def sail(self, player):
        for i in xrange(0, self.distance):
            tools.clear(2)
                    
            print 'Day', player.day
            River().setsail()
                    
            tools.next(0)
            player.day += 1
        
        print 'Day', player.day
        result = self.enter()
        player.day += 1
        
        return result
    
    
    def enter(self):
        print "Error'd, blank town object used."


class Chimvera(Town):
    
    def enter(self):
        print "CHIMVERA HOLDER"
        
        return 'Privako'


class Privako(Town):
    
    distance = 1
    
    def enter(self):
        print "PRIVAKO HOLDER"
        
        return 'Kaapa'
    
    
class Kaapa(Town):
    
    distance = 1
    
    def enter(self):
        print "KAAPA HOLDER"
        
        return 'PoopTown'


class PoopTown(Town):
    
    distance = 1
    
    def enter(self):
        print "Congrats, you made it to the end! Welcome to PoopTown."
        
        exit(0)


class Map(object):

    towns = {'Chimvera': Chimvera(),
        'Privako': Privako(),
        'Kaapa': Kaapa(),
        'PoopTown': PoopTown()
    }
    
    def __init__(self, start):
        self.next = self.towns.get(start)
    
    
    def town(self, player):
        self.next = self.towns.get(self.next.sail(player))
    
    def num(self):
        return len(self.towns)

            
class Journey(object):
    def __init__(self, map, ship):
        self.map = map
        self.player = ship
    
    
    def begin(self):
        while True:
            self.map.town(self.player)
                    

map = Map("Chimvera")
player = Ship()
engine = Journey(map, player)
engine.begin()