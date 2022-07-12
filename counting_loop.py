count = 0
x = [9, 7, 12, 45, 3, 17]
print('Before', count)
for thing in x:
    count = count + 1
    print(thing)
print('after', count)
zork = 0
print('Before', zork)
for thing in x :
    zork = zork  + thing 
    print(zork, thing)
print('After', zork)
    
avg = zork / count
print(avg)