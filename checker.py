scores = [75, 40, 85, 60, 30]

total = sum(scores)
print("Total score:", total)

average = total / len(scores)
print("Average:", average)

highest_score = max(scores)
print("Highest score:", highest_score)

lowest_score = min(scores)
print("Lowest score:", lowest_score)

passed = 0
failed = 0
for score in scores:
    if score >= 50:
        passed += 1
    else:
        failed += 1
print("Students passed:", passed)
print("Students failed:", failed)


scores = [95, 82,  67, 54, 43, 29, 78]
total = sum(scores)
print("Total:", total)

average = total / len(scores)
print("Average:", average)

highest = max(scores)
print("Highest:", highest)

lowest = min(scores)
print("Lowest:", lowest)

passed = 0
failed = 0
grade_a = 0
grade_b = 0
grade_c = 0
grade_d = 0
grade_e = 0
grade_f = 0
for score in scores:

    if score >= 50:
        passed += 1
    else:
        failed += 1

    if  score >= 80:
        grade_a += 1

    elif score >= 70:
        grade_b += 1

    elif score >= 60:
        grade_c += 1

    elif score >= 50:
        grade_d += 1

    elif score >= 40:
        grade_e += 1
    else:
        grade_f += 1

print("Students passed:", passed)
print("Students failed:", failed)
print("Students grade_a:", grade_a)
print("Students grade_b:", grade_b)
print("Students grade_c:", grade_c)
print("Students grade_d:", grade_d)
print("Students grade_e:", grade_e)
print("Students grade_f:", grade_f)