import random, tools

class Room(object):
    
    def __init__(self, prompt='> '):
        self.prompt = prompt
        self.dark = False
        

class Foyer(Room):
    
    def enter(self):
        print "You enter the Foyer."
        print "Infront of you lies a grand staircase that reaches 2 stories tall." \
              "alongside are 2 magnificent doorways on either side.\n\n"
        
        print "Valid directions are East, West, and Up"
        
        return self.exit()
    
    def exit(self):
        while True:
            response = tools.answer(self.prompt)
            
            if response == 'go east':
                return 'EastHall'
            elif response == 'go west':
                return 'WestHall'
            elif response == 'go up':
                return 'UpperHall'
            elif ('look' and 'up') in response:
                print "It's a staircase oOoOoOoOo"
            elif 'look' in response:
                print "It's a door!"
            else:
                print "I couldn't quite get that..."
    
    
class WestHall(self):
    def __init__(self, dark):
        self.dark = dark
    
    
    def dark(self):
        print "It is too dark =("
        return "Return"
    
    
    def enter(self):
        print "You enter the South Hallway"
        
        if self.dark == True:
            return self.dark()
        
        print "There is a single door on either side, and the hallway stretches on...\n\n"
        
        print "Valid directions are North, East, and West."
        
        return self.exit()
    
    
    def exit(self):
        pass


