x = 0

while x < 5:
    print(f'X = {x}')
    
    x += 1
else:
    print('X is no less than 5')
    
while x < 5:
    if(x == 2):
        break # breaks out of loop
    
    print(x)
    
    x += 1
    
for i in [1,2,3,4]:
    pass # placeholder

for c in 'Adolfo':
    if(c == 'o'):
        continue # stops flow and goes back to loop start
    
    print(c)