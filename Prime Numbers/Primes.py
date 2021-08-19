for i in range(0,3000): # 3000 is the maximum number, this value can be changed depending how high you want to search for primes
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)
