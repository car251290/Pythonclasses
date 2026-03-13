def calification_score(grade):
    if grade >= 90:
        return '4'
    elif grade >= 80:
        return '3'
    elif grade >= 70:
        return '2'
    elif grade >= 60:
        return '1'
    else:
        return '0'


# Inputs
participation = float(input("Enter the participation grade (0-100): "))
homework = float(input("Enter the homework grade (0-100): "))
project = float(input("Enter the project grade (0-100): "))

# Calculate final grade
# Example weights: Participation 20%, Homework 30%, Project 50%
final_grade = (participation * 0.2) + (homework * 0.3) + (project * 0.5)

# Convert to calification score
score = calification_score(final_grade)

print(f"\nFinal Grade: {final_grade:.2f}")
print(f"Calification Score (0-4 scale): {score}")