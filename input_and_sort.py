fhand = input('Enter text:', )
counts = dict()
for line in fhand :
    words = line.split()
    counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items() :
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10] :
    print(key, val) 
