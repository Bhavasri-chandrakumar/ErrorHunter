
def is_prime(num):
    if num <= 1:
        return False
    elif num == 2 or num == 3:
        return True
    else:
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                return False
        return True

# Input validation loop
while True:
    try:
        n = int(input("Enter a number: "))
        break
    except ValueError:
        print("Please enter a valid integer.")

# Display the result
if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
