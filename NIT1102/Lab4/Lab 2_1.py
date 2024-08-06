"""
File Name: Lab 121
Lab Activity: Part 2 Question C

Author: Ankit Shrestha
Student ID: s8117545
Date: 8/07/2024

Program Description: 
Write a program that inputs a filename from the user and prints to the terminal a report of the wages paid to the employees for the given period. 
The report should be in tabular format with the appropriate header. 
Each line should contain an employee’s name, the hours worked, and the wages paid for that period.
"""
 # Get the filename from the user

#filename = input("Enter your filename: ")

# Open the file

f = open("filenam.txt", "w")
f.write("Employee Name \tHours Worked \tWages Paid \n")
f.close()

# Get Employees Information

employee_num = int(input("Enter the number of employees: "))
for i in range(employee_num):
    name = input("Enter the name of the employee: ")
    hours_worked = float(input("Enter the number of hours worked: "))
    wages_paid = float(input("Enter the wages paid: "))

    # Write the information to the file

    f = open("filenam.txt", "a")
    f.write("%15s%15.2f%15.2f" % \
          (name, hours_worked, wages_paid))
    #f.write(f"{name} \t{hours_worked} \t{wages_paid} \n")
    f.close()