test_score = 49.99
grade = ''  # Initialize grade variable

# Grading logic
if test_score >= 70:
    grade = "A"
elif test_score >= 60:
    grade = "B"
elif test_score >= 50:
    grade = "C"
else:
    grade = "F"


print(f"Test Score: {test_score}, Grade: {grade}")