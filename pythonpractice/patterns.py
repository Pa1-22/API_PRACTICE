n=int(input())
"""for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end="  ")
    print()

output:
*  *  *  *  *  
*  *  *  *  *
*  *  *  *  *
*  *  *  *  *
*  *  *  *  *"""

"""for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(" ",end= " ")
    print()

output: 
* * * * * 
*       *
*       *
*       *
* * * * *"""

"""for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()

output:
1 1 1 1 1 
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5"""

"""for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()

output:

1 2 3 4 5 6 7 
1 2 3 4 5 6 7
1 2 3 4 5 6 7
1 2 3 4 5 6 7
1 2 3 4 5 6 7"""
"""n = 5
count = 1

for i in range(n):
    for j in range(n):
        if count < 10:
            print("0" + str(count), end=" ")
        else:
            print(count, end=" ")
        count += 1
    print()

output:

01 02 03 04 05 
06 07 08 09 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
"""

"""for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
output:
*
* *
* * *
* * * *
* * * * *"""
"""k=n-1
for i in range(1,n+1):
    for k in range(1,n+1):
        if k<=n-i:
            print(" ",end=" ")
    for j in range(1,n+1):
        if j<=i:
            print("*",end=" ")
    print()

output:
       * 
        * *
      * * *
    * * * * 
  * * * * *
* * * * * * """

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == n or j == 1 or i == j:
            print("*", end=" ")
        else:
            print("  ", end="  ")
    print()


