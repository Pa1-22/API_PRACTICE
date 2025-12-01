'''n = int(input("Enter a number: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print("Prime")
else:
    print("Not a prime")'''

#using function

'''def isPrime():
    
    n = int(input("Enter a number: "))
    count = 0
# range starting from 1 to length-1
    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1

    if count == 2:
        print("Prime")
    else:
        print("Not a prime")

isPrime()'''

#check the prime numbers between 2 numbers
'''
start=int(input())
end=int(input())
list=[]
for start in range(2,end+1):
     count=0
     for i in range(1,start+1):
          if start%i==0:
               count += 1
     if count==2:
      list.append(i)
print(list)    
'''

# write the program to print the prime numbers between 2 numbers using function
def isPrime():
    start=int(input())
    end=int(input())

    #create a list to store the numbers
    list=[]
    for start in range(2,end+1):
        count=0
        # this range check from 1 to given number
        for i in range(1,start+1):
          if start%i==0:
               count += 1
        if count==2:
          list.append(i)
    print(list)
isPrime()
