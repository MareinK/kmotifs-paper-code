# some colors used for terminal output in early script

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

short = {'r': RED,
         'b': BLUE,
         'c': CYAN,
         'g': GREEN}

p = lambda c,s: short[c] + s + RESET

r = lambda s: p('r',s)
b = lambda s: p('b',s)
c = lambda s: p('c',s)
g = lambda s: p('g',s)

