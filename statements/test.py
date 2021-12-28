# 1.- Use for, .split(), and if to create a Statement that will print out words that start with 's':
st1 = 'Print only the words that start with s in this sentence'

for i in st1.split(' '):
    if('s' in i):
        print(i)
        
# 2.- Use range() to print all the even numbers from 0 to 10.
for n in range(0,11):
    if(n % 2 == 0):
        print(n)
        
# 3.- Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
modulo_3 = [n for n in range(1,50) if n % 3 == 0]

# 4.- Go through the string below and if the length of a word is even print "even!"
st2 = 'Print every word in this sentence that has an even number of letters'

for i in st2.split(' '):
    if(len(i) % 2 == 0):
        print(i)
        
# 5.- Write a program that prints the integers from 1 to 100. 
#     But for multiples of three print "Fizz" instead of the number 
#     And for the multiples of five print "Buzz". 
#     For numbers which are multiples of both three and five print "FizzBuzz".
for n in range(1,101):
    if(n % 3 == 0 and n % 5 == 0):
        print("FizzBuzz")
        continue
    if(n % 3 == 0):
        print("Fizz")
        continue
    if(n % 5 == 0):
        print("Buzz")
        continue
    print(n)
    
# 6.- Use List Comprehension to create a list of the first letters of every word in the string below:
st3 = 'Create a list of the first letters of every word in this string'

first_letter_word = [i[0] for i in st3.split(' ')]
