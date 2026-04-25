# Qns: Class Result Analysis

# A teacher records student results in groups.
# Each inner list contains:
# [student name, English mark, Math mark, Science mark]

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

# =========================
# Task 1: Extract Total Scores
# =========================

# Create a list called total_scores.
# Each student's total score is English + Math + Science.
#
# Example:
# Alex's total = 85 + 92 + 78

# =========================
# Task 2: Analyse the Total Scores
# =========================

# Using total_scores, find and print:
# 1. The highest total score
# 2. The lowest total score
# 3. The number of students
# 4. The average total score

# You must use:
# - max()
# - min()
# - len()

# =========================
# Task 3: Create Result Summary
# =========================

# Create a 1D list called result_summary.
# For each student, add the following 3 items into result_summary:
# name, total score, result status
#
# If total score is 150 or above, the status is "Pass".
# Otherwise, the status is "Fail".
#
# Example:
# ["Alex", 255, "Pass", "Ben", 158, "Pass", ...]

# =========================
# Task 4: Convert 1D List into 2D List
# =========================

# Convert result_summary into a 2D list called result_table.
# Each inner list should contain 3 items:
# [name, total score, result status]
#
# You MUST use list slicing.
#
# Example:
# [
#   ["Alex", 255, "Pass"],
#   ["Ben", 158, "Pass"],
#   ...
# ]

# =========================
# Task 5: Print the Final Result Table
# =========================

# Print each row neatly:
#
# Alex - 255 - Pass
# Ben - 158 - Pass
# ...