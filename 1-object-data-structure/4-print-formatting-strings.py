# Using .format
print('This is a String {}'.format('INSERTED')) # This is a String INSERTED

print('The {2} {1} {0}'.format('fox','brown','quick')) # The quick brown fox

print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick')) # The quick brown fox

# Float formatting
result = 100/777 # 0.1287001287001287

print("The result was {:1.3f}".format(result))

# Using string literals
name = "Jose"
age = 3
print(f'Hello, his name is {name}.\nHe is {age} years old.')

print(f'The result was {result:1.3f}')