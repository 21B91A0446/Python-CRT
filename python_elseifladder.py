'''
Python program to check the given letter is vowel or consonant
'''
alpha = input("Enter any letter: ")
if alpha.isalpha():
    if alpha == 'a' or alpha == 'A':
        print("{} is a vowel".format(alpha))
    elif alpha == 'e' or alpha == 'E':
        print("{} is a vowel".format(alpha))
    elif alpha == 'i' or alpha == 'I':
        print("{} is a vowel".format(alpha))
    elif alpha == 'o' or alpha == 'O':
        print("{} is a vowel".format(alpha))
    elif alpha == 'u' or alpha == 'U':
        print("{} is a vowel".format(alpha))
    else:
        print("{} is a consonant".format(alpha))
else:
    print("Invalid input. Please enter only letter")