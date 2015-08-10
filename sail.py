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
    
    def setsail(self, length, day):
        pass


class Town(object):
    pass


class Chimvera(Town):
    pass


class Privako(Town):
    pass
    
    
class Kaapa(Town):
    pass

    
class Bonco(Town):
    pass


class PoopTown(Town):
    pass


class Map(object):
    Towns = {'Chimvera': Chimvera(), 'Privako': Privako(), 'Kaapa': Kaapa(), \
             'Bonco': Bonco(), 'PoopTown': PoopTown()}
    
    def __init__(self, start):
        self.start = Towns[start]
        self.nextTown = None
    
    
    def town(self):
        if not self.next:
            self.next = Towns[self.start.enter()]
        else:
            self.next = Towns[self.next.enter()]
    
    def num(self):
        return len(Towns)

            
class Journey(object):
    def __init__(self, map):
        self.map = map
    
    
    def begin(self, rlength=(15,10,20)):
        path = River()
        day = 0
        
        for section in xrange(0, self.map.num()-1)
            self.map.town()
            day += 1
            
            path.setsail(rlength[section], day)