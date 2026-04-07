count = int(input("Enter no of primes: "))
num = 2
primes = []

while len(primes) < count:
    is_prime = True
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)
        
    num += 1

print(f"The first {count} primes are: ",primes)