'''n=int(input("enter the number: "))
temp=n
rev=0
while n>0:
    last=n%10
    rev=rev*10+last
    n=n//10
if temp==rev:
    print("palindrome")
else:

    print("not a palindrome")'''

def checkPalindrome(n):

   temp=n
   rev=0
   while n>0:
      last=n%10
      rev=rev*10+last
      n=n//10
   if temp==rev:
     return "palindrome"
   else:

     return "not a palondrome"

def palindrome():
    n=int(input())
    res=checkPalindrome(n)
    print(res)
palindrome()