string = 'Hello World'

#Indexing
print(string[0])    # H
print(string[-2])   # l

#Slicing
print(string[2:])   # llo World
print(string[:3])   # Hel (Up to index 3, it does not include the index 3)
print(string[3:6])  # lo 
print(string[1:3])  # el 
print(string[::])   # Hello World
print(string[::2])  # HloWrd
print(string[::-1]) # dlroW olleH (Reverses the string)