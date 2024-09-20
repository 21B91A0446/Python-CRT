'''
Python program to print rank using marks
'''
marks = int(input("Enter any marks: "))

if marks <= 100:
    if marks > 90 and marks <= 100:
        print("Topper")
    elif marks > 75 and marks <= 90:
        print("1st Class")
    elif marks > 55 and marks <= 75:
        print("2nd Class")
    elif marks > 40 and marks <= 55:
        print("3rd Class")
    else:
        print("Fail")
else:
    print("Out of Range")