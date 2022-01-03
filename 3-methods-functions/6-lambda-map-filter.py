# Map function
def square(n):
    return n ** 2

nums = [1,2,3,4,5]

for item in map(square,nums):
    print(item)
    
def splicer(s):
    if(len(s) % 2 == 0):
        return 'EVEN'
    return s[0]

names = [
    'Adolfo',
    'Nathalia',
    'Isabella'
]

print(list(map(splicer,names)))

# Filter function
def check_even(n):
    return n % 2 == 0

nums = [1,2,3,4,5,6]

print(list(filter(check_even,nums)))

# Lambda expresions
# square() as lambda
print(list(map(lambda n: n ** 2,nums)))

# check_even() as lambda
print(list(filter(lambda n: n % 2 == 0,nums)))

# Reverse string 
print(list(map(lambda name: name[::-1],names)))