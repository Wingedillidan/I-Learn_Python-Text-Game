# Each random event consists of a type (trail, specific town, etc.) and a
# scenario the player must resolve.
# Code by Collin McLean

import random
import tools
from ui import printer
from player import carmine
from sys import exit


class Event(object):
    """Base event class, enclosed are a few tools generally used across
    all events."""

    def __init__(self, msg_invalid="Didn't understand that :/"):
        """msg_invalid used for unacceptable answers in the 'ask' function"""
        self.invalid = msg_invalid

    def ask(self, question, answers, prompt='> '):
        """Function to ask and process a question, 'answers' should be in a
        list object"""
        printme = question + '\n'

        # displays answers
        for i in xrange(0, len(answers)):
            printme += '[%(i)i] %(answer)s' % \
                {'i': i+1, 'answer': answers[i]} + '\n'

        printer.display(printme)

        # interprets the user's response, a valid response can be the integer
        # of the answer's position, OR the full answer typed out.
        while True:
            response = raw_input(prompt)

            try:
                if int(response)-1 < len(answers) and int(response) >= 0:
                    tools.clear(1)
                    return int(response)-1
            except ValueError:
                pass

            for i in xrange(0, len(answers)):
                if answers[i].lower().strip() == response.lower().strip():
                    tools.clear(1)
                    return i

            print self.invalid

    def error(self, msg="Error'd, received an unpossible output from \
                         'ask'ed question"):
        """Game error output"""

        print msg
        exit(1)


# =================================================
# ----------------- RIVER EVENTS ------------------
# =================================================

class Snakes(Event):

    def scenario(self):
        printer.display("OH NOES! SNAKES ARRIVED ON YOUR BOAT!")

        response = self.ask('How to unsnake the boat?',
                            ['Yell at them', 'Eat them'])

        if response == 0:
            print "You yell as loud as you can, the snakes don't understand \
                   fleshbag. [-10 health]"
            carmine.change(hp=-10)
        elif response == 1:
            print "You ate ALL the snakes, looks like you wiggled your way \
                   out of this one. [+2 food]"
            carmine.change(food=2)
        else:
            self.error()


class Rudder(Event):

    def scenario(self):
        print "OH NOES! Your rudder ajam!"

        response = self.ask('What do?',
                            ['Use a stick to clear the clutter', 'Improvise'])

        if response == 0:
            print "Your stick only added to the jam. [-15 health]"
            carmine.change(hp=-15)
        elif response == 1:
            print" IMPROV!"
        else:
            self.error()


class Grammar(Event):

    def scenario(self):
        print "OH NOES! Your entire crew was infected by the virus of \
               poor grammar."
        print "Generic Crewmun: \"Your going to die captain!\""

        response = self.ask('How win?',
                            ['Teach proper grammer',
                             'Revert ship to text talk'])

        if response == 0:
            # GET RID OF HARD CODE NAOW!
            print "It took some time, but eventually every one learned there \
                   grammar again... eventually [+1 day] [-5 health]"

            carmine.change(day=1, hp=-5)
        elif response == 1:
            # Again, self, not this, you're better than this...
            print "The grammar nazis invaded. [-20 health]"
            carmine.change(hp=-20)
        else:
            self.error()


class Seattle(Event):

    def scenario(self):
        print "Are you properly disposing of your compostable waste?"

        response = self.ask('Your answer?', ['No...', 'LIE!'])

        if response == 1:
            print '50/50 shot...'
            tools.next()
            if random.randint(0, 1) == 1:
                response = 2

        if response == 2:
            print 'Uh-huh... we need to have a chat [+2 days] [-10 health]'
            carmine.change(hp=-10, day=2)
        elif response == 1:
            print 'Alright then, carry on...'
        elif response == 0:
            print 'Well, in this part of the river we compost, let me tell \
                   you why... [+1 day] [-5 health]'
            carmine.change(hp=-5, day=1)
        else:
            self.error()


class Fork(Event):

    def scenario(self):
        print "You arrive at a fork in the river..."

        response = self.ask('Which way?', ['Left', 'Right'])

        if response == random.randint(0, 1):
            print "The water is a bit rough, but luckily you manage to get \
                   through safely..."
        else:
            things = ['Birds', 'Monkey', 'Dicks', 'Narwhals', 'Unicorns']
            i = random.randint(0, len(things)-1)

            print "{} attacked your ship D: [-10 health]".format(things[i])
            carmine.change(hp=-10)


class Abandoned(Event):

    def scenario(self):
        print "You pass by a ship that has been utterly rekt..."

        response = self.ask('Do you check the wreckage?', ['Yes', 'No'])

        if response == 0:
            if random.randint(0, 1) == 1:
                i = random.randint(1, 5)
                print "Hooray! Some scrap! [+{} scrap]".format(i)
            else:
                print "SEA ZOOOMBIES!!!"
                if random.randint(0, 1) == 1:
                    print "RUUUUUN [+1 day] [-5 health]"
                    carmine.change(day=1, hp=-5)
                else:
                    print "Ya got overwhelmed a bit [+2 days] [-15 health]"
                    carmine.change(day=2, hp=-15)


class Nothing(Event):

    def scenario(self):
        print "It's calm in this stretch of river."


# ==================================================
# --------------- <TOWN NAME> EVENTS ---------------
# ==================================================


# ==================================================
# ------------- EVENT MANAGER CLASSES --------------
# ==================================================


class Library(object):
    """Manages event objects and randomly calls them up for adventureness"""

    def __init__(self):
        self.events = [Snakes(),
                       Rudder(),
                       Grammar(),
                       Seattle(),
                       Fork(),
                       Abandoned()
                       ]

    def generate(self, odds=70):
        """Calls an event object, anything above the odds argument signals
        that there is no event/calm waters."""

        if random.randint(0, 100) > odds:
            Nothing().scenario()
        else:
            i = random.randint(0, len(self.events)-1)
            self.events[i].scenario()
