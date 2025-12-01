
s=input()
rev=""
for i in s[::-1]:
  rev += i
if rev==s:
  print("palindrome")
else:
  print("not palindrome")