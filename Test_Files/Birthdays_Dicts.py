#A program for remebering birthdays

a = 0
birthdays = {}
while a == 0:
    print('Would you like to add a birthday, retreive one or quit? a/r/q')
    c = input()
    if c == 'a':
        print('Please tell me their name:')
        name = input()
        print('please tell me thier birthday:')
        bday = input()
        birthdays[name] = bday
        print('Birthdays database updated')
    if c == 'r':
        print('Please tell me their name:')
        name = input()
        if name in birthdays:
            print(name + '\'s birthday is:')
            print(birthdays[name])
        else:
            print('I don\'t know this birthday')
            continue
    if c == 'q':
        exit()
    else:
        continue
    