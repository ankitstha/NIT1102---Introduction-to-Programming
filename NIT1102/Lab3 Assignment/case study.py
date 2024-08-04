startingBalance = int(input("Enter the starting balance: "))
numOfYears = int(input("Enter the number of years: "))
interestRate = float(input("Enter the rate as % "))
totalInterestRate = 0.0
interestRate = interestRate / 100
print("%4s%18s%16s%16s" % \
       ("Year", "Starting Balance", "Interest", "Ending Balance"))
for year in range(1, numOfYears+1):
    interest = startingBalance * interestRate
    endBalance = startingBalance + interest