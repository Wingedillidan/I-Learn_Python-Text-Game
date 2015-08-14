def clear(lines=50):
    for i in xrange(lines / 2):
        print "\n\n"
    if lines % 2 > 0:
        print "\n"

    
def answer(prompt):
    while True:
        response = raw_input(prompt).lower().strip()
        
        if not response:
            print "Please enter something, anything! D:"
        
        return response


def next(lines=2, prompt='PRESS ENTER TO CONTINUE'):
    clear(lines)
    raw_input(prompt)