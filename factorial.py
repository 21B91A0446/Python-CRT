def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)
num = int(input("Enter any number: "))
res = fact(num)
print("Factorial of {} is {}".format(num,res))