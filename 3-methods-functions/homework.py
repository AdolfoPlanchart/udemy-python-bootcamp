import math
import string

# 1.- Write a function that computes the volume of a sphere given its radius.
def vol(rad):
    return (4 / 3) * (math.pi * (rad ** 3))

# Check
print('Question 1')
print(vol(2))
print('----------')

# 2.- Write a function that checks whether a number is in a given range (inclusive of high and low)
def range_check(num,low,high):
    return not (num > high or num < low)

# Check
print('Question 2')
print(range_check(5,2,7))
print('----------')

# 3.- Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(s):
    cleaned = ''.join(c for c in s if c.isalpha())
    
    highs = 0
    lows = 0
    
    for c in cleaned:
        if(c.isupper()):
            highs += 1
    
    lows = len(cleaned) - highs
    
    print(f'No. of Uppercase characters: {highs}\nNo. of Lowercase characters: {lows}')

# Check
print('Question 3')
up_low('Hello Mr. Rogers, how are you this fine Tuesday?')
print('----------')

# 4.- Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(l):
    return list(set(l))

# Check
print('Question 3')
print(unique_list([1,1,1,2,2,2,3,3,3,4,4,4]))
print('----------')

# 5.- Write a Python function to multiply all the numbers in a list.
def multiply(l):
    multiplied = 1
    
    for elem in l:
        multiplied *= elem
        
    return multiplied

# Check
print('Question 4')
print(multiply([1,2,3,-4]))
print('----------')

# 6.- Write a Python function that checks whether a word or phrase is palindrome or not.
def palindrome(s):
    s = s.replace(' ','')
    back = s[::-1]
    return s.lower() == back.lower()

# Check
print('Question 5')
print(palindrome('Anita lava la tina'))
print('----------')

# 7.- Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
def pangram(s, alphabet = string.ascii_lowercase):
    cleaned = [c.lower() for c in s if c.isalpha()]
    
    unique = unique_list(cleaned)
    unique.sort()
    unique = ''.join(unique)
    
    return unique == alphabet

print('Question 6')
print(pangram('The quick brown fox jumps over the lazy dog'))
print(pangram('Sphinx of black quartz, judge my vow.'))
print(pangram('The five boxing wizards jump quickly.'))
print(pangram('ADOLFO ANTONIO'))
print('----------')