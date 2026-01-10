#WAP to ask the user to enter names of their 3 favorite movies & store them in a list

movies =[]
name1 = str(input("Enter the first Fav Movie name :"))
name2 = str(input("Enter the second Fav Movie name :"))
name3 = str(input("Enter the third Fav Movie name :"))

movies.append(name1)
movies.append(name2)
movies.append(name3)

print(movies)