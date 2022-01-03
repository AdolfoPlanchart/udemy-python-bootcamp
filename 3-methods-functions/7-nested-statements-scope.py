name = 'Global String'

def greet():
    name = 'Adolfo'
    
    def hello():
        print('Hello ' + name)
        
    hello()
    
greet()
        
x = 50

def func(x):
    # global x 
    print(f'X is: {x}')
    # LOCAL Reassignment on GLOBAL variable
    x = 200
    return x
    
# func()
x = func(x)