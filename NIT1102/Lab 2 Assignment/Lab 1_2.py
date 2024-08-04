"""
File Name: Lab 1_2
Lab Activity: Part 2 Question D

Author: Ankit Shrestha
Student ID: s8117545
Date: 8/01/2024

Program Description: A program that inputs the payment per task, the number of tasks, the bonus percentage,
the task threshold for the bonus and display the freelancer's total payment.
"""

# Ask the user to input the required values
paymentPerTask = int(input("Enter the payment per task: "))
numberOfTask = int(input("Enter the number of task: "))
bonusPercentage = float(input("Enter the bouns percentage: "))
taskThreshold = int(input("Enter the task threshold: "))

# Calculations
total_payment = paymentPerTask * numberOfTask  #Total payment without the bonus
if numberOfTask > taskThreshold: #If the number of task done is greater than the task threshold print the total payment with the bonus
    bonus_amount = total_payment * bonusPercentage / 100
    total_payment = total_payment + bonus_amount
    print("The total payment is $",total_payment)
else:  #If the number of task done is less than the task threshold print the total payment without the bonus
    print("The total payment is $",total_payment)
    


"""
Peer Review student id and name: s8099162, Sam Greco
Feedback: The code works well and no errors have been noticed.

"""


