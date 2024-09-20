char = input("Enter a String: ")
if char == char[::-1]:
    print(char,"is a pallindrome")
else:
    print(char,"is not a pallindrome")