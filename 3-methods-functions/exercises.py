# 1.- LESSER OF TWO EVENS: 
# Write a function that returns the lesser of two given numbers if both numbers are even, 
# but returns the greater if one or both numbers are odd
def lesser_of_two_evens(a,b):
    if(a % 2 != 0 or b % 2 != 0):
        return a if a > b else b 
    return b if a > b else a

# Check
print('Question 1:')
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))
print('----------')

# 2.- ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(s):
    splitted = s.split(' ')
    
    return splitted[0][0] == splitted[1][0]

# Check
print('Question 2:')
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))
print('----------')

# 3.- MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(a,b):
    if(a == 20 or b == 20):
        return True
    
    return a + b == 20
# Check
print('Question 3:')
print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))
print('----------')

# 4.- OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# Note: It was not specificed what happens if the string is less than four characters long
def old_macdonald(s):
    new = ''
    
    for i,c in enumerate(s):
        if(i == 0 or i == 3):
           new +=  c.capitalize()
           continue
        new += c
        
    return new

# Check
print('Question 4:')
print(old_macdonald('adolfo'))
print(old_macdonald('macdonald'))
print('----------')

# 5.- MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(s):
    to_list = s.split(' ')
    to_list.reverse()
    
    return ' '.join(to_list)

# Check
print('Question 5:')
print(master_yoda('I am Home'))
print(master_yoda('We are Ready'))
print(master_yoda('message secret a is this'))
print('----------')

# 6.- ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10

# Check
print('Question 6:')
print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
print('----------')

# 7.- FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(l):
    for i,n in enumerate(l):
        next = i + 1
        if(next < len(l)):
            if(n == 3 and l[next] == 3):
                return True
    return False

# Check
print('Question 7:')
print(has_33([1,3,3]))
print(has_33([1,3,1,3]))
print(has_33([3,1,3]))
print('----------')

# 8.- PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(s):
    new = ''
    for c in s:
        new += c * 3
    return new

# Check
print('Question 8:')
print(paper_doll('Hello'))
print('----------')

# 9.- BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(a,b,c):
    sum = a + b + c
    if((a == 11 or b == 11 or c == 11) and sum > 21):
        sum -= 10
    if(sum > 21):
        return 'BUST'
    return sum

# Check
print('Question 9:')
print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))
print('----------')

# 10.- SUMMER OF '69: Return the sum of the numbers in the array
# Except ignore sections of numbers starting with a 6 and extending to the next 9 
# (every 6 will be followed by at least one 9). 
# Return 0 for no numbers.
def summer_69(l):
    exclude = []
    diff = []
    for index,elem in enumerate(l):
        if(elem == 6):
            for inner_e in l[index:]:
                exclude.append(inner_e)
                if(inner_e == 9):
                    break
    diff = [i for i in l + exclude if i not in l or i not in exclude]
    return sum(diff)
    
# Check
print('Question 10:')
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2,1,6,9,11]))
print('----------')