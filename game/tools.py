def clear(lines=50, r=False):
    result = ''
    
    for i in xrange((lines-1) / 2):
        result += "\n\n"
    
    if lines <= 0:
        result = ''
    elif lines % 2 == 0:
        result += "\n"
    
    if r:
        return result
    
    print result

    
def answer(prompt):
    while True:
        response = raw_input(prompt).lower().strip()
        
        if not response:
            print "Please enter something, anything! D:"
        
        return response


def bar(lines=32):
    return '|' * lines

def next(lines=1, prompt='PRESS ENTER TO CONTINUE'):
    clear(lines)
    raw_input(prompt)