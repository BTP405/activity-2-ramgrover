def is_prime(num):  #This line defines a function named is_prime that takes a single argument num, representing a positive integer.
    for j in range(2, num):#This line starts a for loop that iterates over the range from 2 to num - 1. The loop variable is j.
        if num % j == 0:
            return False
    return True

def getPrimeNumbers(n):#This line defines another function named getPrimeNumbers that takes a single argument n, representing an upper limit.
    return [num for num in range(2, n+1) if is_prime(num)]#This line uses a list comprehension to generate a list of prime numbers between 2 and n (inclusive). It iterates over the range from 2 to n, and includes only those numbers for which the is_prime function returns True.

# Example usage:
n = 10
prime_numbers = getPrimeNumbers(n)
print(f"Prime numbers between 2 and {n}: {prime_numbers}")


getPrimeNumbers(10)

