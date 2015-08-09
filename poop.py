from sys import exit
import random

class Room(object):

    def __init__(self, thing):
        self.thing = thing
    
    
    def answer(self, prompt='> '):
        return raw_input(prompt).strip().lower()
    
    
    def clear(self, lines=50):
        print '\n' * lines
    
    
    def pressenter(self, prompt='PRESS ENTER TO CONTINUE'):
        raw_input(prompt)


class Welcome_Room(Room):

    def enter(self):
        self.clear()
        
        print "Welcome to the poop gates, many enter, several call this place: \"Crap\""
        print "Before you lies a large set of porcelain gates, a white statue lies in front of you... is a bowl with a lid."
        print "What do you do?"
        
        while True:
            response = self.answer()
            
            if 'poop' in response:
                print "You enter the Dungeon of Poop!"
                self.pressenter()
                
                return "Foyer_Room"
            elif ('leave' or 'exit') in response:
                print "You exit the dungeon, YOU WIN! GG."
                self.pressenter()
                
                exit(0)
            else:
                print "You hear a faint fart: 'Use your butt, not your head' ... try again."


class Foyer_Room(Room):
    
    def enter(self):
        self.clear()