low = int(input("Enter lower value: "))
high = int(input("Enter higher value: "))
for n in range(low,high+1):
    c = 0
    for i in range(2,(n // 2) + 1):
        if n%i == 0:
            c += 1
            break
    if c == 0:
        print(n,end=" ")