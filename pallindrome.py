def is_pallindrome(num):
    original_num = num
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    if reversed_num == original_num:
        return "is a pallindrome"
    else:
        return "is not a pallindrome"
a = int(input("Enter a number: "))
print(a,is_pallindrome(a))