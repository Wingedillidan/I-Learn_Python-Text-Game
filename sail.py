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

    towns = {'Chimvera': Chimvera(),
        'Privako': Privako(),
        'Kaapa': Kaapa(),
        'Bonco': Bonco(),
        'PoopTown': PoopTown()
    }
    
    def __init__(self, start):
        self.start = self.towns.get(start)
        self.nextTown = None
    
    
    def town(self):
        if not self.next:
            self.next = self.towns[self.start.enter()]
        else:
            self.next = self.towns[self.next.enter()]
    
    def num(self):
        return len(self.towns)

            
class Journey(object):
    def __init__(self, map):
        self.map = map
    
    
    def begin(self, rlength=(15,10,20)):
        path = River()
        day = 0
        
        for part in xrange(0, self.map.num()-1):
            # self.map.town()
            day += 1
            
            # if the rlength tuple (tracks journey length between towns) does not have enough values, it will
            # assume the towns are neighboring and have a 0 unit distance.
            if not part > len(rlength)-1:
                for section in xrange(0, rlength[part]):
                    path.setsail()
                    day += 1
            