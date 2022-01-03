def percent_of_two(a,b):
    return sum((a,b)) * 0.05

def percent_of_args(*args):
    return sum(args) * 0.05

def fruits(**kwargs):
    if 'fruit' in kwargs:
        print('Fruit: {}'.format(kwargs['fruit']))
    else:
        print('No fruit here')
        
fruits(fruit = 'apple', veggie = 'lettuce')

def combined(*args,**kwargs):
    print('I\'d like {} {}'.format(args[0],kwargs['food']))

combined(10,20,30,40,food = 'eggs')