#i'm sorry, I got help from chatGPT :)

def largest_prime_factor(number):
    factor = 2
    while factor * factor <= number:
        while number % factor == 0:
            number //= factor
        factor += 1
    return number

# Example usage for the number 600851475143
number_to_check = 600851475143
result = largest_prime_factor(number_to_check)
print(result)