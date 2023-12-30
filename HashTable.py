#The Hashing function 
def hashing(a):
    counter = 0
    hashing = []
    value = []
    index = 0
    for i in range(len(a)):
        hashing.append(a[counter])
        counter += 1
    counter = 0
    for n in range(len(a)):
        value.append(ord(hashing[counter]))
        counter += 1
    counter = 0
    index = sum(value) / len(a)
    #return an Integer type, not a Float
    return(int(index))

#a function to create an array, to organize and stock the Hash Table 
def table(a):
    size = a 
    
