def clear(lines=50):
    print "\n"*lines

    
def answer(prompt):
    while True:
        response = raw_input(prompt).lower().strip()
        
        if not response:
            print "Please enter something, anything! D:"
        
        return response


def next(prompt='PRESS ENTER TO CONTINUE'):
    clear(2)
    raw_input(prompt)