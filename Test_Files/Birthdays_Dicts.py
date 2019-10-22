'''
A program for remebering birthdays
'''

A = 0
BIRTHDAYS = {}
while A == 0:
    print('Would you like to add a birthday, retreive one or quit? a/r/q')
    C = input()
    if C == 'a':
        print('Please tell me their name:')
        NAME = input()
        print('please tell me thier birthday:')
        BDAY = input()
        BIRTHDAYS[NAME] = BDAY
        print('Birthdays database updated')
    if C == 'r':
        print('Please tell me their name:')
        NAME = input()
        if NAME in BIRTHDAYS:
            print(NAME + '\'s birthday is:')
            print(BIRTHDAYS[NAME])
        else:
            print('I don\'t know this birthday')
            continue
    if C == 'q':
        exit()
    else:
        continue
    