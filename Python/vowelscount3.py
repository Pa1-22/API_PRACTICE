# Write a Python script to count how many vowels are present in a given string without using built-in count functions.

'''vowels=input()
count=0
characters=[]

for ch in vowels:
    
       if ch.lower() in ['a','e','i','o','u']:
        
         count += 1
         characters.append(ch)
print(count) 
print(characters) '''

# using function

def vowelsCount():
    vowels=input()
    count=0
    characters=[]

    for ch in vowels:
      # checking ch is present in given list
       if ch.lower() in ['a','e','i','o','u']:
        count += 1
        characters.append(ch)
    print(count) 
    print(characters)
vowelsCount()

