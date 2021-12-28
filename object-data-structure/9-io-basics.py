with open('files\\io-basics.txt','r') as file: #read mode
    content = file.read()

    file.seek(0) 

    lines = file.readlines()

    print(lines)

with open('files\\io-basics.txt','a') as file: #append mode
	file.write('\nFourth line')

with open('files\\io-basics-2.txt','w') as file: #write mode
    file.write('This file was generated from script')