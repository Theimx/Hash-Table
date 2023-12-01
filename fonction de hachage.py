
def hash(a):
    lenght = len(a)
    counter = 0
    hashing = []
    value = []
    index = 0
    for i in range(lenght):
        hashing.append(a[counter])
        counter += 1
    counter = 0
    for n in range(lenght):
        value.append(ord(hashing[counter]))
        counter += 1
    counter = 0
    index = sum(value) / lenght
    print("liste de char : ",hashing)
    print("valeur associer :",value)
    print("index du mot :",index)
    return(index)

a = hash(input("entrez le mot a hasher :"))
print(a)

