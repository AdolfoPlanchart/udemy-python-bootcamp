from random import shuffle, randint

for n in range(0,11,2):
    print(n)

print(list(range(0,11,2)))

word = 'adolfo'

for index,char in enumerate(word):
    print(index,'->',char)
    
list_1 = [1,2,3]
list_2 = ['a','b','c']
list_3 = [0.1,0.2,0.3]

for item in zip(list_1,list_2,list_3):
    print(item)
    
print(list(zip(list_1,list_2,list_3)))

nums = [10,20,30,40,100]

print(min(nums))

print(max(nums))

shuffle_list = [1,2,3,4,5,6,7,8,9,10]

shuffle(shuffle_list)

print(shuffle_list)

print(randint(0,100))

res = input('What\'s your name? ')

print(f'Hello, {res}')