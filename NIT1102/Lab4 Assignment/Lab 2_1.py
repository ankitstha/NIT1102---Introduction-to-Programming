"""
File Name: Lab 2_1
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

filename = input("Enter your filename: ")

# Open the file
f = open(filename + ".txt", "w") 
f.write("Name\tHours\tWages\n")
f.close()
# Get Employees Information

employee_num = int(input("Enter the number of employees: "))
for i in range(employee_num):
    name = input("Enter the name of the employee: ")
    hours_worked = float(input("Enter the number of hours worked: "))
    hourly_wage = float(input("Enter the hourly wage: "))

    # Calculate the wages paid
    total_wage = hours_worked * hourly_wage

    # Write the information to the file
    f = open(filename + ".txt", "a")
    f.write(f"{name}\t{hours_worked}\t\t{total_wage}\n")
    f.close()

"""
Peer Review
My Peer:
Name: Ryan Bower
Student ID: s8128380
Feedback: Code is effective and runs correctly. shown to work with multiple different inputs
giving correct outputs as well as being easily readable. however could use more annotations to show 
understanding of the code and task given.
"""