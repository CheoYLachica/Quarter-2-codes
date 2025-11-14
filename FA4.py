total_class_score = 0
total_scores_counted = 0

for i in range(1, num_students + 1):
    print(f"Student {i}")
    student_total_score = 0

    for j in range(1, num_subjects + 1):
        score = int(input(f"Enter score {j}: "))
        student_total_score += score
        total_scores_counted += 1

    student_average = student_total_score / num_subjects
    print(f"Average for Student {i} = {student_average:.1f}")

total_class_score += student_total_score

if total_scores_counted > 0:
    class_average = total_class_score / total_scores_counted
    print(f"Class Average = {class_average:.1f}")
else:
    print("No scores were entered, class average cannot be calculated.")