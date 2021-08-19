for i in range(0,3000): # 3000 is the maximum number, this value can be changed depending how high you want to search for primes
    if i > 1: # 1 isn't a prime number :P 
        for j in range(2, i): # Loop checking every number from 2-3000
            if (i % j) == 0: # If any number in the sequence can be perfectly divided then then loop breaks and moves to the next number
                break
        else:
            print(i) # Prints a prime number if previous condition isn't satisfied
