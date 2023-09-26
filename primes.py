"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes < 1:
        raise ValueError("Your number should be greater than 0")
    count = 0
    num = 2
    while count < number_of_primes:
        prime = True
        for i in range (num-1, 1, -1):
            if num % i == 0:
                prime = False
                break
        if prime == True:
            list.append(num)
            count += 1
        num += 1
    return list

print(primes(10))

