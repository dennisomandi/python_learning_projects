#with open('sample1.txt'

fname = input('The file name: ')
try :
    fhand = open(fname)
except :
    print("This file cannot be opened")
    quit()
    
for line in fhand :
    line = line.rstrip()
    if line.startswith('Ex ') :
        print(line)
