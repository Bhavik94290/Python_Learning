#Grade students based on marks

marks = (int(input("Enter the marks out pf 100 :")))
print("Your marks is : " , marks)

if(marks >= 90):
    print("Your Grade is : A")
elif(90 > marks >= 80):
    print("Your Grade is : B")
elif(80 > marks >= 60):
    print("Your Grade is : C")
elif(60 > marks >= 55):
    print("Your Grade is : D")
elif(55 > marks >= 33):
    print("Your Grade is : E")
else:
    print("You are Failed ")

print("your Grade based on Marks")