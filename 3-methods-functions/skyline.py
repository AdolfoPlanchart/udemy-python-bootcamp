def myfunc(s):
    new = ''
    for i,c in enumerate(s):
        if(i % 2 == 0):
            new += c.lower()
        else:
            new += c.upper()
    return new

print(myfunc('adolfo'))