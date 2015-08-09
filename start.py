from char import Character
from response import YesNo

class StatGen(object):
    
    def __init__(self, character):
        self.char = character
    
    
    def generate(self, rerolls=3):
        rr = rerolls
    
        for stat in ('combat', 'luck', 'health'):
            while True:
                self.rollstat(stat)
                
                if rr > 0:
                    if YesNo('Would you like to use a reroll? Y/N [%(reroll)i left]' % \
                            {'reroll': rr}) == False:
                        break
                    else:
                        rr -= 1
                else:
                    break
    
    
    def rollstat(self, stat):
        result = ()
        
        if stat == 'combat':
            result = (self.char.roll(1)+6, 12)
            self.char.combat = result[0]
        elif stat == 'luck':
            result = (self.char.roll(1)+6, 12)
            self.char.luck = result[0]
        elif stat == 'health':
            result = (self.char.roll(2)+12, 24)
            self.char.health = result[0]
        else:
            print "ERROR in StatGen, invalid stat ('%(stat)s') selection.\n\n" % {'stat': stat}
        
        print "\n\n[%(stat)s] You rolled a %(roll)i out of a possible total of %(max)i." % \
              {'stat': stat, 'roll': result[0], 'max': result[1]}
              

class Welcome(object):
    
    def __init__(self, character):
        self.char = character
    
    
    def start   