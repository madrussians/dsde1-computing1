# Fizz Buzz
X = 1
while X < 100:
    if X % 3 == 0:
        if X % 5 == 0:
            print('Fizz-Buzz')
        else:
            print('Fizz')
    else:
        if X % 5 == 0:
            print('Buzz')
        else:
            print(X)
    X +=1
            