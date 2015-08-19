import tools, sail

class Controller(object):
    
    def _fill(self, space, lines=1):
        result = ""
        line = " " * space
        
        for i in xrange(lines):
            result += line + '\n'
            
        if not lines:
            result += line
        
        return result
    
    
    def _border(self, space, c=False, start=True, end=False):
        result = ''
        column = ' + '
        lining = '-'
        
        if c:
            column = ' | '
            lining = ''
        
        if start:
            result = self.padding
        
        result += column + lining * (space-2)
        
        if end:
            result += column + self.padding + '\n'
        
        return result
    
    
    def _frame(self):
        space = self.box1 + self.box2 + 3 + (len(self.padding)*2)
        
        border = self._border(self.box1) + self._border(self.box2, start=False, end=True)
        body = self._border(self.box1, c=True) + self._border(self.box2, c=True, start=False, end=True)
        
        # This is about where I realized that I was trying to make a text GUI...
        # AND this couldn't end well.
        result = border
        result += body * self.height
        result += border
        result += tools.clear(1, True)
        
        self.frame = result
    
    
    def _base(self):
        self._frame()
    
        pos = 3
        pos2 = 4
        
        space = self.box1 + len(self.padding) + 4
        self.frame = self._fill(space, 0) + '%(pos1)s - %(pos2)s\n' + self.frame
        
        while True:
            newthing = '| %(pos' + str(pos) + ')s | %(pos' + str(pos2) + ')s |'
            thing = self.frame.find('|  |  |')
            
            if thing == -1:
                break
            
            self.frame = self.frame.replace('|  |  |', newthing, 1)
            pos += 2
            pos2 += 2
            
            
    def display(self, text):
        tools.clear()
        
        print self.frame % self.content
    
    
    def __init__(self, player, box1=13, box2=72, height=5, padding=1):
        self.player = player
        self.box1 = box1
        self.box2 = box2
        self.height = height
        self.padding = ' ' * padding
        self.frame = ""
        self.content = {'pos1': 'Day '+str(self.player.day), 'pos2': self.player.place,
            'pos3': 'Health: ' + str(self.player.hp)}
        
        self._base()

