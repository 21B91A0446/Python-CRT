num = int(input("Enter any number: "))
count = 0
if num > 1:
    for i in range(2,int(num/2)+1):
        if num%i == 0:
            count += 1
    if count == 0:
        print(num,"is a prime")
    else:
        print(num,"is a composite")