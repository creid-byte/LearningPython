def greet(name):
    if name == "Claire":
        return 'Welcome back'
    return "hello, " + name + '! Welcome to my app'


print(greet('Chris'))
print('\n')
print(greet('Claire'))
print('\n')

def good_morning(name='User', morning_person= True):
    if not morning_person:
        return 'Maybe have some coffee before talking to me'
    return 'It is a pleasure to see you, ' + name

print(good_morning("Chris", False))

print('\n')

def print_info(name, age, email):
        print(name + ' is ' + str(age) + '. Reached at ' + email)

print_info('chris', 13, 'chris@gmail')

print('\n')

list = [['chris', 13, 'chris@gmail'],
        ['pixie', 8, 'pixie@gmail']]

for l in list:
    print_info(*l)