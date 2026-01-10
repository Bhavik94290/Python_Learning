#List is muttable in Python But String Is  Imutable in Python  

student = ["bhavik", 95.4,22,"surat"]
print(student)

student[0] = "Jigar"
print(student)

marks = [99,98,97,96,95,94]
print(marks[1:4])
print(marks[-1:-4])

list = [6,8,9,7,3,5,2,4,1]
list.append(10)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
list.insert(1, 693)
print(list)