"""
File Name: Lab 1_1
Lab Activity: Part 2 Question F

Author: Ankit Shrestha
Student ID: s8117545
Date: 7/31/2024

Program Description: A program that converts hours to its equivalent in minutes first then to seconds 
and prints the results on the screen.  The program should request a number 
representing the hours and converts it into minutes then seconds
"""
# Define Minutes per hour and Seconds per minute
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60

# Ask user for input
hour = int(input("Enter the hour you want to convert: "))

# Convert hour into minutes and print it
minutes = hour * MINUTES_PER_HOUR
print(hour,"hour is equivalent to", minutes,"minutes")

# Convert minutes into seconds and print it
seconds = minutes * SECONDS_PER_MINUTE
print(hour,"hour is equivalent to", seconds,"seconds")

"""
Peer Review student id and name: s8099162, Sam Greco
Feedback: Works Perfectly
"""