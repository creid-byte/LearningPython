print('do you want to continue? Y/N')
response = input()

while response=='Y':
    print('do you want to continue? Y/N')
    response = input()

while True:
    print('Q to quit. Continuing....')
    response = input()
    if response == 'Q':
        break

# indefinite loop and characters
while True:
    print('Continue? Y/N')
    response = input()
    if response != 'Y' and response != 'y':
        break