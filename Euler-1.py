def multiples3or5(n):
    if n % 3 == 0 or n % 5 == 0:
        return True
    else:
        return False
sum = 0
for i in range(1, 1000):
    #print ("checkin", i)
    if multiples3or5(i):
        #print("multiples is fine for", i)
        sum = sum + i
        #print ("sum is", sum)
print (sum)

