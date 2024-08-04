"""
File Name: Lab 1_3
Lab Activity: Part 2 Question A

Author: Ankit Shrestha
Student ID: s8117545
Date: 8/01/2024

Program Description: A program that that displays a salary schedule, 
in tabular format, for teachers in a school district
"""

# Get the required values from the user

startingSalary = int(input("Enter the starting salary: "))
percentgeIncrease = float(input("Enter the percentage increase: "))
numberOfYears = int(input("Enter the number of years: "))

# Print the header of the table

print("%15s%15s%15s" % \
      ("Year", "Salary", "IncreaseAmount"))

# Calculate the salary and increase for each year and print them

for year in range(1, numberOfYears + 1):    # Loop through the years
    salary = startingSalary * (1 + percentgeIncrease / 100) ** year # Calculate the salary
    increaseAmount = salary - startingSalary # Calculate the increase amount every year
    print("%15d%15.2f%15.2f" % \
          (year, salary, increaseAmount)) # Print the year, salary and increased amount of salary

"""
Peer Review student id and name: s8099162, Sam Greco
Feedback: Code looks great, No errors occured andthe output was as expected.
"""