x=input("enter number:")
#splits the string at spaces and creates a list of strings:
#list comprehension converts each string to an integer:["50", "60", "70"] → [50, 60, 70]
numbers=[int(i) for i in x.split()]
count=0
for i in numbers:
    if i>40:
        count+=1
if count==len(numbers):
    print("pass")
else:
    print("fail")