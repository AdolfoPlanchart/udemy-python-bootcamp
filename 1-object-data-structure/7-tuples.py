tuple = (1,2,3)

list = [1,2,3]

len(tuple) # returns 3

tuple = ('one',2)

tuple[0] # returns one

tuple[-1] # returns 2

tuple.count('one') # returns 1

tuple.index('one') # returns 0 (index of 'one' element)

list[0] = 'NEW' # all good no errors

tuple[0] = 'NEW' # TypeError: 'tuple does not support item assignment'