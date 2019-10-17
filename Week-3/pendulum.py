#A program that simulates the pendulum equation

import math

def period(a, b):
    x = isinstance(a, str)
    y = isinstance(b, str)
    if x == False:
        if y == False:
            if a < 0:
                raise(ValueError)
            else:
                if b <= 0:
                    raise(ValueError)
                else:
                    c = 2 * math.pi * math.sqrt( a / b )
                    return(c)
        else:
            raise(TypeError)
    else:
        raise(TypeError)

