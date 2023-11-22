i = int(input("Enter Starting Number: "))
j = int(input("Enter End Number: "))

while i<=j:
    k = -1
    l = 2
    while l<=i/2:
        if i%l == 0:
            k = k+1
            l = l+1
        else:
            l = l+1
    if k == -1:
        print(i, end=",")
        i = i+1
    else:
        i = i+1