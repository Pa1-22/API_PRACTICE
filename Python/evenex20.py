choice = "start"
f = open("file.txt", "w")

# Take numbers until user types "stop"
while choice != "stop":
    n = input("Enter a number: ")
    f.write(n + "\n")
    choice = input("Type 'stop' to end or press Enter to continue: ")

f.close()

# Read numbers from file
f = open("file.txt", "r")
numbers = f.read().split()
f.close()

even_count = 0
odd_count = 0

# Count even and odd numbers
for i in numbers:
    if int(i) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
