# Qns: Class Result Analysis with Functions (Solution)

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

def get_total_scores(students):
    total_scores = []

    for i in range(len(students)):
        total = students[i][1] + students[i][2] + students[i][3]
        total_scores.append(total)

    return total_scores


# ==================================================
# Task 2: Analyse Scores
# ==================================================

def analyze_scores(total_scores):
    highest = max(total_scores)
    lowest = min(total_scores)
    count = len(total_scores)
    average = sum(total_scores) / count

    print("Highest total score:", highest)
    print("Lowest total score:", lowest)
    print("Number of students:", count)
    print("Average total score:", average)


# ==================================================
# Task 3: Build 1D Summary List
# ==================================================

def build_summary(students, total_scores):
    result_summary = []

    for i in range(len(students)):
        name = students[i][0]
        total = total_scores[i]

        if total >= 150:
            status = "Pass"
        else:
            status = "Fail"

        result_summary.append(name)
        result_summary.append(total)
        result_summary.append(status)

    return result_summary


# ==================================================
# Task 4: Convert 1D List to 2D List using Slicing
# ==================================================

def convert_to_table(result_summary):
    result_table = []

    for i in range(0, len(result_summary), 3):
        row = result_summary[i:i+3]
        result_table.append(row)

    return result_table


# ==================================================
# Task 5: Print Final Table
# ==================================================

def print_table(result_table):
    for i in range(len(result_table)):
        name = result_table[i][0]
        total = result_table[i][1]
        status = result_table[i][2]

        print(name + " - " + str(total) + " - " + status)


# ==================================================
# Task 6: Main Function
# ==================================================

def main(students):
    total_scores = get_total_scores(students)
    analyze_scores(total_scores)
    result_summary = build_summary(students, total_scores)
    result_table = convert_to_table(result_summary)
    print_table(result_table)


# ==================================================
# Task 7: Call main
# ==================================================

main(students)