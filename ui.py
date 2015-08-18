class Box(object):
    
    def _sides(self, c=False):
        column = '+'
        lining = '-'
        
        if c:
            column = '|'
            lining = ' '
        
        return column + ' ' + lining * (self.x-4) + ' '  + column + '\n'
    
    
    def _frame(self):
        self.result += self._sides()
        
        body = self._sides(True)
        self.result += body * (self.y-2)
        
        self.result += self._sides()
    
    
    def __init__(self, x=5, y=5):
        self.x = x
        self.y = y
        self.result = ""
        
        self._frame()
        

class Controller(object):
    
    def __init__(self, player):
        self.player = player
    
    
    def _fill(self, space, lines=1):
        result = ""
        line = " " * space
        
        if lines:
            for i in xrange(lines):
                result += line + '\n'
        
        return result
    
    
    def _border(self, space, c=False, end=False):
        result = ''
        column = ' + '
        lining = '-'
        
        if c:
            column = ' | '
            lining = ' '
        
        if space > 2:
            result = column + lining * (space-2)
        else:
            result = 'Error, invalid border space argument supplied, minimum req. is 3'
        
        if end:
            result += column + '\n'
        
        return result
    
    
    def _frame(self, space1=13, space2=72, height=5):
        space = space1 + space2 + 5
        
        result = self._fill(space, 4)
        result += self._border(space1) + self._border(space2, end=True)
        body = self._border(space1, c=True) + self._border(space2, c=True, end=True)
        
        # This is about where I realized that I was trying to make a text GUI...
        # AND this couldn't end well.
        result += body * height
        result += self._border(space1) + self._border(space2, end=True)
        result += self._fill(space)
        
        return result
    
    
    def base(self):
        pass
    
test = Controller(1)
print test._frame(13, 72)