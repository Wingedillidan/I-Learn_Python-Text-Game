# Oregon trail style game that puts the player sailing on a boat in a probably
# post-apocalyptic world wherein you must sail through x1 amount of port towns
# and encounter dangerous events along the way.
#
# Every town consists of the town itself as-well-as the process of sailing to
# it, which is calculated as each event equals one section of river, the speed
# of your travel modifies how many events you get so the sections consist of a
# flexible theoretical time... this is still a WIP. River events are randomized
# scenarios.
# Type of boat? Uhhhhh
#
# Code by Collin McLean

import tools
import event
from player import carmine
from sys import exit

# =================================================
# ------------------ TOWNS -------------------
# =================================================


class Town(object):
    """Base town class, introduces the function that runs the river travel
    to the destination town."""

    # Distance is equivalent to amount of possible river events
    distance = 0
    odds = 0
    name = None

    def __init__(self):
        pass

    def sail(self):
        """Runs every event, or the distance, to the town and adjusts according
        to the speed set by the player."""

        events = event.Library()

        # To do, figure out better way to manage speed
        for i in xrange(0, self.distance+carmine.speed):
            # Each river event costs the player's ship 5hp for wear & tear
            # in post-apocalyptic environments (everything is post-
            # apocalyptic... I think)
            carmine.change(hp=-5, place="River")
            tools.clear(5)
            print 'Day {} - Health: {}\n'.format(carmine.day,
                                                 carmine.hp)
            events.generate(self.odds)

            tools.next()
            carmine.change(day=1)

        carmine.change(place=self.name)
        tools.clear()
        print 'Day {} - Health: {}\n'.format(carmine.day, carmine.hp)
        result = self.enter()
        carmine.change(day=1)

        return result

    def enter(self):
        """Define this within a specific town class, you 'enter'ed
        into town."""
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

    def __init__(self, start):
        # Is there a better way of doing this?
        self.towns = {'Chimvera': Chimvera(),
                      'Privako': Privako(),
                      'Kaapa': Kaapa(),
                      'PoopTown': PoopTown()
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
