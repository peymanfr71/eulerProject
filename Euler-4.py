#The sum of the squares
sum_of_squares = sum(x**2 for x in range(1, 101))
#print(sum_of_squares)

#The square of the sum of the first 
square_of_sum = sum(range(1, 101)) ** 2
#print(square_of_sum)

#Calculate the difference
difference = square_of_sum - sum_of_squares
print("Difference:", difference)
