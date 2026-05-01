first_score = float(input("Enter first exam score: "))
second_score = float(input("Enter second exam score: "))
third_score = float(input("Enter first exam score: "))

lowest_score = min(first_score, second_score, third_score)
highest_score = max(first_score, second_score, third_score)
middle_score = 0

if lowest_score == first_score and highest_score == second_score:
    middle_score = third_score

elif lowest_score == second_score and highest_score == third_score:
    middle_score = first_score

elif lowest_score == third_score and highest_score == first_score:
    middle_score = second_score

elif lowest_score == first_score and highest_score == third_score:
    middle_score = second_score

elif lowest_score == second_score and highest_score == first_score:
    middle_score = third_score

elif lowest_score == third_score and highest_score == second_score:
    middle_score = first_score

weighted_average = (0.4 * highest_score) + (0.35 * middle_score) + (0.25 * lowest_score)
print(f"Weighted average = {weighted_average}")

