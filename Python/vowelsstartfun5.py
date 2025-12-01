
def printVowel(names):
   
   modifiedlist=[]

   for i in names:
        
        #using lower() method to change the name to lower letters

        #in is using to check whether letter is present in given list or not
        if i[0].lower() in ['a','e','i','o','u']:
            modifiedlist.append(i)
   return modifiedlist



def vowelsPrint():
#using string take the input from the user
   actuallist=input("Enter names:")

#using split function separate names in string
   names=actuallist.split()

   vowel=printVowel(names)
   print(vowel)
vowelsPrint()