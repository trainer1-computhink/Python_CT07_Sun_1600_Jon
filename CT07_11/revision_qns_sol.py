# Qns: Class Result Analysis Solution

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

total_scores = []

for i in range(len(students)):
    total = students[i][1] + students[i][2] + students[i][3]
    total_scores.append(total)

print("Total Scores:", total_scores)


# =========================
# Task 2: Analyse the Total Scores
# =========================

highest = max(total_scores)
lowest = min(total_scores)
count = len(total_scores)
average = sum(total_scores) / count

print("Highest total score:", highest)
print("Lowest total score:", lowest)
print("Number of students:", count)
print("Average total score:", average)


# =========================
# Task 3: Create Result Summary (1D List)
# =========================

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

print("Result Summary (1D):", result_summary)


# =========================
# Task 4: Convert 1D → 2D using slicing
# =========================

result_table = []

for i in range(0, len(result_summary), 3):
    row = result_summary[i:i+3]
    result_table.append(row)

print("Result Table (2D):", result_table)


# =========================
# Task 5: Print Final Table
# =========================

for i in range(len(result_table)):
    name = result_table[i][0]
    total = result_table[i][1]
    status = result_table[i][2]

    print(name + " - " + str(total) + " - " + status)