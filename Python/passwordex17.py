password1=input("Enter the password:")

choice=0

while choice <3:
    password=input("Enter the password:")
    if password == password1:
          print(password)
          break
    else:
        choice += 1
        print("failed try again")
if choice == 3:
     print("exceeded 3 failed attempt")