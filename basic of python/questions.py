#Write a python program that takes in a student name, class, and section. It should also take in five subject marks of the students and find the total mark and percentage. Display a result in such a way that their name, class, section, and percentage are printed.


student_name = input("enter student name : ")
student_class = input("enter student class : ")
student_section = input("enter student section : ")


science = int(input("science marks = "))
maths = int(input("maths marks = "))
socialstudy = int(input("socialstudy_marks = "))
english = int(input("english marks = "))
punjabi = int(input("punjabi marks ="))

percentage = (science + maths + socialstudy + punjabi + english)/500*100
print(student_name,end="-> ")
print(student_class,end="-> ")
print(student_section,end="-> ")
print(percentage,end="-> ")