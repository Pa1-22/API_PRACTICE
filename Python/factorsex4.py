#take the input from the user

'''n=int(input("Enter a number: "))
factors=[]
for i in range(1,n+1):
    if n%i==0:
        factors.append(i)
print(factors)'''

# write a program using to find common factors betwwn 2 numbers


'''n=int(input("Enter a number: "))
m=int(input("Enter a number"))
factors=[]
#using min function between 2 numbers give min number
for i in range(1, min(n, m)+1):
        if n%i==0 and m%i==0:
          factors.append(i)
print(factors)'''

#using function

def _is_a_factor(n, m):
    factors = []
    # using min() to iterate till smaller number
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            factors.append(i)
    return factors


def find_factors():
    n = int(input("Enter first number: "))
    m = int(input("Enter second number: "))
    result = _is_a_factor(n, m)
    print(result)

# calling main function
find_factors()
