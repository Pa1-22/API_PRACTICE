n=int(input())

#If a number is divisible by both 3 and 5, it is obviously divisible by 15, because 15 is the least common multiple of 3 and 5
if n%15==0 and n%7!=0:
   print("divisible by both numbers 3 and 5")
else:
   print("not divisible by both the numbers")