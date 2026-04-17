count = 0
total = 0

for number in range (10):
    student_score = int(input(f"Enter score {number}: "))
    total += student_score
    count += 1
average = total / count
print(average)
