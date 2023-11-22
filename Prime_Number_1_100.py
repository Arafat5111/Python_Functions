start = 2
end = 101
for i in range(start, end):
    for j in range(start, end):
        if i%j == 0:
            break

    if i==j:
        print(i, end=",")