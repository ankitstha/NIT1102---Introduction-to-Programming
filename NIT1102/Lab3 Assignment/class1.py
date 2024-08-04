lowerBound = int(input("Enter the lower bound: "))
upperBound = int(input("Enter the upper bound: "))
sum = 0
for count in range(lowerBound, upperBound+1):
    sum = sum + count
    print(sum)