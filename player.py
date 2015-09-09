import random


class Ship(object):
    """Player object defined as the ship sailing on the river."""

    # Add silly death messages to me =D
    lose_msgs = ['You deaded', 'DOOOOOOOOM!', 'You have been made unalive',
                 'Over Game :c', 'GG', 'You got rekt', 'RIP',
                 'Lel, supes dead', 'GG no re', 'Fin']

    def __init__(self, hp=100, fuel=0, food=0, scrap=0, day=0, place=None):
        """Retains ship stats: health, fuel level (WIP), stored food (WIP),
        scrap (1 scrap increases chances at a full 25hp rebuild), day, and
        speed (modifies amount of river sections to destination, WIP)."""

        self.hp = hp
        self.fuel = fuel
        self.food = food
        self.scrap = scrap
        self.day = day
        self.speed = 0
        self.crew = 0
        self.place = place
        self.contents = {'hp': self.hp, 'fuel': self.fuel, 'food': self.food,
                         'scrap': self.scrap, 'day': self.day,
                         'speed': self.speed, 'crew': self.crew,
                         'place': self.place
                         }

    def check(self):
        # Move around the lose function to incorporate it here

        if self.hp <= 0:
            i = random.randint(0, len(self.lose_msgs)-1)
            print self.lose_msgs[i]
            exit(0)

    def change(self, hp=0, fuel=0, food=0, scrap=0, day=0, speed=0,
               crew=0, place=None):
        """Adjusts the ship stats and then checks for any possible
        lose conditions"""

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

carmine = Ship()
