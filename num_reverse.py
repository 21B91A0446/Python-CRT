def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    print("Reverse number is: ",reversed_num)
a = int(input("Enter any number: "))
reverse = reverse_number(a)
#print("The reversed number is: ",reverse_number)