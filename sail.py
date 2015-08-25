# Oregon trail style game that puts the player sailing on a boat in a probably post-apocalyptic world wherein
# you must sail through x1 amount of port towns and encounter dangerous events along the way.
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

    # Add silly death messages to me =D
    lose_msgs = ['You deaded', 'DOOOOOOOOM!', 'You have been made unalive', 'Over Game :c',
                 'GG', 'You got rekt', 'RIP', 'Lel, supes dead', 'GG no re', 'Fin']

    def __init__(self, hp=100, fuel=0, food=0, scrap=0, day=0, place=None):
        """Retains ship stats: health, fuel level (WIP), stored food (WIP), scrap (1 scrap increases chances
        at a full 25hp rebuild), day, and speed (modifies amount of river sections to destination, WIP)."""

        self.hp = hp
        self.fuel = fuel
        self.food = food
        self.scrap = scrap
        self.day = day
        self.speed = 0
        self.crew = 0
        self.place = place
        self.contents = {'hp': self.hp, 'fuel': self.fuel, 'food': self.food, 'scrap': self.scrap, 
            'day': self.day, 'speed': self.speed, 'crew': self.crew, 'place': self.place}
    
    def check(self):
        ### Move around the lose function to incorporate it here
        
        if self.hp <= 0:
            i = random.randint(0, len(self.lose_msgs)-1)
            print self.lose_msgs[i]
            exit(0)
    
    
    def change(self, hp=0, fuel=0, food=0, scrap=0, day=0, speed=0, crew=0, place=None):
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

        if place:
            self.place = place

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
    name = None

    def __init__(self, ship, ui):
        self.player = ship
        self.ui = ui


    def sail(self):
        """Runs every event, or the distance, to the town and adjusts according
        to the speed set by the player."""

        events = event.Library(self.player, self.ui)

        ### To do, figure out better way to manage speed
        for i in xrange(0, self.distance+self.player.speed):
            # Each river event costs the player's ship 5hp for wear & tear
            # in post-apocalyptic environments (everything is post-apocalyptic... I think)
            self.player.change(hp=-5, place="River")
            tools.clear(5)
            print 'Day {} - Health: {}\n'.format(self.player.day, self.player.hp)
            events.generate(self.odds)

            tools.next()
            self.player.change(day=1)

        self.player.change(place=self.name)
        tools.clear()
        print 'Day {} - Health: {}\n'.format(self.player.day, self.player.hp)
        result = self.enter()
        self.player.change(day=1)

        return result


    def enter(self):
        """Define this within a specific town class, you 'enter'ed into town."""
        print "Error'd, blank town object used."


class Chimvera(Town):

    name = 'Chimvera'

    def enter(self):
        print "CHIMVERA HOLDER"

        return 'Privako'


class Privako(Town): 

    name = 'Privako'
    distance = 5
    odds = 70

    def enter(self):
        print "PRIVAKO HOLDER"

        return 'Kaapa'


class Kaapa(Town):

    name = 'Kaapa'
    distance = 5
    odds = 80

    def enter(self):
        print "KAAPA HOLDER"

        return 'PoopTown'


class PoopTown(Town):

    name = 'PoopTown'
    distance = 10
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
