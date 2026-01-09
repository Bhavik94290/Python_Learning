#WAP to find the greatest of 3 numbers entered by the user.

num1 = int(input("Enter the Number 1: "))
num2 = int(input("Enter the Number 2: "))
num3 = int(input("Enter the Number 3: "))

if(num1 >= num2 and num1 >= num3):
    print("Number 1 is Greatest")
elif(num2 >= num3):
    print("Number 2 is Greatest")
else:
    print("Number 3 is Greatest")