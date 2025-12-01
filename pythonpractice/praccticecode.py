a=list(map(int,input().split()))
z=list(set(a))
b=1
c=1
for i in z:
    if i%2==0:
        b=b*i
    else:
      c=c*i
print(abs(b-c))