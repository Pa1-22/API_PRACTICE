'''f=open('textfile.txt','r')
g=f.readlines()
list2=[]
list3=[]
for i in g:
    words=i.split()
    list2.extend(words)
for j in list2:
    for k in j:
        list3.append(k)
    
print(g)
print(list2)
print(len(g))
print(len(list2))
print(len(list3))'''

f=open('textfile.txt', 'r')
text=f.read()

# Count lines
lines = text.split('\n')

# Count words
words =  text.split()

# Count characters
characters = len(text)

print("Number of lines:", len(lines))
print("Number of words:", len(words))
print("Number of characters:", characters)


