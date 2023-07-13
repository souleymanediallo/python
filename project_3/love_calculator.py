# Love Calculator
# Instructions
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# > Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."
name_1 = input("What is your name ? ").upper()
name_2 = input("What is her name ? ").upper()
total_name = name_1 + name_2

score_true = 0
score_love = 0

for letter in total_name:
    if letter in "TRUE":
        score_true += 1
    if letter in "LOVE":
        score_love += 1

score_as_str = str(score_true) + str(score_love)
score = int(score_as_str)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")

# Example
# name_1 = "Jay z"
# name_2 = "Beyonce"

# Output 1
# Your score is 23.