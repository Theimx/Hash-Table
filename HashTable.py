
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
    return(int(index))

#a function to create an array, to organize and stock the Hash Table 
def table(b):
    size = b * 2
    
#a function to place a word in the Table in the right place 
def placing(a):
    hash(a)
    place(a)

#a function to search a word in the table and return the content
def read(a):
    a = a 
