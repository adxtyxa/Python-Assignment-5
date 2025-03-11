stu_mark = {'Alice':50, 'Bob':60, 'Jack':10}

Name = input("Enter the student's name:")

if Name in stu_mark:
    print(f"{Name}'s marks: {stu_mark[Name]}")
else:
    print("Student not found")