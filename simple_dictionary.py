count =  dict()
names = ['den', 'oma', 'nis', 'ndi', 'nis', 'den', 'den', 'oma']
for name in names :
    if name not in count :
        count[name] = 1
    else :
        count[name] = count[name] + 1
print(count)

counts = dict()
line = input('Enter the text:' )
words = line.split()

print('words:', words)
print('counting...')
for word in words :
    counts[word] = counts.get(word, 0) + 1
print('counts:', counts)