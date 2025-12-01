'''g = open("symbols.txt", "r")
f = open("sample.txt", "w")

g1 = g.read()
p = g1.split('\n')

for line in p:
    if not line.lstrip().startswith("#"):
        f.write(line + '\n')   # Add newline back

g.close()
f.close()

k=open("sample.txt","r")
print("Copied successfully (excluding lines starting with #) ")
print(k.read())
k.close()'''


#program to read the lines contains python

f = open("sample.txt", "r")
g = f.readlines()  # reads all lines as a list
f.close()

for line in g:
    if "python" in line:
        print(line.strip())  # .strip() removes extra spaces/newlines
