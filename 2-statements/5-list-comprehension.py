# naive way
message = 'hello'

to_list = []

for i in message:
    to_list.append(i)

# with list comprehension
list1 = [i in i in message]

list2 = [n for n in range(0,11) if n % 2 == 0] # only even

list3 = [n ** 2 for n in range(0,11) if n % 2 == 0] # only powered even

celsius = [0,10,20,34.5]

fahrenheit = [((9 / 5) * temp + 32) for temp in celsius] # more complex arithmetics (c° to f°)

# nested for loop in list comprehension
list4 = [x * y for x in [2,4,6] for y in [1,10,100]]

print(list4)