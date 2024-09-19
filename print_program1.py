n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
print("add --> Sum of n1, n2")
print("sub --> Difference between n1,n2")
print("mul --> Product of n1, n2")
print("div --> n1 divided by n2")
print("fdiv --> floor division of n1 with n2")
print("mdiv --> modulo division of n1 with n2")
print("sq --> Square of n1, n2")
print("cb --> Cube of n1, n2")
op = input("Enter any option: ")
def calci(n1,n2):
    if op == "add":
        return n1+n2
    elif op == "sub":
        return n1-n2
    elif op == "mul":
        return n1*n2
    elif op == "div":
        return n1/n2
    elif op == "fdiv":
        return n1//n2
    elif op == "mdiv":
        return n1%n2
    elif op == "sq":
        return n1**2, n2**2
    elif op == "cb":
        return n1**2, n2**3
    else:
        return "Wrong option please enter any option only from the above."
print(calci(n1,n2))