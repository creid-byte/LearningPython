i = 10
print("Getting sums up to", i)
while (i > -1):
    sum = 0
    j = i
    while j > 0:
        if j > 1:
            print(j, "+", end=" ")
        else:
            print(j, "=", end=" ")
        sum += j
        j -= 1
    print(sum)
    i -= 1

    print('\n')

    for w in range(10):
        for q in range(w,10):
            print(q, end=' ')
        print()