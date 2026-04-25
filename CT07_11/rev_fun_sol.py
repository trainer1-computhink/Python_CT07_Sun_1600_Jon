# Qns: Student Score Analyzer Solution

marks = [85, 42, 73, 91, 58, 67, 81, 95]


# =========================
# Task 1: get_total
# Parameter: marks (list of integers)
# Return Type: integer
# =========================

def get_total(marks):
    total = 0

    for i in range(len(marks)):
        total = total + marks[i]

    return total


# =========================
# Task 2: get_average
# Parameter: marks (list of integers)
# Return Type: float
# =========================

def get_average(marks):
    total = get_total(marks)
    average = total / len(marks)

    return average


# =========================
# Task 3: count_pass
# Parameter: marks (list of integers)
# Return Type: integer
# =========================

def count_pass(marks):
    pass_count = 0

    for i in range(len(marks)):
        if marks[i] >= 50:
            pass_count = pass_count + 1

    return pass_count


# =========================
# Task 4: analyze_marks
# Parameter: marks (list of integers)
# Return Type: None
# =========================

def analyze_marks(marks):
    total = get_total(marks)
    average = get_average(marks)
    pass_count = count_pass(marks)

    print("Total marks:", total)
    print("Average mark:", average)
    print("Number of passing students:", pass_count)


# =========================
# Task 5: Call the function
# =========================

analyze_marks(marks)


# =========================
# Task 6: count_pass with passing_mark
# Parameter:
# - marks (list of integers)
# - passing_mark (integer)
# Return Type: integer
# =========================

def count_pass_with_mark(marks, passing_mark):
    pass_count = 0

    for i in range(len(marks)):
        if marks[i] >= passing_mark:
            pass_count = pass_count + 1

    return pass_count


print("Number of students scoring 60 and above:", count_pass_with_mark(marks, 60))