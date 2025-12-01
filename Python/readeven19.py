f=open("file.txt","r")
k=f.read()
j=k.split()
f.close()
sum=0
for even in j:
    if int(even) %2==0:
        sum = sum+int(even)
        
print(sum)