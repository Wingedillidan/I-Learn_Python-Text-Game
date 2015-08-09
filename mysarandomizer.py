from datetime import datetime
import random, tools, arrows

class Arrow(object):
    def __init__(self, status=None, name='default'):
        self.status = status
        self.name = name
        
        self.record(True)
    
    
    def record(self, stamp=False):
        if not self.name:
            print "ERROR: cannot record into file, name is invalid."
            return 0
        
        file = open(self.name + '.mysa', 'a')
        
        if stamp:
            file.write(datetime.now().strftime('%b %d, %Y %H:%M:%S.%f') + '\n')
        else:
            file.write(self.status + '\n')
        
        file.close()
    
    def display(self):
        if self.status:
            tools.clear()
            
            if self.status == 'left':
                print arrows.left()
            elif self.status == 'right':
                print arrows.right()
    
    
    def switch(self):
        if random.randint(0, 1) == 1:
            self.status = 'left'
        else:
            self.status = 'right'
        
        self.display()
        self.record()