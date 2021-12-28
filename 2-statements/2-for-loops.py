my_list = [1,2,3,4,5,6,7,8,9,10]

for n in my_list:
    print(n)
    
# print even numbers
for n in my_list:
    if(n % 2 == 0):
        print(f'Even: {n}')
        
list_sum = 0

for n in my_list:
    list_sum += n

print(f'Sum of list: {list_sum}')

# tuple unpacking

tup_list = [(1,2),(3,4),(5,6),(7,8)]

for a,b in tup_list:
    print(a) # first element of each tuple
    print(b) # second element of each tuple
    
# dict unpacking

dct = {'k1':1,'k2':2,'k3':3}

for key,val in dct.items():
    print(key,' -> ',val)