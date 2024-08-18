data = "Python Rules!"

# Obtain a list of words in the string
words = data.split()
print(words)

# Convert the string to uppercase
upper = data.upper()
print(upper)

# Locate the position of string "rules"
location = data.find("Rules")
print(location)

# Replace the exclamation mark with a question mark
replace = data.replace("!", "?")
print(replace)