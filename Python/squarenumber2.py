#Using a for loop, generate a list of squares of only the odd numbers from 1 to 20.


'''start=int(input("Enter starting number:"))
end=int(input("Enter ending number:"))
#create a list to store the squares of number
list=[]

for i in range(start,end+1):
   
   if i%2==1:
      list.append(i*i)

print(list)'''

#Use function, generate a list of squares of only the odd numbers from 1 to 20.
#math is a module having methods before using it import it and use it

import math
def squareNumbers():
    
   start=int(input("Enter starting number:"))
   end=int(input("Enter ending number:"))
#create a list to store the squares of number
   squares=[]
   squarevalues=[]

   for i in range(start,end+1):
   
     if i%2==1:
        squares.append(i**2)
        #sqrt is a function if we use it we will get the number for sqrt eg.64 o/p 8
        squarevalues.append(int(math.sqrt(i*i)))

   print(squares)
         
   print(squarevalues)
squareNumbers()
