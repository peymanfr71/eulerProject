#Even number function
def Even(n):
    if n % 2 == 0:
        return True
    else:
        return False
first = 1
second = 2

sum = 0

while (first < 4000000):
    if Even(first):
        sum = sum + first
    new = first + second
    first = second
    second = new
print (sum) 