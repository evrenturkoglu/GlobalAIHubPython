FirstName = input("Please enter your name: ")
LastName =  input("Please enter your surname: ")
Age= int( input("Please enter your age: "))
Date_Of_Birth = int( input("Please enter date of birthday as year[YYYY format]: "))

userList = [FirstName, LastName, Age, Date_Of_Birth]

i=0
lenList = len(userList)

while(i < lenList):
    print(userList[i])
    i += 1

if Age < 18:
    print("You can't go out because it's too dangerous")
elif Age > 18:
    print(You can go out to the street")

