#Type_Conversion
a=2
b=4.5

print(a+b) #ans Should 6.5

#Type_Casting :
c=int("2")
d=5.5
print(c+d)
print(type(a))

#How To Get Input From The User
val = input("Enter the Value :")
print(type(val) , val)


name = input("enter name: ")
age = int(input("enter age: "))
marks = float(input("enter marks: "))

print("welcome", name)
print("age =", age)
print("marks =", marks)


#Area Of Sq

side = float(input("enter the val of side : "))

print("Area =" ,side ** 2) #16.0

#a>=b

a = int(input("Enter the first value of a :"))
b = int(input("Enter the Second value of b :"))

print(a>=b) #True