'''
toys.py

Simple toy functions to get comfortable working 
with functions.
'''


# write a function that adds 1
# to the input and prints the result
print('Excersise 1; A function that add 1 and prints the answer.')
def inc_return(a):
    a = a + 1
    print(a)
    return(a)
print('Please input a value')
A = input()
A = int(A)
print('Answer:')
inc_return(A)
print('end')

# write a function that adds
# the two input numbers together
# and returns the sum
print('Excersise 2; A function that adds two numbers and prints the answer.')
def sum(a, b):
    c = a + b
    print(c)
    return(c)
print('Please input two values')
B = input()
C = input()
B = int(B)
C = int(C)
print('Answer:')
sum(B, C)
print('end')


# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return
print('Excersise 3; A function that adds two numbers and increments them.')
def sum_inc(a, b):
    c = sum(a, b)
    inc_return(c)
    return(c)
print('Please input two values')
E = input()
F = input()
E = int(E)
F = int(F)
print('Answer:')
sum_inc(E, F)
print('end')

# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even
print('Excersise 4; A function that checks if the value is even.')
def is_even(a):
    b = ( a % 2 ) == 0
    print(b)   
    return(b)
print('Please input a value')
G = input()
G = int(G)
print('Answer:')
is_even(G)
print('end')


# create for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'
print('Excersise 5; A function that repeats a string a given number of times.')
def string_repeat(a, b):
    x = 0
    while x < b:
        print(a)
        x = x + 1
        continue
    return
print('Please input a string then a value')
H = input()
I = input()
I = int(I)
print('Answer:')
string_repeat(H, I)
print('end')
