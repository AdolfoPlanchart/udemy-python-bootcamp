name = "Sam"

#name[0] = 'P' TypeError: 'str' object does not support item assignment

changed_name = 'P' + name[1:]

x = 'Hello World'

x = x + '! It is beautiful outside.' # Hello World! It is beautiful outside.

letter = 'z'

letter = letter * 10 # zzzzzzzzzz

x = 'Hello World'

print(x.upper()) # Returns string in uppercase

print(x.lower()) # Returns string in lowercase

print(x.split()) # Returns a list of the string ['Hello','World']

print(x.split('o')) # Splits the string by the character ['Hell', ' W', 'rld'] 