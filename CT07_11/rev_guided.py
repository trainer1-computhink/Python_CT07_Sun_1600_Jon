# Qns: Class Result Analysis with Functions (Guided Practice)

students = [
    ["Alex", 85, 92, 78],
    ["Ben", 42, 55, 61],
    ["Clara", 73, 80, 69],
    ["Dylan", 91, 88, 95],
    ["Eva", 58, 63, 70],
    ["Farah", 67, 72, 66],
    ["George", 81, 79, 84],
    ["Hannah", 95, 97, 93]
]

# ==================================================
# Task 1: Get Total Scores
# ==================================================
# Function Name: get_total_scores
# Parameter: students (list)
# Return Type: list
#
# Goal:
# Return a list containing each student's total score.
#
# Hint:
# Each student is stored like this:
# ["Alex", 85, 92, 78]
#
# English mark is at index 1
# Math mark is at index 2
# Science mark is at index 3

def get_total_scores(students):
    total_scores = []

    # TODO:
    # Loop through students
    # Calculate each student's total
    # Add the total into total_scores

    return total_scores


# ==================================================
# Task 2: Analyse Scores
# ==================================================
# Function Name: analyze_scores
# Parameter: total_scores (list)
# Return Type: None
#
# Goal:
# Print:
# - highest score
# - lowest score
# - number of students
# - average score
#
# You should use:
# max(), min(), len()

def analyze_scores(total_scores):
    # TODO:
    # highest = ...
    # lowest = ...
    # count = ...
    # average = ...

    # TODO:
    # Print the results neatly
    pass


# ==================================================
# Task 3: Build 1D Summary List
# ==================================================
# Function Name: build_summary
# Parameters:
# - students (list)
# - total_scores (list)
# Return Type: list
#
# Goal:
# Return a 1D list in this format:
# ["Alex", 255, "Pass", "Ben", 158, "Pass", ...]
#
# Rule:
# If total score >= 150, status is "Pass"
# Otherwise, status is "Fail"

def build_summary(students, total_scores):
    result_summary = []

    # TODO:
    # Loop through students
    # Get the student's name
    # Get the student's total score from total_scores
    # Decide Pass or Fail
    # Append name, total, and status into result_summary

    return result_summary


# ==================================================
# Task 4: Convert 1D List to 2D List using Slicing
# ==================================================
# Function Name: convert_to_table
# Parameter: result_summary (list)
# Return Type: list
#
# Goal:
# Convert:
# ["Alex", 255, "Pass", "Ben", 158, "Pass"]
#
# Into:
# [
#   ["Alex", 255, "Pass"],
#   ["Ben", 158, "Pass"]
# ]
#
# Hint:
# Each row has 3 items.
# Use slicing:
# result_summary[i:i+3]

def convert_to_table(result_summary):
    result_table = []

    # TODO:
    # Loop from 0 to the length of result_summary
    # Increase by 3 each time
    # Slice 3 items each time
    # Add the slice into result_table

    return result_table


# ==================================================
# Task 5: Print Final Table
# ==================================================
# Function Name: print_table
# Parameter: result_table (list)
# Return Type: None
#
# Goal:
# Print each row like this:
# Alex - 255 - Pass

def print_table(result_table):
    # TODO:
    # Loop through result_table
    # Get name, total, and status from each row
    # Print neatly
    pass


# ==================================================
# Task 6: Main Function
# ==================================================
# Function Name: main
# Parameter: students (list)
# Return Type: None
#
# Goal:
# Call all the functions in the correct order.

def main(students):
    # Step 1: Get total scores
    total_scores = get_total_scores(students)

    # Step 2: Analyse scores
    analyze_scores(total_scores)

    # Step 3: Build 1D summary list
    result_summary = build_summary(students, total_scores)

    # Step 4: Convert 1D summary into 2D table
    result_table = convert_to_table(result_summary)

    # Step 5: Print final table
    print_table(result_table)


# ==================================================
# Task 7: Call main
# ==================================================

main(students)