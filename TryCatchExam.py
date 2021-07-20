def zeroError(num):
    try:
        return 100/num
    except ZeroDivisionError:
        print('Number divided by zero')

def valueError():
    print('How many cats do you have?')
    try:
        num = input()
        if int(num) > 5:
            print('There are lots of cats')
        else:
            print('There are very less cats')
    except ValueError:
        print('invalid value')

    


print(zeroError(1))
print(zeroError(0))
valueError()
