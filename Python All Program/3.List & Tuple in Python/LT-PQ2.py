#WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

list = ["m","a","a","m"]

copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("list is palindrome ")
else:
    print(" list is not a palindrome")