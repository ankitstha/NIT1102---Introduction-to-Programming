"""
File Name: Lab 2_2
Lab Activity: Part 2 Question C

Author: Ankit Shrestha
Student ID: s8117545
Date: 8/08/2024

Problem:
Modify the sentence-generator program created in part 1 so that it inputs its 
vocabulary from a set of text files at startup. 
The filenames are nouns.txt, verbs.txt, articles.txt, and prepositions.txt.
"""

import random
#nouns = "D:/Victoria University/NIT1102/Lab5 Assignment/nouns.txt"
#verbs = "D:/Victoria University/NIT1102/Lab5 Assignment/verbs.txt"
#articles = "D:/Victoria University/NIT1102/Lab5 Assignment/articles.txt"
#prepositions = "D:/Victoria University/NIT1102/Lab5 Assignment/prepositions.txt"

file_name = {"noun":"D:/Victoria University/NIT1102/Lab5 Assignment/nouns.txt", "verbs":"D:/Victoria University/NIT1102/Lab5 Assignment/verbs.txt", "articles":"D:/Victoria University/NIT1102/Lab5 Assignment/articles.txt", "prepositions":"D:/Victoria University/NIT1102/Lab5 Assignment/prepositions.txt"}
def read_file(file_name):
    with open(file_name, "r") as file:
        words = file.readlines()
        words = [word.strip() for word in words]
    return words