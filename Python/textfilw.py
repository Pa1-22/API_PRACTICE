# open the file in read mode
f=open('textfile.txt','r')
ch="python"

# Here, 'line' is an iterative variable that represents each line in the file as one string.
# Each line automatically includes the newline character '\n' at the end.
for line in f:
    #lower is a built in function which can makes the string ass lower case
    if ch in line.lower():
        #strip a built in functgion in string which can remove whitespace from the beginning or the end:
        print(line.strip())
f.close()