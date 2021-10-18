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



