# Oregon trail style game with random events along the journey, except in a boat on the river.
# There are 3 sections of riverway, each consist of (15, 10, 20) tiles, therefore there are 4 towns/stops
# Sea is too open, open world games means lots of extra work =(
# Possible names: Chrimvera, Privako
# Type of boat? Uhhhhh
# 
# Code by Collin McLean

import tools, event

class River(object):

    def __init__(self):
        pass
    
    def setsail(self):
        event.Generate()


class Town(object):
    
    def __init__(self):
        pass


class Chimvera(Town):
    
    def enter(self):
        print "CHIMVERA HOLDER"
        
        return 'Privako'


class Privako(Town):
    
    def enter(self):
        print "PRIVAKO HOLDER"
        
        return 'Kaapa'
    
    
class Kaapa(Town):
    
    def enter(self):
        print "KAAPA HOLDER"
        
        return 'PoopTown'


class PoopTown(Town):
    
    def enter(self):
        print "Congrats, you made it to the end! Welcome to PoopTown."


class Map(object):

    towns = {'Chimvera': Chimvera(),
        'Privako': Privako(),
        'Kaapa': Kaapa(),
        'PoopTown': PoopTown()
    }
    
    river_lengths = (1, 1, 1)
    
    def __init__(self, start):
        self.next = self.towns.get(start)
    
    
    def town(self):
        self.next = self.towns.get(self.next.enter())
    
    def num(self):
        return len(self.towns)

            
class Journey(object):
    def __init__(self, map):
        self.map = map
    
    
    def begin(self):
        path = River()
        day = 0
        
        for part in xrange(0, self.map.num()):
            tools.clear()
            
            print 'Day', day
            self.map.town()
            
            tools.next(0)
            day += 1
            
            # if the rlength tuple (tracks journey length between towns) does not have enough values, it will
            # assume the towns are neighboring and have a 0 unit distance.
            if not part > len(self.map.river_lengths)-1:
                for section in xrange(0, self.map.river_lengths[part]):
                    tools.clear(2)
                    
                    print 'Day', day
                    path.setsail()
                    
                    tools.next(0)
                    day += 1

map = Map("Chimvera")
engine = Journey(map)
engine.begin()