integer_list = [1,2,3]

mixed_list = ['String',100,23.2]

len(mixed_list) # returns list length (3)

mixed_list[0] # 'String'

mixed_list[1:] # [100,23.2]

new_list = integer_list + mixed_list # [1,2,3,'String',100,23.2]

new_list[0] = 4 # [4,2,3,'String',100,23.2]

new_list.append('Adolfo') # Adds new item to list -> [4,2,3,'String',100,23.2,'Adolfo']

new_list.pop() # Removes last item in list and RETURNS IT -> [4,2,3,'String',100,23.2]

popped_item = new_list.pop() # new_list = [4,2,3,'String',100] popped_item = 23.2

new_list.pop(0) # Removes item at given index [2,3,'String',100]

letters = ['a','e','x','b','c']
numbers = [4,1,8,3]

# Sort happens IN PLACE, it does not return anything
letters.sort()
numbers.sort()

print(letters)
print(numbers)

# Reverse happens IN PLACE, it does not return anything
letters.reverse()
numbers.reverse()

print(letters)
print(numbers)