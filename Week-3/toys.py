'''
toys.py

Simple toy functions to get comfortable working 
with functions.
'''

# write a function that adds 1
# to the input and prints the result
def inc_return(a):
    a = a + 1
    print(a)
    return(a)

# write a function that adds
# the two input numbers together
# and returns the sum

def sum(a, b):
    c = a + b
    print(c)
    return(c)

# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return

def sum_inc(a, b):
    c = sum(a, b)
    inc_return(c)
    return(c)

# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even

def is_even(a):
    b = ( a % 2 ) == 0
    print(b)   
    return(b)

# create for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'

def string_repeat(a, b):
    print(a*b)
    